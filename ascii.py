from PIL import Image, ImageDraw, ImageFont
import math

# Scheme for the inner blue parts (first image)
chars_inner = " .`'^:,;Il!i<>~+_-?[]{}1()|/tfjrxnuvczXYUJCLQ0OZmwmqpdbkhao*#MW&8%B@$"[::-1]

# Scheme for the background and bright areas (second image)
chars_outer = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

# Scaling and font parameters
scaleFactor = 0.15  # Increased for better resolution
oneCharWidth = 7    # Reduced for finer character placement
oneCharHeight = 14  # Adjusted aspect ratio for accuracy

def getChar(inputInt):
    # Define thresholds for inner blue and outer parts
    if inputInt > 100:  # Example threshold for bright/background areas
        return chars_outer[math.floor(inputInt * (len(chars_outer) / 256))]
    else:  # Apply inner blue scheme for darker areas
        return chars_inner[math.floor(inputInt * (len(chars_inner) / 256))]

# Open input image
im = Image.open("/Users/sanjaymalik/Desktop/car.jpg")

# Use a smaller font for better resolution
fnt = ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 10)

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
outputImage.save('output7.png')
print("ASCII art saved as 'output7.png' and 'Output.txt'.")
