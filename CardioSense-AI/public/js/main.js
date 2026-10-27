
"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.querySelector(".menu-toggle");
    const navigation = document.querySelector(".nav-links");

    if (menuButton && navigation) {
        menuButton.addEventListener("click", () => {
            const isOpen = navigation.classList.toggle("open");
            menuButton.setAttribute("aria-expanded", String(isOpen));
        });

        navigation.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                navigation.classList.remove("open");
                menuButton.setAttribute("aria-expanded", "false");
            });
        });
    }

    const form = document.querySelector(".assessment-form");

    if (form) {
        form.addEventListener("reset", () => {
            window.setTimeout(() => {
                const error = form.querySelector(".alert-error");
                if (error) {
                    error.remove();
                }
            }, 0);
        });
    }
});
