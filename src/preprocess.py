import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Example: Denoising and skew correction
    denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)
    return denoised
