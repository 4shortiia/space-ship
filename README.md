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

გახსენი `index.html` და დაწერე დოკუმენტის სტრუქტურა.

```html
<!doctype html>
<html lang="ka"></html>
```

**რატომ?**  
`<!doctype html>` ეუბნება ბრაუზერს, რომ ეს HTML5 დოკუმენტია.  
`lang="ka"` — ენა ქართულია.

---

## ნაბიჯი 3 — `<head>` სექცია

`<html>` ტეგის შიგნით დაწერე `<head>`:

```html
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>S.S. Semantic | Final Approach</title>
    <link rel="stylesheet" href="style.css" />
</head>
```

**რა არის თითოეული?**

| ტეგი                         | დანიშნულება                     |
| ---------------------------- | ------------------------------- |
| `<meta charset="UTF-8">`     | ქართული ასოები სწორად გამოჩნდეს |
| `<meta name="viewport" ...>` | მობილურზე სწორი ზომა            |
| `<title>`                    | ბრაუზერის ჩანართზე სახელი       |
| `<link rel="stylesheet">`    | CSS ფაილის მიბმა                |

---

## ნაბიჯი 4 — `<body>` — ხომალდის სხეული

`</head>`-ის შემდეგ გახსენი `<body>`:

```html
<body></body>
```

`<body>`-ს შიგნით ყველა ხილული ელემენტი მოთავსდება.

---

## ნაბიჯი 5 — კოსმოსური ფონი

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

## ნაბიჯი 6 — კოსმოსური სცენა (რაკეტა და დედამიწა)

```html
<div id="space-scene">
    <div id="earth">🌍</div>
    <div id="rocket-container">
        <div id="rocket">🚀</div>
        <div id="fire"></div>
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

## ნაბიჯი 7 — მისიის კონტროლ-პანელი

ეს მთავარი `<div>`-ია, სადაც ყველაფერი ხდება:

```html
<div id="mission-control"></div>
```

`id="mission-control"` — JavaScript ამ div-ს მალავს გაშვების შემდეგ.

---

## ნაბიჯი 8 — `<header>` (სათაური)

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

## ნაბიჯი 9 — აუდიო ფაილი

`</header>`-ის შემდეგ:

```html
<audio id="space-music" src="assets/interstellar.mp3" loop></audio>
```

> ⚠️ შექმენი საქაღალდე `assets/` და ჩააგდე MP3 ფაილი სახელად `interstellar.mp3`.  
> `loop` ატრიბუტი — მუსიკა მარადიულად მეორდება.

---

## ნაბიჯი 10 — `<main>` სექცია

```html
<main></main>
```

`<main>` — სემანტიკური ტეგი, რომელიც გვერდის მთავარ კონტენტს შეიცავს.

---

## ნაბიჯი 11 — კაპიტნის ჟურნალი (`#logs`)

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

## ნაბიჯი 12 — ხომალდის ხიდი (`#bridge`)

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

## ნაბიჯი 13 — გარე ვიზუალიზაცია (`#visuals`)

```html
<section id="visuals" class="reveal">
    <h2>🔭 გარე ვიზუალიზაცია</h2>
    <div class="img-frame">
        <img
            src="https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=800"
            alt="Cosmos"
            class="zoom-img"
        />
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

**კლასები:**

| კლასი       | დანიშნულება                  |
| ----------- | ---------------------------- |
| `stat-grid` | CSS Grid — 2×2 ბადე          |
| `ready`     | მწვანე ფერი — სტატუსი კარგია |
| `danger`    | წითელი ფერი — საფრთხე        |

---

## ნაბიჯი 15 — გაშვების ზონა (ყველაზე მნიშვნელოვანი!)

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

**ელემენტები:**

| ელემენტი                  | დანიშნულება                                             |
| ------------------------- | ------------------------------------------------------- |
| `<input type="password">` | კოდის შეყვანის ველი (სიმბოლოები იმალება)                |
| `id="mission-code"`       | JS ამ ველს კითხულობს                                    |
| `<button type="button">`  | ღილაკი — `type="button"` form submit-ს თავიდან აარიდებს |
| `id="launch-btn"`         | JS ამ ღილაკს ასმენს                                     |
| `class="pulse-text"`      | CSS pulse ანიმაცია                                      |

---

## ნაბიჯი 16 — დახურე `</main>` და დაამატე `<footer>`

```html
    </main>

    <footer>
      <p>S.S. SEMANTIC TERMINAL | DESIGNED BY NORA | 2026</p>
    </footer>

  </div><!-- /mission-control -->
