// Main JavaScript for the site
document.addEventListener('DOMContentLoaded', function() {
    // Flash message fade out
    const messages = document.querySelectorAll('.alert');
    if (messages.length > 0) {
        setTimeout(() => {
            messages.forEach(msg => {
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 500);
            });
        }, 5000);
    }

    // Form validation enhancements
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Processing...';
            }
        });
    });
});