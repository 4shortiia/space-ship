import os
import json
import requests
import re  # Added for regex matching
import google.generativeai as genai

# Configuration: Extensions to look for
SUPPORTED_EXTENSIONS = {
    # JavaScript / TypeScript & Flavors
    '.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs',
    # Modern Frameworks
    '.vue', '.svelte', '.astro',
    # Styling
    '.css', '.scss', '.sass', '.less', '.styl',
    # Markup & Templates
    '.html', '.htm', '.pug', '.ejs', '.handlebars', '.hbs',
    # Backend / Other
    '.json', '.go', '.java', '.cpp', '.c' , '.md'
}

# Directories to ignore
IGNORE_DIRS = {
    '.git', '.github', '.vscode', '.idea', 
    'node_modules', 'bower_components', 
    'dist', 'build', 'out', 'coverage', 
    '__pycache__', 'venv', 'bin', 'obj', 
    '.next', '.nuxt', '.astro'
}

# Curated learning resources
LEARNING_RESOURCES = """
**HTML & Semantic Markup:**
- MDN HTML Basics: https://developer.mozilla.org/en-US/docs/Learn/HTML
- Web.dev Learn HTML: https://web.dev/learn/html

**CSS & Styling:**
- CSS-Tricks Complete Guide: https://css-tricks.com/guides/
- MDN CSS Layout: https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout
- Flexbox Froggy (Game): https://flexboxfroggy.com/
- Grid Garden (Game): https://cssgridgarden.com/

**JavaScript Basics:**
- JavaScript.info (ქართულად): https://javascript.info/
- MDN JavaScript Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- Eloquent JavaScript (Free Book): https://eloquentjavascript.net/

**Forms & Validation:**
- MDN Forms Guide: https://developer.mozilla.org/en-US/docs/Learn/Forms
- Web.dev Sign-in Form Best Practices: https://web.dev/sign-in-form-best-practices/

**Accessibility:**
- Web.dev Learn Accessibility: https://web.dev/learn/accessibility
- A11y Project Checklist: https://www.a11yproject.com/checklist/

**General Best Practices:**
- Web.dev Learn: https://web.dev/learn
- Frontend Checklist: https://frontendchecklist.io/
"""

def get_pr_commits(repo, pr_number, token):
    """Fetch all commits from a PR"""
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/commits"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    # Page size increased to 100 to ensure we catch most commits
    params = {"per_page": 100} 
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_commit_changes(repo, commit_sha, token):
    """Fetch the files changed in a specific commit"""
    url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def should_ignore_file(file_path):
    """Check if file should be ignored based on path or extension"""
    for ignore_dir in IGNORE_DIRS:
        if f"/{ignore_dir}/" in file_path or file_path.startswith(f"{ignore_dir}/"):
            return True
    ext = os.path.splitext(file_path)[1]
    return ext not in SUPPORTED_EXTENSIONS

def get_reviewed_shas(repo, pr_number, token):
    """
    Fetches existing comments on the PR to find which commits 
    have already been reviewed by the AI.
    Returns a set of short_shas (e.g., {'7b3f1a', ...}).
    """
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {"per_page": 100} # Get last 100 comments
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        comments = response.json()
        
        reviewed_shas = set()
        
        # We look for the pattern **[`short_sha`]** which matches the output format
        # Regex explanation:
        # \*\*\[`  -> Matches literal **[`
        # ([a-f0-9]+) -> Captures the hex string (the SHA)
        # `\]\*\* -> Matches literal `]**
        sha_pattern = re.compile(r"\*\*\[`([a-f0-9]+)`\]\*\*")
        
        for comment in comments:
            body = comment.get('body', '')
            # Only look at comments that look like our AI reviews
            if "🎓 კომიტების მიმოხილვა (AI Mentor)" in body:
                found_shas = sha_pattern.findall(body)
                reviewed_shas.update(found_shas)
                
        print(f"👀 Found existing reviews for commits: {reviewed_shas}")
        return reviewed_shas

    except Exception as e:
        print(f"⚠️ Could not fetch existing comments: {e}")
        return set()

