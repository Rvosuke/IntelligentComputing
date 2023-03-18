from PIL import Image, ImageDraw

# Create a new RGBA image
img = Image.new("RGBA", (512, 512), (255, 255, 255, 255))

# Create a new ImageDraw object
draw = ImageDraw.Draw(img)

# # Draw a filled polygon on the image
# points = [(100, 100), (100, 400), (400, 400), (400, 100)]
# draw.polygon(points, fill=(0, 255, 0, 128))
triangle = Image.new('RGBA', (512, 512), (255, 255, 255, 255))
draw2 = ImageDraw.Draw(triangle)
draw2.polygon([(10, 10), (50, 10), (10, 50)], fill=(0, 0, 255, 128))

img = Image.alpha_composite(img, triangle)
# Display the image
img.show()
