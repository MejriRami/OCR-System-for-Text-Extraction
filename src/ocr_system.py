import cv2
from preprocess import preprocess_image
from cnn_model import TextDetectionCNN
from crnn_model import CRNN

def ocr_pipeline(image_path):
    # Preprocess the image
    image = preprocess_image(image_path)

    # Initialize models
    cnn_model = TextDetectionCNN()
    crnn_model = CRNN()

    # Detect text boxes (this is a placeholder, you'll need to implement it)
    text_boxes = cnn_model.detect_text(image)

    # Recognize text from the detected boxes
    extracted_text = []
    for box in text_boxes:
        text = crnn_model.recognize_text(image[box[0]:box[1], box[2]:box[3]])
        extracted_text.append(text)

    return extracted_text

if __name__ == "__main__":
    image_path = "data/example_image.png"
    result = ocr_pipeline(image_path)
    print("Extracted Text:", result)
