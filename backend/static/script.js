document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('symptom-form');
    const input = document.getElementById('symptoms');
    const spinner = document.getElementById('spinner');
    const datalist = document.getElementById('symptom-list');

    // Form validation
    form.addEventListener('submit', (e) => {
        const symptoms = input.value.trim();
        if (!symptoms) {
            e.preventDefault();
            showError('Please enter at least one symptom.');
            return;
        }
        // Check for invalid characters (allow letters, commas, spaces)
        if (!/^[a-zA-Z\s,]+$/.test(symptoms)) {
            e.preventDefault();
            showError('Symptoms should only contain letters, commas, and spaces.');
            return;
        }
        spinner.style.display = 'block';
        clearError();
    });

    // Autocomplete enhancement: filter datalist options based on input
    input.addEventListener('input', () => {
        const value = input.value.toLowerCase();
        const options = datalist.querySelectorAll('option');
        options.forEach(option => {
            const text = option.value.toLowerCase();
            option.style.display = text.includes(value) ? 'block' : 'none';
        });
    });

    function showError(message) {
        let errorDiv = document.querySelector('.error');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'error';
            form.appendChild(errorDiv);
        }
        errorDiv.innerHTML = `<i class="fas fa-exclamation-triangle"></i> ${message}`;
    }

    function clearError() {
        const errorDiv = document.querySelector('.error');
        if (errorDiv) {
            errorDiv.remove();
        }
    }
});

function saveAsPDF() {
    // Simple print to PDF functionality
    window.print();
}
