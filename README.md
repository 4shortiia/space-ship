# 🚀 მისია: S.S. SEMANTIC — ეკიპაჟის გადარჩენა

---

## შესავალი

კოსმოსური ხომალდი **S.S. Semantic** მოექცა შავი ხვრელის გრავიტაციულ ველში.  
ეკიპაჟი კრიო-კაფსულებშია — ჟანგბადი იწურება.  
ერთადერთი გამოსავალი: **ჰიპერ-ნახტომი დედამიწისკენ.**

მაგრამ ჰიპერ-ნახტომის სისტემა მხოლოდ **სემანტიკურად გამართულ HTML კოდზე** მუშაობს.  
შენი ამოცანაა — ააწყო ხომალდის კონტროლ-პანელი სწორი HTML სტრუქტურით,  
შეიყვანო საიდუმლო კოდი და ეკიპაჟი სახლში დააბრუნო. 🌍

---

## 🛠️ რა გჭირდება

- ტექსტური რედაქტორი (VS Code, Notepad++ და სხვ.)
- ბრაუზერი (Chrome, Firefox)
- სამი ფაილი: `index.html`, `style.css`, `script.js`

---

## ნაბიჯი 1 — შექმენი ფაილები

შექმენი საქაღალდე სახელად `ss-semantic`.  
საქაღალდეში შექმენი სამი ცარიელი ფაილი:

```
ss-semantic/
├── index.html
├── style.css
└── script.js
```

---

## ნაბიჯი 2 — HTML-ის საფუძველი (`index.html`)

გახსენი `index.html` და დაწერე დოკუმენტის სტრუქტურა, შეიყვანე ! (ძახილის ნიშანი) და დააჭირე enter-ს.

```html
<!doctype html>
<html lang="ka">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>S.S. Semantic | Final Approach</title>
    </head>
    <body>
        <!-- ყველა ხილული კონტენტი აქ -->
    </body>
</html>
```

**რატომ?**

- `<!doctype html>` — ეუბნება ბრაუზერს, რომ ეს HTML5 დოკუმენტია
- `lang="ka"` — ენა ქართულია
- `<meta charset="UTF-8">` — ქართული ასოები სწორად გამოჩნდეს
- `<meta name="viewport">` — მობილურზე სწორი ზომა
- `<link rel="stylesheet">` — CSS ფაილის მიბმა

---

## ნაბიჯი 3 — `<body>` — ხომალდის სხეული

`</head>`-ის შემდეგ გახსენი `<body>`:

```html
<body></body>
```

`<body>`-ს შიგნით ყველა ხილული ელემენტი მოთავსდება.

---

## ნაბიჯი 4 — კოსმოსური ფონი

პირველი ელემენტი `<body>`-ში — ვარსკვლავიანი ფონი:

```html
<div class="space-background">
    <div class="stars"></div>
</div>
```

**კლასები CSS-ში:**

- `.space-background` — შავი ფონი, მთელ ეკრანზე
- `.stars` — ანიმირებული ვარსკვლავები (CSS-ით შეიქმნება)

---

## ნაბიჯი 5 — კოსმოსური სცენა (რაკეტა და დედამიწა)

```html
<div id="space-scene">
    <div id="earth">🌍</div>
    <div id="rocket-container">
        <div id="rocket">
            🚀
            <div id="fire"></div>
        </div>
    </div>
</div>
```

**ID-ები JavaScript-ისთვის:**

| ID                 | რისთვის                                          |
| ------------------ | ------------------------------------------------ |
| `space-scene`      | მთლიანი კოსმოსური სცენა (თავდაპირველად დამალული) |
| `earth`            | დედამიწის ემოჯი                                  |
| `rocket-container` | რაკეტა + ცეცხლი — ერთად მოძრაობენ                |
| `rocket`           | 🚀                                               |
| `fire`             | ცეცხლის ანიმაცია (CSS-ით)                        |

---

## ნაბიჯი 6 — მისიის კონტროლ-პანელი

