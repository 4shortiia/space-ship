const launchBtn = document.getElementById("launch-btn");
const site = document.getElementById("mission-control");
const spaceScene = document.getElementById("space-scene");
const rocketContainer = document.getElementById("rocket-container");
const codeInput = document.getElementById("mission-code");
const captainLog = document.getElementById("captain-log");
const music = document.getElementById("space-music");

// Damage range display
const damageLevel = document.getElementById("damage-level");
const damageDisplay = document.getElementById("damage-display");

if (damageLevel) {
    damageLevel.addEventListener("input", (e) => {
        damageDisplay.textContent = e.target.value + "%";
        if (e.target.value > 75) {
            damageDisplay.style.color = "var(--danger)";
        } else if (e.target.value > 50) {
            damageDisplay.style.color = "var(--bg-neon)";
        } else {
            damageDisplay.style.color = "var(--success)";
        }
    });
}

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

// Repair Form Handler
const repairForm = document.getElementById("repair-form");
if (repairForm) {
    repairForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const system = document.getElementById("system-name").value;
        const damage = document.getElementById("damage-level").value;
        const priority = document.getElementById("priority").value;
        const notes = document.getElementById("tech-notes").value;

        if (!system) {
            alert("⚠️ აირჩიეთ სისტემა!");
            return;
        }

        const autoRepair = document.querySelector(
            'input[name="auto-repair"]',
        ).checked;
        const backupPower = document.querySelector(
            'input[name="backup-power"]',
        ).checked;
        const alertCrew = document.querySelector(
            'input[name="alert-crew"]',
        ).checked;

        let message = `🔧 აღდგენის რეგისტრაცია:\n\n`;
        message += `სისტემა: ${system}\n`;
        message += `დაზიანება: ${damage}%\n`;
        message += `პრიორიტეტი: ${priority}\n`;
        if (notes) message += `შენიშვნები: ${notes}\n`;
        message += `\nფუნქციები:\n`;
        if (autoRepair) message += `✓ ავტომატური აღდგენა\n`;
        if (backupPower) message += `✓ სარეზერვო ენერგია\n`;
        if (alertCrew) message += `✓ ეკიპაჟის გაფრთხოვება\n`;

        alert(message + `\n✅ აღდგენა დაწყებულია!`);
        repairForm.reset();
        damageDisplay.textContent = "50%";
    });
}

// Jump Diagnostics Form Handler
const jumpForm = document.getElementById("jump-form");
const jumpResult = document.getElementById("jump-result");
const resultText = document.getElementById("result-text");

if (jumpForm) {
    jumpForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const distance = parseFloat(document.getElementById("distance").value);
        const time = parseFloat(document.getElementById("jump-time").value);
        const velocity = parseFloat(document.getElementById("velocity").value);
        const jumpType = document.querySelector(
            'input[name="jump-type"]:checked',
        ).value;

        // Simulate jump calculations
        const calcVelocity = (distance / time) * 100;
        const status =
            velocity >= 90
                ? "✅ უსაფრთხო"
                : velocity >= 70
                  ? "⚠️ ზოგი რისკი"
                  : "🔴 საშიში";
        const estimatedTime = ((distance / velocity) * 100).toFixed(2);
        const jumpNames = {
            warp: "ვარპ-ნახტომი",
            hyperspace: "ჰიპერსივრცეს გადახტება",
            quantum: "კვანტური გადასახტება",
        };

        resultText.innerHTML = `
            <strong>${jumpNames[jumpType]}</strong><br/>
            მანძილი: ${distance} ღია წელი<br/>
            სიჩქარე: ${velocity}% (გამოთვლილი: ${calcVelocity.toFixed(0)}%)<br/>
            სტატუსი: ${status}<br/>
            სავარაუდო დრო: ${estimatedTime} წამი
        `;

        jumpResult.classList.remove("hidden");
    });
}

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

            alert(
                "✅ მისია წარმატებით დასრულდა! ეკიპაჟი უსაფრთხოდ დედამიწაზე არის. 🌍",
            );
            location.reload();
        }, 12000);
    } else {
        alert("⚠️ შეიყვანეთ კოდი!");
    }
});
