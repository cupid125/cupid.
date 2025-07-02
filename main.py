from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file selected", 400
    file = request.files['file']
    if file.filename == '':
        return "No file name", 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "File uploaded successfully"

@app.route('/downloads/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

app.run(host='0.0.0.0', port=81)
