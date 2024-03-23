
document.addEventListener('DOMContentLoaded', function() {

    const fileInputs = document.querySelectorAll('.file-input');

    fileInputs.forEach(function(input) {
    input.addEventListener('change', function() {
        const fileDisplay = input.closest('.file').querySelector('.file-name');
        if (input.files.length > 0) {
            const fileName = input.files[0].name
            generateButton.removeAttribute('disabled');
            fileDisplay.textContent = fileName;
        }
        else {
            generateButton.setAttribute('disabled');
            const fileName = 'Aucun fichier...';
            fileDisplay.textContent = fileName;
        }
        
    });
    }); 
    
    const generateButton = document.getElementById('generateButton');
    const loadBar = document.getElementById('loadBar');
    if (generateButton) {
        generateButton.onclick = function() {
        loadBar.style.display = 'block';
        generateButton.className = 'button is-primary is-loading';
        };
    }

    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
    const $notification = $delete.parentNode;
    $delete.addEventListener('click', () => {
    $notification.parentNode.removeChild($notification);
    });
    });
});
