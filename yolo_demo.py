from ultralytics import YOLO

model = YOLO("C:/Users/moham/Downloads/best.pt")

results = model(source=0 ,device = "cuda:0", show=True, save_crop = True)

