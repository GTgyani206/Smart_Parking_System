import cv2

# process_frame now takes 'drawRectangle' as an argument instead of importing it
def process_frame(frame, roi_data, low_threshold, high_threshold, min_pix, max_pix, drawRectangle):
    # Placeholder for processing
    processed_frame = frame.copy()

    for i in range(len(roi_data)):
        a, b, c, d = roi_data.iloc[i]
        processed_frame = drawRectangle(processed_frame, a, b, c, d, low_threshold, high_threshold, min_pix, max_pix)

    return processed_frame

def draw_parking_availability(frame, roi_data, low_threshold, high_threshold, min_pix, max_pix, drawRectangle):
    processed_frame = process_frame(frame, roi_data, low_threshold, high_threshold, min_pix, max_pix, drawRectangle)
    return processed_frame
