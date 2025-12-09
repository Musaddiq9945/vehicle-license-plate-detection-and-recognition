import easyocr

reader = easyocr.Reader(['en'],gpu= True)
results = reader.readtext("C:/Users/moham/Downloads/images.jpeg")
print(f"Detected Registration Number: {results}")