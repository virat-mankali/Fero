document.addEventListener('DOMContentLoaded', () => {
    // Initialize Flatpickr
    flatpickr("#day", {
        dateFormat: "Y-m-d",
        altInput: true,
        altFormat: "F j, Y",
        allowInput: true,
        placeholder: "Date"
    });

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Input Focus Effect
    const inputs = document.querySelectorAll('.frombox, .tobox, .date');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.style.boxShadow = '0 0 5px 2px rgba(255, 157, 0, 0.5)';
        });
        input.addEventListener('blur', () => {
            input.style.boxShadow = 'none';
        });
    });

    // Button Click Effect
    const searchButton = document.querySelector('.search');
    searchButton.addEventListener('click', () => {
        searchButton.classList.add('clicked');
        setTimeout(() => {
            searchButton.classList.remove('clicked');
        }, 300);
    });

    // Real-time validation and suggestions (example using static data)
    const fromBox = document.querySelector('.frombox');
    const toBox = document.querySelector('.tobox');

    fromBox.addEventListener('input', () => {
        const suggestions = ['Station A', 'Station B', 'Station C'];
        const datalist = document.getElementById('from-list');
        datalist.innerHTML = '';
        suggestions.forEach(suggestion => {
            if (suggestion.toLowerCase().includes(fromBox.value.toLowerCase())) {
                const option = document.createElement('option');
                option.value = suggestion;
                datalist.appendChild(option);
            }
        });
    });

    toBox.addEventListener('input', () => {
        const suggestions = ['Station D', 'Station E', 'Station F'];
        const datalist = document.getElementById('to-list');
        datalist.innerHTML = '';
        suggestions.forEach(suggestion => {
            if (suggestion.toLowerCase().includes(toBox.value.toLowerCase())) {
                const option = document.createElement('option');
                option.value = suggestion;
                datalist.appendChild(option);
            }
        });
    });
});
