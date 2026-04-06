import cv2
import os

def compress_video(input_path, output_path, target_width=1920):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open {input_path}")
        return

    # Original properties
    orig_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    orig_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate target height to maintain aspect ratio
    ratio = target_width / orig_width
    target_height = int(orig_height * ratio)
    
    print(f"Resizing from {orig_width}x{orig_height} to {target_width}x{target_height} ({fps} FPS)")

    # Define codec and writer
    # Try 'mp4v' for .mp4 on Windows
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (target_width, target_height))

    processed = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Resize frame
        resized = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_AREA)
        out.write(resized)
        
        processed += 1
        if processed % 100 == 0:
            print(f"Processed {processed}/{frame_count} frames...", end='\r')

    cap.release()
    out.release()
    print(f"\nDone! Saved to {output_path}")
    print(f"New size: {os.path.getsize(output_path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    input_video = r"slides\assets\outputs\videos\solution-parking-occupancy.mp4"
    output_video = r"slides\assets\outputs\videos\solution-parking-occupancy-small.mp4"
    compress_video(input_video, output_video)