ეს მთავარი `<div>`-ია, სადაც ყველაფერი ხდება:

```html
<div id="mission-control"></div>
```

`id="mission-control"` — JavaScript ამ div-ს მალავს გაშვების შემდეგ.

---

## ნაბიჯი 7 — `<header>` (სათაური)

`mission-control`-ის შიგნით:

```html
<header class="reveal">
    <div class="alert-blink">⚠️ კრიტიკული მდგომარეობა: სისტემური კოლაფსი</div>
    <h1 class="glitch-text">S.S. SEMANTIC — PROTOCOL 0</h1>
    <nav>
        <ul>
            <li><a href="#bridge">ჟურნალი</a></li>
            <li><a href="#logs">რადარი</a></li>
            <li><a href="#status">სტატუსი</a></li>
        </ul>
    </nav>
</header>
```

**კლასები და ტეგები:**

| ელემენტი                  | დანიშნულება                            |
| ------------------------- | -------------------------------------- |
| `class="reveal"`          | CSS-ანიმაცია — გამოჩნდება გადახვევისას |
| `class="alert-blink"`     | მოციმციმე გაფრთხილება                  |
| `class="glitch-text"`     | glitch-ეფექტი სათაურზე                 |
| `<nav>` + `<ul>` + `<li>` | სემანტიკური ნავიგაცია                  |
| `href="#bridge"`          | გადასვლა იმავე გვერდის სექციაზე        |

---

## ნაბიჯი 8 — აუდიო ფაილი

`</header>`-ის შემდეგ:

```html
<audio id="space-music" src="assets/interstellar.mp3" loop></audio>
```

> `loop` ატრიბუტი — მუსიკა უსასრულოდ მეორდება.

---

## ნაბიჯი 9 — `<main>` სექცია

```html
<main>
    <!-- ყველა <section> აქ -->
</main>
```

`<main>` — სემანტიკური ტეგი, რომელიც გვერდის მთავარ კონტენტს შეიცავს.

---

## ნაბიჯი 10 — კაპიტნის ჟურნალი (`#logs`)

`<main>`-ის შიგნით:

```html
<section id="logs" class="reveal">
    <h2>📡 კაპიტნის ჟურნალი: ვარსკვლავური დრო 4026.4</h2>
    <div class="typing-container">
        <p class="typing-text" id="captain-log">
            "სისტემური ჩანაწერი: 4026.4. ლოკაცია: სექტორი X-7. ხომალდი მოჰყვა
            შავი ხვრელის გრავიტაციულ ველში. კურსიდან გადახრა — კრიტიკულია.
            ეკიპაჟი გადაყვანილია კრიო-კაფსულებში რესურსების დასაზოგად. კავშირი
            დედამიწასთან გაწყვეტილია, ეს ჩანაწერი ავტომატურ რეჟიმში იგზავნება.
            ეს სიგნალი შესაძლოა კოსმოსის წყვდიადში სამუდამოდ ჩაიკარგოს და ვერც
            კი მოაღწიოს დედამიწამდე... სემანტიკური ძრავები მუშაობს მაქსიმალურ
            სიმძლავრეზე — 110%. ერთადერთი გამოსავალი ჰიპერ-ნახტომის
            გააქტიურებაა. დედამიწა ჩვენი სამიზნე წერტილია. ვიწყებ ათვლას."
        </p>
    </div>
</section>
```

**კლასები:**

| კლასი / ID                 | დანიშნულება                                     |
| -------------------------- | ----------------------------------------------- |
| `class="reveal"`           | ჩვენების ანიმაცია                               |
| `class="typing-container"` | ტექსტის კონტეინერი                              |
| `class="typing-text"`      | CSS სტილი საბეჭდ ტექსტს                         |
| `id="captain-log"`         | JavaScript ამ ელემენტს წვდება typeWriter-ისთვის |

---

## ნაბიჯი 11 — ხომალდის ხიდი (`#bridge`)

