document.addEventListener("DOMContentLoaded", () => {
    // Navbar scroll hide/show
    const navbar = document.querySelector("header");
    let lastScrollTop = 0;

    window.addEventListener("scroll", () => {
        let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        // If scrolling down, hide the navbar, otherwise show it
        if (currentScroll > lastScrollTop) {
            navbar.style.top = "-90px"; // Hide navbar when scrolling down
        } else {
            navbar.style.top = "0"; // Show navbar when scrolling up
        }

        // Update lastScrollTop value
        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; 
    });

    // Intersection Observer for header animation (fade-in effect)
    const animatedHeaders = document.querySelectorAll(".animate.shadowed");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible"); // Add class when header is visible
            }
        });
    }, { threshold: 0.5 }); // Trigger when 50% of the header is visible

    animatedHeaders.forEach((header) => {
        observer.observe(header); // Observe each header
    });
});

