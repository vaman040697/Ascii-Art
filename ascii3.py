from PIL import Image, ImageDraw, ImageFont
import math

# ASCII characters for intensity mapping (dark to light)
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256

# Scaling and font parameters
scaleFactor = 0.15  # Resolution scaling
oneCharWidth = 5    # Reduced width for tighter spacing
oneCharHeight = 10  # Reduced height for proportional spacing

def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]

# Open input image
im = Image.open("/Users/sanjaymalik/Desktop/car.jpg")

# Use a smaller font for better resolution
fnt = ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 8)

# Resize image for ASCII mapping
width, height = im.size
im = im.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

# Prepare output image
outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

# Convert pixels to ASCII
with open("Output.txt", "w") as text_file:
    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r / 3 + g / 3 + b / 3)
            pix[j, i] = (h, h, h)  # Convert to grayscale
            char = getChar(h)
            text_file.write(char)
            d.text((j * oneCharWidth, i * oneCharHeight), char, font=fnt, fill=(r, g, b))  # Colored ASCII

        text_file.write('\n')

# Save output image
outputImage.save('output2.png')
print("ASCII art with reduced spacing saved as 'output2.png' and 'Output.txt'.")
