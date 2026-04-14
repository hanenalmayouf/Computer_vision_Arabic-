from ultralytics import YOLO

model = YOLO('yolo26n-pose.pt')
res = model.predict(source='https://ultralytics.com/images/bus.jpg', imgsz=640, conf=0.1)

r = res[0]
print('type', type(r.keypoints))
print('shape', r.keypoints.data.shape)
print('sample', r.keypoints.data[:1,:5,:])
print('attrs', [a for a in dir(r.keypoints) if not a.startswith('_')])
print('r keys', [k for k in r.__dict__.keys() if not k.startswith('_')])
print('kp first person first 5 points', r.keypoints.data[0,:5,:])
