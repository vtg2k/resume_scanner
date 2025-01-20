from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    return jsonify({"message": "Resume uploaded successfully", "filename": file.filename})

if __name__ == '__main__':
    app.run(port=5000)