```html
<section id="bridge" class="reveal">
    <h2>🛰️ კავშირი ხომალდის ხიდთან</h2>
    <div
        class="dialogue-box"
        style="background: rgba(255,255,255,0.05); border-left: 3px solid #39ff14; padding: 15px; margin-bottom: 20px; font-size: 0.9rem;"
    >
        <p>
            <strong>Semantic:</strong>
            „კაპიტანო, შავმა ხვრელმა ხომალდის
            <code>&lt;main&gt;</code>
            სტრუქტურა დააზიანა. დედამიწაზე დასაბრუნებლად ყველა
            <code>&lt;section&gt;</code>
            უნდა დავასტაბილუროთ!"
        </p>
        <p>
            <strong>Flex:</strong>
            „ჩემი გამოთვლებით, მხოლოდ სემანტიკურად გამართული კოდი გაუძლებს
            ჰიპერ-ნახტომის წნევას.
            <code>&lt;header&gt;</code>
            და
            <code>&lt;footer&gt;</code>
            ბლოკები უკვე იზოლირებულია."
        </p>
        <p>
            <strong>Layout:</strong>
            „მე
            <code>&lt;article&gt;</code>
            ტეგში მოვაქციე გადარჩენის გეგმა, კოდი მზად არის. კაპიტანო, შენს
            ბრძანებას ველოდებით!"
        </p>
    </div>
</section>
```

**ახალი ტეგები:**

| ტეგი             | დანიშნულება                                 |
| ---------------- | ------------------------------------------- |
| `<strong>`       | სემანტიკური გამუქება (მნიშვნელოვანი სიტყვა) |
| `<code>`         | კოდის ფრაგმენტი ტექსტში                     |
| `&lt;` და `&gt;` | `<` და `>` სიმბოლოები HTML-ში               |

---

## ნაბიჯი 12 — გარე ვიზუალიზაცია (`#visuals`)

```html
<section id="visuals" class="reveal">
    <h2>🔭 გარე ვიზუალიზაცია</h2>
    <div class="img-frame">
        <img src="assets/cosmos.jpeg" alt="Cosmos" class="zoom-img" />
    </div>
    <p class="sub-text">
        სექტორი: X-7. ობიექტი: ანდრომედას აფეთქებული ვარსკვლავი.
    </p>
</section>
```

**მნიშვნელოვანი:**

| ატრიბუტი           | დანიშნულება                            |
| ------------------ | -------------------------------------- |
| `src`              | სურათის მისამართი                      |
| `alt="Cosmos"`     | სურათის ტექსტური აღწერა (სავალდებულო!) |
| `class="zoom-img"` | CSS hover zoom ეფექტი                  |

---

## ნაბიჯი 14 — სისტემური ანალიზი (`#status`)

```html
<section id="status" class="reveal">
    <h2>📊 სისტემური ანალიზი</h2>
    <div class="stat-grid">
        <div>
            ჟანგბადი:
            <span class="ready">აღდგენილი</span>
        </div>
        <div>
            კორპუსი:
            <span class="danger">დეფორმირებული</span>
        </div>
        <div>
            სემანტიკა:
            <span class="ready">ONLINE</span>
        </div>
        <div>
            ეკიპაჟი:
            <span class="ready">ACTIVE</span>
        </div>
    </div>
</section>
```

**კლასების მნიშვნელობა:**

| კლასი               | ფერი   | CSS                                              |
| ------------------- | ------ | ------------------------------------------------ |
| `class="stat-grid"` | —      | `display: grid; grid-template-columns: 1fr 1fr;` |
| `class="ready"`     | მწვანე | `color: var(--success) #39ff14`                  |
| `class="danger"`    | წითელი | `color: var(--danger) #ff003c`                   |

---

### ნაბიჯი 15 — ეკიპაჟი მონაცემები (ცხრილი)

