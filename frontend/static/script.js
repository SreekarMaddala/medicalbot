document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('symptom-form');
    const spinner = document.getElementById('spinner');

    form.addEventListener('submit', () => {
        spinner.style.display = 'block';
    });
});

function saveAsPDF() {
    // Simple print to PDF functionality
    window.print();
}
