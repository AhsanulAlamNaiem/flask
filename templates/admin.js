function formatText(command, value = null) {
    document.execCommand(command, false, value);
}

document.getElementById('image-upload-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const imagePreview = document.getElementById('image-preview');
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Image Preview" style="max-width: 100%;">`;
        };
        reader.readAsDataURL(file);
    }
});
