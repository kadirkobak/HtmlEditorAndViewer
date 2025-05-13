from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        html_code = request.form["html_code"]
    else:
        html_code = ""
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>HTML Editor & Preview</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    display: flex;
                    width: 95%;
                    height: 90%;
                    max-width: 1500px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                    overflow: hidden;
                    background-color: #fff;
                }
                .editor {
                    flex: 2;
                    padding: 20px;
                    border-right: 2px solid #ddd;
                    display: flex;
                    flex-direction: column;
                }
                .preview {
                    flex: 1;
                    padding: 20px;
                }
                textarea {
                    width: 100%;
                    height: 90%;
                    padding: 10px;
                    font-size: 14px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    font-family: 'Courier New', monospace;
                    background-color: #f9f9f9;
                    resize: none;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 12px 16px;
                    font-size: 16px;
                    border-radius: 4px;
                    cursor: pointer;
                    margin-top: 10px;
                    width: 100%;
                }
                button:hover {
                    background-color: #45a049;
                }
                .preview-box {
                    width: 100%;
                    height: 100%;
                    border: 1px solid #ddd;
                    padding: 10px;
                    box-sizing: border-box;
                    overflow: auto;
                }
                .preview-box iframe {
                    width: 100%;
                    height: 100%;
                    border: none;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <!-- Editor Section -->
                <div class="editor">
                    <h2>HTML Editor</h2>
                    <form method="POST">
                        <textarea name="html_code" placeholder="Write your HTML code here...">{{ html_code }}</textarea>
                        <button type="submit" id="previewButton">Preview</button>
                    </form>
                </div>

                <!-- Preview Section -->
                <div class="preview">
                    <h2>Preview</h2>
                    <div class="preview-box">
                        <iframe id="previewIframe"></iframe>
                    </div>
                </div>
            </div>

            <script>
                document.getElementById('previewButton').addEventListener('click', function(event) {
                    event.preventDefault(); // Prevents automatic form submission
                    const htmlCode = document.querySelector('textarea[name="html_code"]').value;
                    const iframe = document.getElementById('previewIframe');
                    iframe.srcdoc = htmlCode; // Updates iframe content
                });
            </script>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
