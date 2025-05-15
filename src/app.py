from flask import Flask , request , jsonify
from flask_cors import CORS
from pytesseract import Image


app =Flask(__name__)
CORS(app)

@app.route('/ocr', methods=['POST'])
def ocr_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    img=Image.open(file)
    text=pytesseract.image_to_string(img)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)