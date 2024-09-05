// landingpage.js

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

// Welcome Text Animation
document.addEventListener('DOMContentLoaded', () => {
    const welcomeText = document.querySelector('.welcometext1');
    const nameSpan = document.querySelector('.welcometext');
    const quoteText = document.querySelector('.quotel1');
    const startJourneyButton = document.querySelector('.startjourney');
    
    // Welcome Text Animation
    welcomeText.style.opacity = 0;
    welcomeText.style.transform = 'translateY(-50px)';
    setTimeout(() => {
        welcomeText.style.transition = 'opacity 1s, transform 1s';
        welcomeText.style.opacity = 1;
        welcomeText.style.transform = 'translateY(0)';
    }, 500);

    // Name Span Color Change
    nameSpan.style.color = 'rgb(255, 255, 255)';
    setTimeout(() => {
        nameSpan.style.transition = 'color 1s';
        nameSpan.style.color = 'rgb(140, 255, 0)';
    }, 1500);

    // Quote Text Animation
    quoteText.style.opacity = 0;
    quoteText.style.transform = 'translateY(-50px)';
    setTimeout(() => {
        quoteText.style.transition = 'opacity 1s, transform 1s';
        quoteText.style.opacity = 1;
        quoteText.style.transform = 'translateY(0)';
    }, 1000);

    // Start Journey Button Animation
    startJourneyButton.style.opacity = 0;
    startJourneyButton.style.transform = 'translateY(-50px)';
    setTimeout(() => {
        startJourneyButton.style.transition = 'opacity 1s, transform 1s';
        startJourneyButton.style.opacity = 1;
        startJourneyButton.style.transform = 'translateY(0)';
    }, 1500);
});

// Button Click Animation
document.querySelector('.startjourney').addEventListener('click', function() {
    this.classList.add('clicked');
    setTimeout(() => this.classList.remove('clicked'), 300);
});
