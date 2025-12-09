import easyocr

reader = easyocr.Reader(['en'],gpu= True)
results = reader.readtext("C:/Users/moham/Downloads/images.jpeg") # Replace with your cropped images' path 

print(f"Detected Registration Number: {results}")
