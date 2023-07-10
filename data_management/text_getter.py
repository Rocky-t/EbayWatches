from PIL import Image
import requests
from io import BytesIO
from pytesseract import pytesseract

"""
Experimental file.
Idea: if I can get text from images, I can read the brand name off the dial even if the listing
      does not have the watch's brand name

Result: Existing packages aren't sensitive enough to the small text on a dial and I don't have 
        the resources to train a better one
"""

image_url = r"https://cdn.shopify.com/s/files/1/0256/3031/0455/products/13034421_xxl_v1574628399891.jpg?v=1604082687"
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
# img.show()
text = pytesseract.image_to_string(img)
print(len(text))

print(text)