```html
<section id="crew-manifest" class="reveal">
    <h2>👥 ეკიპაჟის მონაცემები</h2>
    <table class="crew-table">
        <thead>
            <tr>
                <th>სახელი</th>
                <th>პოზიცია</th>
                <th>სტატუსი</th>
                <th>კრიო-კაპსულა</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Semantic AI</td>
                <td>მთავარი ინტელექტი</td>
                <td><span class="ready">აქტიური</span></td>
                <td>-</td>
            </tr>
            <tr>
                <td>Flex Layout</td>
                <td>სტრუქტურული ინჟინერი</td>
                <td><span class="ready">აქტიური</span></td>
                <td>კრიო-1</td>
            </tr>
            <tr>
                <td>Grid Commander</td>
                <td>ნავიგაციის სპეციალისტი</td>
                <td><span class="ready">აქტიური</span></td>
                <td>კრიო-2</td>
            </tr>
            <tr>
                <td>Captain Stark</td>
                <td>მისიის უფროსი</td>
                <td><span class="danger">საფრთხის ქვეშ</span></td>
                <td>კრიო-0 (VIP)</td>
            </tr>
            <tr>
                <td>Dr. Quantum</td>
                <td>ფიზიკოსი</td>
                <td><span class="ready">აქტიური</span></td>
                <td>კრიო-3</td>
            </tr>
        </tbody>
    </table>
</section>
```

**ცხრილის ელემენტები:**

| ელემენტი                      | დანიშნულება        | CSS                                           |
| ----------------------------- | ------------------ | --------------------------------------------- |
| `<table class="crew-table">`  | ცხრილის კონტეინერი | border-collapse: collapse                     |
| `<thead>`                     | ჯამური სტრიქონი    | background: rgba(0, 210, 255, 0.1)            |
| `<th>`                        | სვეტის სათაური     | color: var(--neon); text-transform: uppercase |
| `<tbody>`                     | მონაცემის რიგები   | —                                             |
| `<tr>`                        | ცხრილის რიგი       | `:hover` background rgba(0, 210, 255, 0.05)   |
| `<td>`                        | ცხრილის უჯრა       | padding: 12px; border-bottom                  |
| `<span class="ready/danger">` | სტატუსის წერტილი   | მწვანე/წითალი ფერი                            |

### ნაბიჯი 16 — სისტემების აღდგენის ფორმა

```html
<section id="systems-report" class="reveal">
    <h2>🔧 სისტემების აღდგენის ფორმა</h2>
    <form id="repair-form" class="repair-form">
        <fieldset>
            <legend>სისტემის აღდგენის რეგისტრაცია</legend>

            <div class="form-group">
                <label for="system-name">სისტემის სახელი:</label>
                <select id="system-name" name="system" required>
                    <option value="">-- აირჩიეთ სისტემა --</option>
                    <option value="propulsion">მამოძრავებელი ძრავა</option>
                    <option value="shielding">დაცვის ველი</option>
                    <option value="comms">კავშირის სისტემა</option>
                    <option value="navigation">ნავიგაციური სისტემა</option>
                    <option value="life-support">სიცოცხლის მხარდამჭერი</option>
                </select>
            </div>

            <div class="form-group">
                <label for="damage-level">დაზიანების დონე:</label>
                <input
                    type="range"
                    id="damage-level"
                    name="damage"
                    min="0"
                    max="100"
                    value="50"
                />
                <span id="damage-display">50%</span>
            </div>

            <div class="form-group">
                <label for="priority">აღდგენის პრიორიტეტი:</label>
                <select id="priority" name="priority" required>
                    <option value="critical">კრიტიკული</option>
                    <option value="high">მაღალი</option>
                    <option value="medium">საშუალო</option>
                    <option value="low">დაბალი</option>
                </select>
            </div>

            <div class="form-group">
                <label for="tech-notes">ტექნიკური შენიშვნები:</label>
                <textarea
                    id="tech-notes"
                    name="notes"
                    rows="4"
                    placeholder="აღწერეთ პრობლემა..."
                ></textarea>
            </div>

            <div class="form-group checkbox-group">
                <label>
                    <input type="checkbox" name="auto-repair" />
                    ავტომატური აღდგენა
                </label>
                <label>
                    <input type="checkbox" name="backup-power" />
                    სარეზერვო ენერგია
                </label>
                <label>
                    <input type="checkbox" name="alert-crew" />
                    ეკიპაჟის გაფრთხილება
                </label>
            </div>

            <button type="submit" class="submit-btn">
                📤 აღდგენის დაწყება
            </button>
        </fieldset>
    </form>
</section>
```

