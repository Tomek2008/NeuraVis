document.addEventListener("DOMContentLoaded", () => {
    const navbar = document.querySelector("header");
    let lastScrollTop = 0;

    window.addEventListener("scroll", () => {
        let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll > lastScrollTop) {
            navbar.style.top = "-90px"; 
        } else {
            navbar.style.top = "0"; 
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; 
    });

    // Animacja pojawiania się nagłówków
    const animatedHeaders = document.querySelectorAll(".animate.shadowed");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, { threshold: 0.5 });

    animatedHeaders.forEach((header) => {
        observer.observe(header);
    });
});
