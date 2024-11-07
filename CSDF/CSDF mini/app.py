from flask import Flask, request, jsonify, render_template, send_from_directory
from forensics import extract_metadata, calculate_image_hash, error_level_analysis
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  


if not os.path.exists('uploads'):
    os.makedirs('uploads')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image = request.files['image']
    image_path = f"uploads/{image.filename}"
    image.save(image_path)

    
    metadata = extract_metadata(image_path)
    image_hash = calculate_image_hash(image_path)
    ela_image_path = error_level_analysis(image_path)

    return jsonify({
        "metadata": metadata,
        "hash": image_hash,
        "ela_image": f"http://127.0.0.1:5000/uploads/{os.path.basename(ela_image_path)}"
    })


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug=True)
