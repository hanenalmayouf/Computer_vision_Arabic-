import time

def heavy_inference(frame):
    """Simulates real CPU load."""
    count = 0
    for i in range(10**5):
        count += i
    return frame

def mp_worker(in_q, out_q):
    """The worker function that lives in the separate process."""
    while True:
        frame = in_q.get()
        if frame is None: 
            break
        result = heavy_inference(frame)
        out_q.put(result)
