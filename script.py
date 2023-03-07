import math
import urllib.request
from PIL import Image, ImageDraw, ImageFont

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256
scaleFactor = 0.09
oneCharWidth = 10
oneCharHeight = 18


def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]


text_file = open("ASCII-Text.txt", "w")
urllib.request.urlretrieve(
    'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6d3ec4cb-cd5f-46fe-969b-ba4e6d9626cc/d9x5o5o-5bf8a093-5be1-4ae3-aa3d-6e158c44fd67.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzZkM2VjNGNiLWNkNWYtNDZmZS05NjliLWJhNGU2ZDk2MjZjY1wvZDl4NW81by01YmY4YTA5My01YmUxLTRhZTMtYWEzZC02ZTE1OGM0NGZkNjcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.wJz9nu2pUmHtoSMc4fgdYePIlzAwcNjJYnsh1euAIik',
    "Input-Image.png")

im = Image.open("Input-Image.png").convert('RGB')

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height *
               (oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new(
    'RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight),
               getChar(h), font=fnt, fill=(r, g, b))

    text_file.write('\n')

outputImage.save('ASCII-Image.png')
