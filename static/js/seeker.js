// Seeker-specific JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Job alert form
    const alertForm = document.querySelector('.alert-form');
    if (alertForm) {
        const keywordInput = alertForm.querySelector('input[name="keyword"]');
        const locationInput = alertForm.querySelector('input[name="location"]');
        
        // Suggest popular keywords
        if (keywordInput) {
            keywordInput.addEventListener('input', function() {
                // Could add AJAX call for suggestions here
            });
        }
        
        // Location autocomplete
        if (locationInput) {
            locationInput.addEventListener('input', function() {
                // Could add location autocomplete here
            });
        }
    }
    
    // Bookmark buttons
    document.querySelectorAll('.bookmark-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                e.preventDefault();
                fetch(e.target.href, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': e.target.dataset.csrf || '',
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    credentials: 'same-origin'
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'added') {
                        e.target.textContent = 'Remove Bookmark';
                        e.target.classList.add('btn-danger');
                        e.target.classList.remove('btn-secondary');
                    } else {
                        e.target.textContent = 'Save Job';
                        e.target.classList.add('btn-secondary');
                        e.target.classList.remove('btn-danger');
                    }
                });
            }
        });
    });
});