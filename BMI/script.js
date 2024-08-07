document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('bmi-form');
    const heightInput = document.getElementById('height');
    const weightInput = document.getElementById('weight');
    const bodyFatInput = document.getElementById('body-fat');
    const unitSelect = document.getElementById('unit');
    const bmiValueElement = document.getElementById('bmi-value');
    const bmiCategoryElement = document.getElementById('bmi-category');
    const resultElement = document.getElementById('result');
    const themeToggleButton = document.getElementById('theme-toggle');
    const saveProfileButton = document.getElementById('save-profile');
    const viewHistoryButton = document.getElementById('view-history');
    const scrollTopButton = document.getElementById('scroll-top');
    const helpButton = document.getElementById('help-button');
    const helpTooltip = document.getElementById('help-tooltip');
    const ctx = document.getElementById('bmi-chart').getContext('2d');

    let isDarkMode = false;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const height = parseFloat(heightInput.value);
        const weight = parseFloat(weightInput.value);
        const bodyFat = parseFloat(bodyFatInput.value) || 0;
        const unit = unitSelect.value;

        if (isNaN(height) || isNaN(weight) || height <= 0 || weight <= 0) {
            alert('Please enter valid positive numbers for height and weight.');
            return;
        }

        let heightInMeters;
        if (unit === 'imperial') {
            heightInMeters = (height * 0.0254);
        } else {
            heightInMeters = height / 100;
        }
        const bmi = weight / (heightInMeters * heightInMeters);

        bmiValueElement.textContent = `Your BMI is: ${bmi.toFixed(2)}`;
        let category = '';
        if (bmi < 18.5) {
            category = 'Underweight';
        } else if (bmi < 24.9) {
            category = 'Normal weight';
        } else if (bmi < 29.9) {
            category = 'Overweight';
        } else {
            category = 'Obesity';
        }
        bmiCategoryElement.textContent = `Category: ${category}`;
        resultElement.classList.add('visible');
    });

    themeToggleButton.addEventListener('click', function () {
        isDarkMode = !isDarkMode;
        document.body.classList.toggle('dark-mode', isDarkMode);
        themeToggleButton.textContent = isDarkMode ? 'Switch to Light Theme' : 'Switch to Dark Theme';
    });

    saveProfileButton.addEventListener('click', function () {
        const profile = {
            height: heightInput.value,
            weight: weightInput.value,
            bodyFat: bodyFatInput.value
        };
        localStorage.setItem('bmiProfile', JSON.stringify(profile));
        alert('Profile saved!');
    });

    viewHistoryButton.addEventListener('click', function () {
        const profile = JSON.parse(localStorage.getItem('bmiProfile'));
        if (profile) {
            alert(`Height: ${profile.height}, Weight: ${profile.weight}, Body Fat: ${profile.bodyFat}`);
        } else {
            alert('No profile found.');
        }
    });

    window.addEventListener('scroll', function () {
        if (window.scrollY > 100) {
            scrollTopButton.style.display = 'block';
        } else {
            scrollTopButton.style.display = 'none';
        }
    });

    scrollTopButton.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    helpButton.addEventListener('click', function () {
        helpTooltip.style.display = helpTooltip.style.display === 'none' ? 'block' : 'none';
    });

    const bmiChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [], // Populate with dates or times
            datasets: [{
                label: 'BMI Over Time',
                data: [], // Populate with BMI values
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: { beginAtZero: true },
                y: { beginAtZero: true }
            }
        }
    });

    document.querySelector('.container').classList.add('loaded');
    resultElement.classList.add('visible');
});
