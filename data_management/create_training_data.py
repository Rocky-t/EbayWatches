import csv
import sys
sys.path.insert(1,"../")
import PIL 
from PIL import Image 
import requests
from io import BytesIO


# Run this file with the appropriate names and close to 100,000 watch images will download. labels in the write csv
with open('<name of csv write file>', 'w', newline='') as csvwrite, open('<name of csv read file>', 'r', newline='') as csvread:
    datawriter = csv.writer(csvwrite)
    datareader = csv.reader(csvread)

    i = 0
    for row in datareader:
       #initialize variables
        if i % 200 == 0: 
            print(f"processing watch {i} out of 110,500")

        url = row[0]
        label = row[1]
        name = "watch" + str(i)
        
        try:
        #get PIL image from link
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
        except:
            continue

        #only want images of a certain quality
        if sum(img.size) < 400:
            continue

        #resize, save label and image
        img = img.resize((200,300))
        datawriter.writerow([name,label,url])
        if i > 17096:
            img.save(f"../training_data/{name}.jpg")
        i += 1