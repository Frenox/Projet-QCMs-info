
document.addEventListener('DOMContentLoaded', function() {

    const fileInputs = document.querySelectorAll('.file-input');

    fileInputs.forEach(function(input) {
    input.addEventListener('change', function() {
        const fileDisplay = input.closest('.file').querySelector('.file-name');
        const fileName = input.files.length > 0 ? input.files[0].name : "Aucun fichier…";
        fileDisplay.textContent = fileName;
    });
    }); 
    
    const generateButton = document.getElementById('generateButton');
    const loadBar = document.getElementById('loadBar');
    if (generateButton) {
        generateButton.onclick = function() {
        loadBar.style.display = 'block';
        generateButton.className = 'button is-loading';
        };
    }

    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
    const $notification = $delete.parentNode;
    $delete.addEventListener('click', () => {
    $notification.parentNode.removeChild($notification);
    });
    });

});