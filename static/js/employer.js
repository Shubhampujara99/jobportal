// Employer-specific JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Job posting form enhancements
    const jobForm = document.querySelector('.job-form');
    if (jobForm) {
        const descriptionField = jobForm.querySelector('textarea[name="description"]');
        const requirementsField = jobForm.querySelector('textarea[name="requirements"]');
        
        if (descriptionField && requirementsField) {
            // Add character counters
            function setupCounter(field, maxLength) {
                const counter = document.createElement('div');
                counter.className = 'char-counter';
                field.parentNode.appendChild(counter);
                
                function updateCounter() {
                    const remaining = maxLength - field.value.length;
                    counter.textContent = `${remaining} characters remaining`;
                    counter.style.color = remaining < 50 ? 'red' : '#666';
                }
                
                field.addEventListener('input', updateCounter);
                updateCounter();
            }
            
            setupCounter(descriptionField, 2000);
            setupCounter(requirementsField, 1000);
        }
    }
});