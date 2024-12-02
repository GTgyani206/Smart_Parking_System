import cv2
import pandas as pd
from scripts.selector import save_initial_frame, select_parking_spots
from scripts.detector import process_frame
from scripts.utils import load_parking_spots, drawRectangle


def main():
    # Set the path to the video file and the CSV file containing parking spot locations
    video_path = './data/lot.mp4'  # Update this with the correct video file path
    roi_file = './roi_data.csv'  # Update this with the correct CSV file path

    # Load the parking spot regions of interest (ROI) from the CSV file
    roi_data = load_parking_spots(roi_file)

    # Open the video capture
    cap = cv2.VideoCapture(video_path)

    # Process the first frame and save it as the initial frame for ROI selection
    ret, frame = cap.read()
    if not ret:
        print("Failed to read video")
        return

    save_initial_frame(frame)

    # Select parking spots from the frame
    select_parking_spots(frame)

    # Set the threshold values for parking spot detection
    low_threshold = 100
    high_threshold = 255
    min_pix = 200
    max_pix = 5000

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame to detect parking spot availability
        processed_frame = process_frame(frame, roi_data, low_threshold, high_threshold, min_pix, max_pix)

        # Display the processed frame
        cv2.imshow("Parking Spot Detection", processed_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