```

---

## ნაბიჯი 17 — JS-ის მიბმა და დახურვა

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

## 🎨 CSS და JS-ის მიბმა — "WOW" ეფექტისთვის

HTML მარტო ჩონჩხია. ვიზუალური ეფექტებისთვის საჭიროა:

### `style.css` — ჩასვი ეს:

```css
:root {
    --bg: #010208;
    --neon: #00d2ff;
    --bg-neon: #2298b3;
    --danger: #ff003c;
    --text: #e0e0e0;
    --success: #39ff14;
}

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100vh;
    color: var(--text);
    font-family: "Courier New", monospace; /* Space font */
    overflow-x: hidden;
    overflow-y: auto;
}

/* 🌌 ვარსკვლავების ეფექტი */
.space-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
    background: radial-gradient(circle at center, #050a1d 0%, #010208 100%);
    overflow: hidden;
}

.stars {
    position: absolute;
    width: 200%;
    height: 200%;
    top: -50%;
    left: -50%;
    background: transparent
        url("assets/nebula_stars_space_bright_glow_spiral_universe_galaxies_milky_way_4k_hd_space.jpg");
    background-size: 500px;
    background-repeat: no-repeat;
    background-position: center;
    background-size: 100% 100%;
    opacity: 0.2;
    z-index: 1;
    animation: starsRotate 180s linear infinite;
}

@keyframes starsRotate {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

/* Space scene*/
#space-scene {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 1000;
}

#earth {
    position: absolute;
    top: 15%;
    right: 15%;
    font-size: 150px;
    filter: drop-shadow(0 0 50px var(--neon));
    animation: float 4s ease-in-out infinite alternate;
}

@keyframes float {
    from {
        transform: translateY(0);
    }
    to {
        transform: translateY(-10px);
    }
}

#rocket-container {
    position: absolute;
    /* A rocket appears from the bottom left corner of the screen */
    bottom: -150px;
    left: -150px;
    z-index: 1001;
}

#rocket {
    font-size: 100px;
    transform: rotate(15deg);
    display: inline-block;
}

#fire {
    position: absolute;
    top: 80px;
    left: 40px;
    width: 30px;
    height: 100px;
    background: linear-gradient(to bottom, #fff, var(--neon), transparent);
    filter: blur(8px);
    transform: rotate(0deg);
    animation: engineFire 0.1s infinite alternate;
    z-index: -1;
}

@keyframes engineFire {
    to {
        transform: scaleY(1.5);
        opacity: 0.8;
    }
}

/* Rocket Flight Animation Towards Earth - 3-Stage Approach */
.flyToEarth {
    animation: finalApproach 7.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

@keyframes finalApproach {
    0% {
        transform: translate(0, 0) scale(1);
    } /* Offscreen */
    30% {
        transform: translate(25vw, -25vh) scale(1.1);
    } /* Enters the screen */
    60% {
        transform: translate(60vw, -55vh) scale(0.6);
    } /* Toward the Earth */
    100% {
        transform: translate(78vw, -70vh) scale(0.05);
        opacity: 0;
    } /* Touch and disappear */
}

code {
    color: var(--neon);
    background: rgba(0, 210, 255, 0.1);
    padding: 2px 4px;
}

/* Control panel */
#mission-control {
    position: relative;
    max-width: 850px;
    margin: 60px auto;
    background: rgba(0, 15, 40, 0.9);
    border: 2px solid var(--neon);
    padding: 50px;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 50px rgba(0, 210, 255, 0.3);
    z-index: 10;
}

/* Sections appear */
.reveal {
    animation: slideUp 1.2s ease-out forwards;
    opacity: 0;
}

