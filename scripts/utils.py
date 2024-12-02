import cv2
import pandas as pd

def preprocess_image(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    return blurred_image

# Drawing a rectangle on the image with improvements
def drawRectangle(image, a, b, c, d, low_threshold, high_threshold, min_pix, max_pix):
    a, b, c, d = int(a), int(b), int(c), int(d)  # Ensure that coordinates are integers

    # Cropping the sub-image based on rectangle coordinates
    sub_image = image[b:b + d, a:a + c]

    # Preprocess the sub-image before thresholding
    preprocessed_sub_image = preprocess_image(sub_image)

    # Thresholding the sub-image
    _, thresh = cv2.threshold(preprocessed_sub_image, low_threshold, high_threshold, cv2.THRESH_BINARY)

    # Count the white pixels
    white_pixels = cv2.countNonZero(thresh)

    if white_pixels < min_pix:
        color = (0, 255, 0)  # Green for available spots
    elif white_pixels > max_pix:
        color = (0, 0, 255)  # Red for occupied spots
    else:
        color = (0, 255, 255)  # Yellow for uncertain spots

    # Drawing a rectangle on the original image
    cv2.rectangle(image, (a, b), (a + c, b + d), color, 2)

    return image


# Load parking spots from CSV file
def load_parking_spots(roi_file):
    roi_data = pd.read_csv(roi_file)
    return roi_data
