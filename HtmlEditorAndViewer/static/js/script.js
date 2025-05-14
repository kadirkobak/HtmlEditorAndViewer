document.getElementById('previewButton').addEventListener('click', function (event) {
    event.preventDefault(); 
    const htmlCode = document.querySelector('textarea[name="html_code"]').value;
    const iframe = document.getElementById('previewIframe');
    iframe.srcdoc = htmlCode;
});
