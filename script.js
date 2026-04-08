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
