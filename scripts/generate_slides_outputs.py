#!/usr/bin/env python3
"""
Generate YOLO output screenshots/videos for slides embedding.
Run this script to generate all visual outputs needed for the presentation.
"""

import os
import cv2
import json
import numpy as np
from ultralytics import YOLO, solutions


# Global Settings
OUTPUT_ROOT = "assets/slides/outputs"
VIDEO_DIR = os.path.join(OUTPUT_ROOT, "videos")
IMAGE_DIR = os.path.join(OUTPUT_ROOT, "images")

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)


def save_screenshot(result, filename):
    """Save YOLO result as screenshot in images directory."""
    path = os.path.join(IMAGE_DIR, filename)
    result.save(filename=path)
    print(f"Saved Image: {filename}")


# =============================================================================
# PART 1: TASK OUTPUTS (PNG Screenshots)
# =============================================================================

def generate_classification_output():
    """Generate classification output screenshot."""
    filename = "task-classification.png"
    print(f"\n=== Classification: {filename} ===")
    model = YOLO("yolo26n-cls.pt")
    results = model.predict(source="assets/bus.jpg")
    save_screenshot(results[0], filename)


def generate_detection_output():
    """Generate detection output screenshot."""
    filename = "task-detection.png"
    print(f"\n=== Detection: {filename} ===")
    model = YOLO("yolo26n.pt")
    results = model.predict(source="assets/bus.jpg")
    save_screenshot(results[0], filename)


def generate_segmentation_output():
    """Generate segmentation output screenshot."""
    filename = "task-segmentation.png"
    print(f"\n=== Segmentation: {filename} ===")
    model = YOLO("yolo26n-seg.pt")
    results = model.predict(source="assets/bus.jpg")
    save_screenshot(results[0], filename)


def generate_pose_output():
    """Generate pose estimation output screenshot."""
    filename = "task-pose.png"
    print(f"\n=== Pose Estimation: {filename} ===")
    model = YOLO("yolo26n-pose.pt")
    results = model.predict(source="assets/bus.jpg")
    save_screenshot(results[0], filename)


def generate_obb_output():
    """Generate OBB output screenshot."""
    filename = "task-obb.png"
    print(f"\n=== OBB: {filename} ===")
    model = YOLO("yolo26n-obb.pt")
    results = model.predict(source="https://ultralytics.com/images/boats.jpg", conf=0.7)
    save_screenshot(results[0], filename)


def generate_tracking_output():
    """Generate object tracking demonstration video."""
    filename = "task-tracking.mp4"
    output_path = os.path.join(VIDEO_DIR, filename)
    print(f"\n=== Tracking: {filename} ===")
    
    model = YOLO("yolo26n.pt")
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    results = model.track(source="assets/Cars.mp4", stream=True)
    for result in results:
        im = result.plot()
        out.write(im)
    
    out.release()
    print(f"Saved Video: {filename}")


# =============================================================================
# PART 2: SOLUTION OUTPUTS (Videos)
# =============================================================================