def post_comment(repo, pr_num, token, body):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_num}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"body": f"### 🎓 კომიტების მიმოხილვა (AI Mentor)\n\n{body}"}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("✅ Comment posted successfully!")
    else:
        print(f"❌ Failed to post comment: {response.status_code}")

def main():
    # --- 1. SETUP ---
    gemini_key = os.getenv("GEMINI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")

    if not gemini_key or not github_token:
        print("❌ Error: Missing API Key or Token.")
        return

    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # --- 2. GET CONTEXT ---
    repo_full_name = os.getenv("GITHUB_REPOSITORY")
    event_path = os.getenv("GITHUB_EVENT_PATH")
    
    with open(event_path, 'r') as f:
        event_data = json.load(f)
    
    if 'pull_request' in event_data:
        pr_number = event_data['pull_request']['number']
    else:
        print("⚠️ Not a Pull Request event. Ensure this runs in a PR context for comments.")
        return

    # --- 3. READ EXERCISE/TASK FILE FOR CONTEXT ---
    exercise_content = ""
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file.lower() in ['readme.md', 'task.md', 'exercise.md', 'assignment.md']:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        exercise_content = f.read()
                        print(f"📋 Found task description: {file_path}")
                        break
                except Exception as e:
                    print(f"⚠️ Could not read {file_path}: {e}")
        if exercise_content:
            break

    # --- 4. CHECK HISTORY & FETCH COMMITS ---
    print("🔍 Checking existing reviews...")
    # Fetch list of SHAs that have already been commented on
    reviewed_shas = get_reviewed_shas(repo_full_name, pr_number, github_token)

    print("🔍 Fetching commits from PR...")
    try:
        commits = get_pr_commits(repo_full_name, pr_number, github_token)
        print(f"✅ Found {len(commits)} total commits in PR")
    except Exception as e:
        print(f"❌ Error fetching commits: {e}")
        return

    # --- 5. REVIEW EACH COMMIT ---
    all_feedback = []
    new_reviews_count = 0
    
    for commit in commits:
        commit_sha = commit['sha']
        short_sha = commit_sha[:7]
        commit_message = commit['commit']['message']
        
        # --- SKIP LOGIC: Check if this SHA is in our reviewed set ---
        if short_sha in reviewed_shas:
            print(f"⏭️  Skipping previously reviewed commit: {short_sha}")
            continue

        print(f"\n📝 Reviewing NEW commit: {short_sha} - {commit_message}")
        
        # Get changed files in this commit
        try:
            commit_data = get_commit_changes(repo_full_name, commit_sha, github_token)
            files = commit_data.get('files', [])
        except Exception as e:
            print(f"❌ Error fetching commit changes: {e}")
            continue
        
        # Build content of changed files
        changed_content = ""
        file_count = 0
        
        for file_info in files:
            file_path = file_info['filename']
            
            # Skip ignored files
            if should_ignore_file(file_path):
                continue
            
            # Get the patch (diff)
            patch = file_info.get('patch', '')
            if patch:
                changed_content += f"\n--- FILE: {file_path} ---\n"
                changed_content += f"Status: {file_info['status']}\n"
                changed_content += f"Changes:\n{patch}\n"
                file_count += 1
        
        if file_count == 0:
            print(f"⚠️ No relevant files changed in this commit, skipping...")
            # We treat empty/irrelevant commits as "reviewed" effectively by not adding them to feedback list,
            # but next time the script runs it might check them again. 
            # To strictly avoid re-checking empty commits, we could store them, but for now this is fine.
            continue
        
        print(f"✅ Analyzing {file_count} changed files...")
        
        # --- 6. CREATE CONCISE MENTORING PROMPT ---
        prompt = f"""
იმოქმედე როგორც დამწყები დეველოპერის მხარდამჭერი და მეგობრული მენტორი. 🇬🇪

**სტუდენტის კონტექსტი (სესია 7: შესავალი CSS-ში):**
სტუდენტი არის აბსოლუტური დამწყები. მან იცის მხოლოდ:
- სემანტიკური HTML ტეგები (<header>, <main>, <section>).
- CSS-ის საბაზისო სინტაქსი და External CSS ფაილის შემოტანა.
- სელექტორები: Element, Class, ID.
- საბაზისო სტილები: ფერები, ფონტები, margin, padding.
*შენიშვნა: მან ჯერ არ იცის Flexbox ან Grid. არ მოსთხოვო ეს ცოდნა.*

**დავალების აღწერა:**
{exercise_content if exercise_content else "დავალების აღწერა არ მოიძებნა. შეაფასე ზოგადი HTML/CSS პრინციპებით."}

**კოდში შესული ცვლილებები:**
{changed_content}

**შეფასების კრიტერიუმები (Checklist):**
1. **HTML Semantics:** შეაქე, თუ იყენებს სემანტიკურ ტეგებს. თუ მხოლოდ <div>-ებს იყენებს, ურჩიე <section> ან <main>.
2. **CSS Method:** შეაქე External .css ფაილის გამოყენება. რბილად ურჩიე, რომ არ გამოიყენოს inline styles (`style="..."`) ან internal `<style>`.
3. **Selectors:** შეამოწმე, იყენებს თუ არა **კლასებს** (.class) სტილიზაციისთვის. თუ იყენებს **ID**-ს (#id) სტილისთვის, აუხსენი, რომ ID უნიკალური ელემენტებისთვისაა, სტილისთვის კი კლასები ჯობია.
4. **Unique IDs:** **მკაცრი წესი:** თუ ხედავ დუბლირებულ ID-ებს (ორ ელემენტს ერთი და იგივე ID აქვს), აუხსენი, რომ ID გვერდზე უნიკალური უნდა იყოს.
5. **Naming:** კლასის სახელები უნდა იყოს ინგლისურ ენაზე და შინაარსობრივი.

**ტონი და სტილი:**
- იყავი რბილი და მეგობრული. გამოიყენე "სენდვიჩის მეთოდი" (შექება -> რჩევა -> გამხნევება).
- გამოიყენე ემოჯიები.
- ენა: **მკაცრად ქართული**.

**პასუხის ფორმატი:**
1. **მისალმება:** "გამარჯობა!" + კონკრეტული შექება კოდზე.
2. **Feedback:** 1-2 წინადადება. თუ კოდი კარგია, უბრალოდ შეაქე. თუ შეცდომაა (მაგ: ID სტილიზაციისთვის), აუხსენი მარტივად.
3. **რესურსი:** მხოლოდ იმ შემთხვევაში, თუ ტექნიკური შეცდომაა, მიეცი 1 ლინკი ქვემოთ მოცემული სიიდან.
4. **ზომა:** იყავი ლაკონური (მაქსიმუმ 500 სიმბოლო).

**ხელმისაწვდომი რესურსები:**
{LEARNING_RESOURCES}
"""
        # --- 7. GET AI FEEDBACK ---
        try:
            ai_response = model.generate_content(prompt)
            feedback = ai_response.text.strip()
            
            # Format the feedback with commit info
            # IMPORTANT: The format `**[`{short_sha}`]**` is used by get_reviewed_shas to identify history
            formatted_feedback = f"**[`{short_sha}`]** {commit_message}\n\n{feedback}"
            all_feedback.append(formatted_feedback)
            new_reviews_count += 1
            
        except Exception as e:
            print(f"❌ Gemini Error for commit {short_sha}: {e}")
            continue

    if not all_feedback:
        print("✨ No new commits to review.")
        return

    # --- 8. POST COMBINED COMMENT ---
    print(f"🚀 Posting feedback for {new_reviews_count} new commits...")
    
    header = "🎓 **AI Mentor Review** - ახალი კომიტების განხილვა\n\n"
    footer = "\n\n---\n\n💡 *ეს feedback გენერირებულია AI-ის მიერ.*"
    combined_feedback = header + "\n\n---\n\n".join(all_feedback) + footer
    post_comment(repo_full_name, pr_number, github_token, combined_feedback)

if __name__ == "__main__":
    main()