**ფორმის ელემენტების დეტალი:**

| ელემენტი                  | ატრიბუტი             | დანიშნულება                                            |
| ------------------------- | -------------------- | ------------------------------------------------------ |
| `<form>`                  | `id="repair-form"`   | JavaScript აქ წვდება form submit-ის დასამუშავებლად     |
| `<fieldset>`              | —                    | ფორმის ელემენტების ჯგუფი (სემანტიკური)                 |
| `<legend>`                | —                    | fieldset-ის სათაური                                    |
| `<label>`                 | `for="system-name"`  | form element-ის ლეიბელი (accessibility)                |
| `<select>`                | `required`           | სავალდებულო ველი                                       |
| `<option>`                | `value="propulsion"` | dropdown ვარიანტი                                      |
| `<input type="range">`    | `min="0" max="100"`  | slider (0-100)                                         |
| `<textarea>`              | `rows="4"`           | მრავალხაზოვანი ტექსტი                                  |
| `<input type="checkbox">` | `name="auto-repair"` | JavaScript აქ წვდება `.checked` თვისებით               |
| `<button type="submit">`  | `class="submit-btn"` | ფორმის გაგზავნა (JavaScript აჰ слух form submit event) |

### ნაბიჯი 17 — ჰიპერ-ნახტომის დიაგნოსტიკა ფორმა

```html
<section id="jump-diagnostics" class="reveal">
    <h2>⚡ ჰიპერ-ნახტომის დიაგნოსტიკა</h2>
    <form id="jump-form" class="jump-form">
        <div class="form-group">
            <label for="distance">მანძილი დედამიწამდე (ღია წელი):</label>
            <input
                type="number"
                id="distance"
                name="distance"
                min="0"
                max="10000"
                value="5000"
                step="100"
            />
        </div>

        <div class="form-group">
            <label for="jump-time">ნახტომის დრო (წამი):</label>
            <input
                type="number"
                id="jump-time"
                name="time"
                min="1"
                max="3600"
                value="120"
            />
        </div>

        <div class="form-group">
            <label for="velocity">სიჩქარე (% სინათლის სიჩქარე):</label>
            <input
                type="number"
                id="velocity"
                name="velocity"
                min="0"
                max="999"
                value="85"
            />
        </div>

        <div class="form-group">
            <label>ნახტომის კატეგორია:</label>
            <div class="radio-group">
                <label>
                    <input type="radio" name="jump-type" value="warp" checked />
                    ვარპ-ნახტომი
                </label>
                <label>
                    <input type="radio" name="jump-type" value="hyperspace" />
                    ჰიპერსივრცე
                </label>
                <label>
                    <input type="radio" name="jump-type" value="quantum" />
                    კვანტური ნახტომი
                </label>
            </div>
        </div>

        <button type="submit" class="submit-btn">🚀 ნახტომის სიმულაცია</button>
    </form>

    <div id="jump-result" class="result-box hidden">
        <p><strong>სიმულაციის შედეგი:</strong></p>
        <p id="result-text"></p>
    </div>
</section>
```

**ელემენტების დეტალი:**

| ელემენტი                    | ატრიბუტი           | დანიშნულება                                                |
| --------------------------- | ------------------ | ---------------------------------------------------------- |
| `<input type="number">`     | `step="100"`       | increment 100-ით                                           |
| `<input type="radio">`      | `name="jump-type"` | ერთი რადიო ფიქსირდება                                      |
| `checked`                   | —                  | default selected radio                                     |
| `class="radio-group"`       | —                  | CSS flexbox გაკიდებული                                     |
| `class="result-box hidden"` | —                  | CSS `display: none` — JavaScript აჩვენებს submit-ის შემდეგ |
| `id="result-text"`          | —                  | JavaScript აქ ჩასვამს გამოთვლის შედეგს                     |

