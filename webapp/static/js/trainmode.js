// trainmode.js

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

// Text Animation
document.addEventListener('DOMContentLoaded', () => {
    const quoteText = document.querySelector('.quote-text');
    const trackButton = document.querySelector('.trackbutton');
    const travelButton = document.querySelector('.travelbutton');
    
    // Quote Text Animation
    quoteText.style.opacity = 0;
    quoteText.style.transform = 'translateY(-50px)';
    setTimeout(() => {
        quoteText.style.transition = 'opacity 1s, transform 1s';
        quoteText.style.opacity = 1;
        quoteText.style.transform = 'translateY(0)';
    }, 500);

    // Track Button Animation
    trackButton.style.opacity = 0;
    trackButton.style.transform = 'translateY(-50px)';
    setTimeout(() => {
        trackButton.style.transition = 'opacity 1s, transform 1s';
        trackButton.style.opacity = 1;
        trackButton.style.transform = 'translateY(0)';
    }, 1000);

    // Travel Button Animation
    travelButton.style.opacity = 0;
    travelButton.style.transform = 'translateY(-50px)';
    setTimeout(() => {
        travelButton.style.transition = 'opacity 1s, transform 1s';
        travelButton.style.opacity = 1;
        travelButton.style.transform = 'translateY(0)';
    }, 1500);
});

// Button Click Animation
document.querySelectorAll('.trackbutton, .travelbutton').forEach(button => {
    button.addEventListener('click', function() {
        this.classList.add('clicked');
        setTimeout(() => this.classList.remove('clicked'), 300);
    });
});
