import easyocr

reader = easyocr.Reader(['en'],gpu= True)
results = reader.readtext("runs/detect/predict/crops/License_Plate/0_98.jpg") # Replace with your cropped images' path 

print(f"Detected Registration Number: {results}")

