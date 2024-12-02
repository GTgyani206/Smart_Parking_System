import cv2


# Save the initial frame for ROI selection
def save_initial_frame(frame):
    cv2.imwrite("initial_frame.jpg", frame)


# Select parking spots by drawing rectangles on the frame
def select_parking_spots(frame):
    # Define your ROI manually for this example (replace with actual selection logic)
    # Format: x, y, width, height
    parking_spots = [
        [100, 150, 50, 100],
        [200, 250, 60, 120],
        [300, 350, 70, 140]
    ]

    for spot in parking_spots:
        x, y, w, h = spot
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle for available spots

    cv2.imshow("Selected Parking Spots", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
