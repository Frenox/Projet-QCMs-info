
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
    const result = document.getElementById('result');
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

    $(document).ready(function() {
        $('#qcmForm').submit(function(event) {
            event.preventDefault();
            var formData = new FormData(this);
            $.ajax({
                type: 'POST',
                url: '/process_qcm',
                data: formData,
                processData: false,
                contentType: false,
                dataType: 'json',
                success: function(response) {
                    $('#resultGrid').html(response.result);
                    loadBar.style.display = 'none';
                    result.style.display = 'block';
                    generateButton.className = 'button is-primary';
                },
                error: function(error) {
                    console.log('Error:', error);
                }
            });
        });
    });
});
