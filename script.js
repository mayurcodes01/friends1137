function animateShayari(text) {
    const box = document.querySelector(".shayari-box");
    if (!box) return;

    // Reset box
    box.innerHTML = "";
    box.style.opacity = 0;
    box.style.transform = "translateY(15px)";
    box.style.boxShadow = "0 0 0 rgba(255,75,125,0)";

    // Fade + slide in
    setTimeout(() => {
        box.style.transition = "all 0.6s ease";
        box.style.opacity = 1;
        box.style.transform = "translateY(0)";
        box.style.boxShadow = "0 0 20px rgba(255,75,125,0.6)";
    }, 100);

    // Typewriter effect
    let i = 0;
    const speed = 35;

    function typeWriter() {
        if (i < text.length) {
            box.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        } else {
            pulseGlow();
        }
    }

    setTimeout(typeWriter, 300);
}

// Soft glowing pulse after typing finishes
function pulseGlow() {
    const box = document.querySelector(".shayari-box");
    if (!box) return;

    box.animate(
        [
            { boxShadow: "0 0 15px rgba(255,75,125,0.4)" },
            { boxShadow: "0 0 30px rgba(255,75,125,0.8)" },
            { boxShadow: "0 0 15px rgba(255,75,125,0.4)" }
        ],
        {
            duration: 1800,
            iterations: 2
        }
    );
}