def generate_object_counting_output():
    """Generate object counting solution video."""
    filename = "solution-counting.mp4"
    output_path = os.path.join(VIDEO_DIR, filename)
    print(f"\n=== Object Counting: {filename} ===")
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    counter = solutions.ObjectCounter(
        show=False,
        region=[(100, height//2), (width-100, height//2)],
        model="yolo26n.pt"
    )
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            break
        results = counter(im0)
        if results.plot_im is not None:
            out.write(results.plot_im)
    
    cap.release()
    out.release()
    print(f"Saved Video: {filename}")


def generate_heatmap_output():
    """Generate heatmap solution video."""
    filename = "solution-heatmap.mp4"
    output_path = os.path.join(VIDEO_DIR, filename)
    print(f"\n=== Heatmap: {filename} ===")
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    heatmap = solutions.Heatmap(
        show=False,
        model="yolo26n.pt",
        colormap=cv2.COLORMAP_JET
    )
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            break
        results = heatmap(im0)
        if results.plot_im is not None:
            out.write(results.plot_im)
    
    cap.release()
    out.release()
    print(f"Saved Video: {filename}")


def generate_parking_output():
    """Generate parking management solution video using UHD footage."""
    filename = "solution-parking-occupancy.mp4"
    output_path = os.path.join(VIDEO_DIR, filename)
    print(f"\n=== Parking Management: {filename} ===")
    
    video_source = "assets/videos/4196207-uhd_3840_2160_24fps.mp4"
    cap = cv2.VideoCapture(video_source)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Calibrated coordinates for UHD video based on detections
    parking_json = "parking_spots.json"
    parking_data = [
        {"points": [[3430, 1650], [3600, 1650], [3600, 1870], [3430, 1870]]}, # Occupied (Spot 1)
        {"points": [[3510, 600], [3600, 600], [3600, 750], [3510, 750]]},     # Occupied (Spot 2)
        {"points": [[3200, 1650], [3400, 1650], [3400, 1870], [3200, 1870]]}, # Empty (Spot 3)
        {"points": [[1800, 1000], [2000, 1000], [2000, 1200], [1800, 1200]]}  # Generic (Spot 4)
    ]
    with open(parking_json, 'w') as f:
        json.dump(parking_data, f)
    
    manager = solutions.ParkingManagement(
        model="yolo26n.pt", 
        json_file=parking_json, 
        show=False
    )
    
    cap = cv2.VideoCapture(video_source)
    frame_count = 0
    while cap.isOpened() and frame_count < 120:
        success, im0 = cap.read()
        if not success:
            break
        results = manager(im0)
        if results.plot_im is not None:
            out.write(results.plot_im)
        frame_count += 1
    
    cap.release()
    out.release()
    if os.path.exists(parking_json):
        os.remove(parking_json)
    print(f"Saved Video: {filename}")


def generate_speed_output():
    """Generate speed estimation solution video."""
    filename = "solution-speed-estimation.mp4"
    output_path = os.path.join(VIDEO_DIR, filename)
    print(f"\n=== Speed Estimation: {filename} ===")
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    line_pts = [(0, height//2), (width, height//2)]
    speed_estimator = solutions.SpeedEstimator(
        model="yolo26n.pt", 
        region=line_pts, 
        show=False
    )
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    frame_count = 0
    while cap.isOpened() and frame_count < 150:
        success, im0 = cap.read()
        if not success:
            break
        results = speed_estimator(im0)
        if results.plot_im is not None:
            out.write(results.plot_im)
        frame_count += 1
    
    cap.release()
    out.release()
    print(f"Saved Video: {filename}")


def generate_sahi_output():
    """Generate SAHI sliced inference output video."""
    filename = "task-sahi-inference.mp4"
    output_path = os.path.join(VIDEO_DIR, filename)
    print(f"\n=== SAHI Sliced Inference: {filename} ===")
    
    cap = cv2.VideoCapture("assets/Cars.mp4")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    model = YOLO("yolo26n.pt")
    cap = cv2.VideoCapture("assets/Cars.mp4")
    frame_count = 0
    while cap.isOpened() and frame_count < 100:
        success, im0 = cap.read()
        if not success:
            break
        results = model.predict(im0, conf=0.3)
        im = results[0].plot()
        cv2.putText(im, "SAHI Sliced Inference Simulation", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        out.write(im)
        frame_count += 1
    
    cap.release()
    out.release()
    print(f"Saved Video: {filename}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 60)
    print("Generating YOLO slides outputs (Organized)...")
    print("=" * 60)
    
    # Task Outputs (Images)
    generate_classification_output()
    generate_detection_output()
    generate_segmentation_output()
    generate_pose_output()
    generate_obb_output()
    
    # Demo Outputs (Videos)
    generate_tracking_output()
    generate_sahi_output()
    generate_object_counting_output()
    generate_heatmap_output()
    generate_parking_output()
    generate_speed_output()
    
    print("\n" + "=" * 60)
    print("All outputs generated!")
    print(f"Images: {IMAGE_DIR}")
    print(f"Videos: {VIDEO_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()