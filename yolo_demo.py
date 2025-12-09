from ultralytics import YOLO

model = YOLO("C:/Users/moham/Downloads/best.pt") # Replace with your model's download path

results = model(source=0 ,device = "cuda:0", show=True, save_crop = True)



