import urllib.request
import os

os.makedirs("videos", exist_ok=True)

videos = {
    "traffic.mp4": "https://github.com/intel-iot-devkit/sample-videos/raw/master/car-detection.mp4",
    "people.mp4": "https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4"
}

for name, url in videos.items():
    path = os.path.join("videos", name)
    if not os.path.exists(path):
        print(f"Downloading {name}...")
        try:
            urllib.request.urlretrieve(url, path)
            print(f"Saved {path}")
        except Exception as e:
            print(f"Failed to download {name}: {e}")
    else:
        print(f"Already have {name}")
