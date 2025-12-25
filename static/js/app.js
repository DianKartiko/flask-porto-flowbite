// 1. Inisialisasi Icons
lucide.createIcons();

// 2. Logic Mobile Menu (Sama seperti sebelumnya)
const btn = document.getElementById("mobile-menu-btn");
const menu = document.getElementById("mobile-menu");
const iconMenu = document.getElementById("icon-menu");
const iconClose = document.getElementById("icon-close");
const mobileLinks = document.querySelectorAll(".mobile-link-item");
let isOpen = false;

btn.addEventListener("click", () => {
    isOpen = !isOpen;
    if (isOpen) {
        menu.classList.remove("max-h-0", "opacity-0");
        menu.classList.add("max-h-screen", "opacity-100");
        iconMenu.classList.add("hidden");
        iconClose.classList.remove("hidden");
        mobileLinks.forEach((link, index) => {
            setTimeout(() => {
                link.classList.remove("translate-y-4", "opacity-0");
                link.classList.add("translate-y-0", "opacity-100");
            }, index * 50);
        });
    } else {
        menu.classList.remove("max-h-screen", "opacity-100");
        menu.classList.add("max-h-0", "opacity-0");
        iconMenu.classList.remove("hidden");
        iconClose.classList.add("hidden");
        mobileLinks.forEach((link) => {
            link.classList.remove("translate-y-0", "opacity-100");
            link.classList.add("translate-y-4", "opacity-0");
        });
    }
});

// 3. Logic Dark Mode Toggle
const themeToggleBtn = document.getElementById("theme-toggle");
const htmlElement = document.documentElement;

// Cek LocalStorage atau Preferensi Sistem saat load
if (
    localStorage.getItem("theme") === "dark" ||
    (!("theme" in localStorage) &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
    htmlElement.classList.add("dark");
} else {
    htmlElement.classList.remove("dark");
}

// Event Listener Click Toggle
themeToggleBtn.addEventListener("click", () => {
    if (htmlElement.classList.contains("dark")) {
        htmlElement.classList.remove("dark");
        localStorage.setItem("theme", "light");
    } else {
        htmlElement.classList.add("dark");
        localStorage.setItem("theme", "dark");
    }
});
