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
            <style>
                body { font-family: Arial, sans-serif; display: flex; }
                .container { display: flex; width: 100%; }
                .editor { width: 50%; padding: 10px; border-right: 2px solid #ccc; }
                .preview { width: 50%; padding: 10px; }
                textarea { width: 100%; height: 100%; border: none; padding: 10px; font-family: monospace; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="editor">
                    <h3>HTML Editor</h3>
                    <form method="POST">
                        <textarea name="html_code" placeholder="HTML kodunuzu buraya yazın...">{{ html_code }}</textarea>
                        <button type="submit" style="display: none;"></button>
                    </form>
                </div>
                <div class="preview">
                    <h3>Preview</h3>
                    <div style="border: 1px solid #ccc; padding: 10px;">
                        {{ html_code|safe }}
                    </div>
                </div>
            </div>
        </body>
        </html>
    """, html_code=html_code)

if __name__ == "__main__":
    app.run(debug=True)

