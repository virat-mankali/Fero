// main.js

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Navbar Scroll Effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Button Animation
document.querySelectorAll('.buttons button').forEach(button => {
    button.addEventListener('click', function() {
        this.classList.add('clicked');
        setTimeout(() => this.classList.remove('clicked'), 300);
    });
});

// Text Animation
const text = document.querySelector('.quotemain h1');
text.innerHTML = text.textContent.replace(/\S/g, "<span>$&</span>");
const letters = document.querySelectorAll('.quotemain h1 span');
letters.forEach((letter, i) => {
    setTimeout(() => {
        letter.classList.add('fade');
    }, i * 50);
});