## ნაბიჯი 18 — გაშვების ზონა (ყველაზე მნიშვნელოვანი!)

```html
<section class="launch-zone reveal">
    <h3>🚀 ჰიპერ-ნახტომის ავტორიზაცია</h3>
    <p class="pulse-text">
        შეიყვანეთ
        <code>&lt;meta&gt;</code>
        კოორდინატები გადასარჩენად:
    </p>
    <input type="password" id="mission-code" placeholder="ACCESS CODE" />
    <br />
    <button type="button" id="launch-btn">INITIATE LAUNCH</button>
</section>
```

**_ ავტორიზაციისთვის ნებისმიერი კოდი მუშაობს _**

**ელემენტები:**

| ელემენტი                  | დანიშნულება                                             |
| ------------------------- | ------------------------------------------------------- |
| `<input type="password">` | კოდის შეყვანის ველი (სიმბოლოები იმალება)                |
| `id="mission-code"`       | JS ამ ველს კითხულობს                                    |
| `<button type="button">`  | ღილაკი — `type="button"` form submit-ს თავიდან აარიდებს |
| `id="launch-btn"`         | JS ამ ღილაკს ასმენს                                     |
| `class="pulse-text"`      | CSS pulse ანიმაცია                                      |

---

## ნაბიჯი 19 — დახურე `</main>` და დაამატე `<footer>`

```html
    </main>

    <footer>
      <p>S.S. SEMANTIC TERMINAL | DESIGNED BY 10X | 2026</p>
    </footer>

  </div><!-- /mission-control -->
```

---

## ნაბიჯი 20 — JS-ის მიბმა და დახურვა

```html
  <script src="script.js"></script>
</body>
</html>
```

> ⚠️ `<script>` ყოველთვის `</body>`-ის წინ — ჯერ HTML ჩაიტვირთოს, შემდეგ JS გაეშვას.

---

## ✅ მთლიანი სტრუქტურის სქემა

```
<html>
 ├── <head>          → CSS, charset, title
 └── <body>
      ├── .space-background   → ვარსკვლავიანი ფონი
      ├── #space-scene        → რაკეტა + დედამიწა
      ├── #mission-control    → მთავარი პანელი
      │    ├── <header>       → სათაური + nav
      │    ├── <audio>        → მუსიკა
      │    ├── <main>
      │    │    ├── #logs     → კაპიტნის ჟურნალი
      │    │    ├── #bridge   → დიალოგი
      │    │    ├── #visuals  → სურათი
      │    │    ├── #status   → სტატუსები
      │    │    └── .launch-zone → კოდი + ღილაკი
      │    └── <footer>       → ხელმოწერა
      └── <script>            → JS ფაილი
```

---

## 🎨 CSS-ის მიბმა — "WOW" ეფექტისთვის

HTML მარტო ჩონჩხია. ვიზუალური ეფექტებისთვის საჭიროა:

### `style.css` დაკავშირება:

## meta თეგში სათაურის ქვეშ ჩასვი ეს ლინკი

<link rel="stylesheet" href="style.css" />

### 🏁 საბოლოო შემოწმება

გახსენი `index.html` ბრაუზერში და შეამოწმე:

- [ ] გვერდი იხსნება მოძრავი ანიმაციური კოსმოსის სურათით
- [ ] კაპიტნის ჟურნალი ბეჭდვის ეფექტით იწერება
- [ ] ნავიგაციაში გვერდებზე გადართვისას სექციები ჩნდება
- [ ] კოდის შეყვანა და LAUNCH — ხომალდის გაშვება
- [ ] მუსიკა გაშვებისთანავე ირთვება

### მისია შესრულებულია. ეკიპაჟი სახლშია.🌍
