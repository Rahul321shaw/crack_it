from PIL import Image, ImageDraw
img  = Image.open("pil_text.png")

# img = Image.new('RGB', (500, 200), color=(000, 000, 000))

d = ImageDraw.Draw(img)
d.text((20, 20), "Hello World", fill=(255, 0, 0))

img.save('111.png')