@keyframes slideUp {
    from {
        transform: translateY(50px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

header {
    text-align: center;
    border-bottom: 2px solid var(--neon);
    padding-bottom: 20px;
}
.glitch-text {
    color: #fff;
    text-shadow: 0 0 10px var(--neon);
}
.alert-blink {
    color: var(--danger);
    animation: alert 0.6s infinite;
    font-weight: bold;
}
@keyframes alert {
    50% {
        opacity: 0.2;
    }
}

nav ul {
    display: flex;
    justify-content: center;
    gap: 20px;
    list-style: none;
    padding: 15px 0;
    margin: 0;
}
nav a {
    color: var(--neon);
    text-decoration: none;
    font-weight: bold;
    font-size: 0.85rem;
    text-transform: uppercase;
}
nav a:hover {
    text-shadow: 0 0 10px var(--neon);
}

section {
    background: rgba(255, 255, 255, 0.03);
    padding: 30px;
    margin-top: 30px;
    border-radius: 4px;
    border-left: 4px solid var(--neon);
}
h2 {
    color: var(--neon);
    text-transform: uppercase;
    font-size: 1.2rem;
    margin-top: 0;
    letter-spacing: 1px;
}

/* Copy the text of the captain's log (from the image) */
.typing-container {
    background: rgba(0, 0, 0, 0.3);
    padding: 15px;
    border-radius: 4px;
    border: 1px solid rgba(0, 210, 255, 0.2);
    box-shadow: inset 0 0 10px rgba(0, 210, 255, 0.1);
}

.typing-text {
    /* Neon text */
    color: var(--neon);
    text-shadow:
        0 0 5px var(--bg-neon),
        0 0 2px #fff;
    font-size: 1.05rem;
    line-height: 1.5;
    font-weight: bold;
    border-right: 2px solid var(--neon); /* Print cursor */
    white-space: normal;
    overflow: hidden;
    animation: blink-caret 0.75s step-end infinite;
}

@keyframes blink-caret {
    50% {
        border-color: transparent;
    }
}

.zoom-img {
    width: 100%;
    max-width: 500px;
    display: block;
    margin: 15px auto;
    border-radius: 4px;
    border: 1px solid rgba(0, 210, 255, 0.3);
    transition: 1s;
}
.zoom-img:hover {
    transform: scale(1.02);
}

.stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    text-align: center;
}
.danger {
    color: var(--danger);
    font-weight: bold;
}
.ready {
    color: var(--success);
    font-weight: bold;
}

.launch-zone {
    text-align: center;
    border: 1px dashed var(--neon);
    margin-top: 40px;
    padding: 30px;
}
.pulse-text {
    animation: pulse 1s infinite;
    color: var(--success);
}
@keyframes pulse {
    50% {
        opacity: 0.3;
    }
}
input {
    padding: 12px;
    background: #000;
    border: 1px solid var(--neon);
    color: white;
    width: 220px;
    text-align: center;
    font-family: inherit;
}
button {
    padding: 12px 40px;
    background: var(--neon);
    border: none;
    font-weight: bold;
    cursor: pointer;
    text-transform: uppercase;
    margin-top: 15px;
    transition: 0.3s;
}
button:hover {
    background: #fff;
    color: #000;
    box-shadow: 0 0 20px #fff;
}

.hyper-jump {
    animation: vanishes 1.4s cubic-bezier(0.6, -0.28, 0.735, 0.045) forwards;
}

@keyframes vanishes {
    100% {
        transform: scale(0.1) rotate(10deg);
        filter: blur(50px);
        opacity: 0;
    }
}

footer {
    text-align: center;
    opacity: 0.3;
    padding: 40px 0;
    font-size: 0.8rem;
}



---
```

### `script.js` — ჩასვი ეს:

```JS

const launchBtn = document.getElementById("launch-btn");
const site = document.getElementById("mission-control");
const spaceScene = document.getElementById("space-scene");
const rocketContainer = document.getElementById("rocket-container");
const codeInput = document.getElementById("mission-code");
const captainLog = document.getElementById("captain-log");
const music = document.getElementById("space-music");

music.volume = 0.3;

function typeWriter(text, element, speed) {
    let i = 0;
    element.innerHTML = "";
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    type();
}

window.addEventListener("load", () => {
    const fullText = captainLog.innerText;
    typeWriter(fullText, captainLog, 50);
});

launchBtn.addEventListener("click", function () {
    if (codeInput.value.trim() !== "") {
        // 🎵 მუსიკა პირდაპირ user gesture-ის კონტექსტში ირთვება
        music.play().catch((error) => console.log("აუდიო ვერ გაეშვა:", error));

        // 🔊 ხმის აწევა
        let vol = music.volume;
        let fadeIn = setInterval(() => {
            if (vol < 0.9) {
                vol = Math.min(vol + 0.05, 0.9);
                music.volume = vol;
            } else {
                clearInterval(fadeIn);
            }
        }, 100);

        site.classList.add("hyper-jump");
        setTimeout(() => {
            site.style.display = "none";
            spaceScene.style.display = "block";
            rocketContainer.classList.add("flyToEarth");
        }, 2500);

        // 9 წამიანი ფრენა და დასრულება
        setTimeout(() => {
            let volOut = music.volume;
            let fadeOut = setInterval(() => {
                if (volOut > 0.05) {
                    volOut = Math.max(volOut - 0.05, 0.05);
                    music.volume = volOut;
                } else {
                    music.pause();
                    clearInterval(fadeOut);
                }
            }, 200);

            alert("მისია წარმატებით დასრულდა! ეკიპაჟი უსაფრთხოდ არის. 🌍");
            location.reload();
        }, 12000);
    } else {
        alert("შეიყვანეთ კოდი!");
    }
});


---
```

### 🏁 საბოლოო შემოწმება

გახსენი `index.html` ბრაუზერში და შეამოწმე:

- [ ] გვერდი შავ ფონზე იხსნება ვარსკვლავებით
- [ ] კაპიტნის ჟურნალი ბეჭდვის ეფექტით იწერება
- [ ] გვერდის გადახვევისას სექციები გამოჩნდება
- [ ] კოდის შეყვანა და LAUNCH — რაკეტა გაფრინდება
- [ ] მუსიკა გაშვებისთანავე ირთვება

### მისია შესრულებულია. ეკიპაჟი სახლშია.🌍
