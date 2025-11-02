from PIL import Image
import re

file_path = "file.txt"

# Read digits only
with open(file_path, "r") as f:
    data = re.findall(r"\d", f.read())

# Try to guess dimensions (close to square root of length)
import math
n = int(math.sqrt(len(data)))

width, height = n, n
print(f"Detected dimensions: {width}x{height}")

# Define color mapping (black for 0, white for 1-9)
colors = {
    "0": (0, 0, 0),
    "1": (255, 255, 255),
    "2": (200, 0, 0),
    "3": (180, 180, 180),
    "4": (160, 160, 160),
    "5": (140, 140, 140),
    "6": (120, 120, 120),
    "7": (100, 100, 100),
    "8": (80, 80, 80),
    "9": (60, 60, 60),
}

# Create the image
img = Image.new("RGB", (width, height))
pixels = img.load()

for i, char in enumerate(data[:width * height]):
    x = i % width
    y = i // width
    pixels[x, y] = colors.get(char, (0, 0, 0))

output_path = "image_from_text_auto.png"
img.save(output_path)

output_path
