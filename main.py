from PIL import Image
import glob
import os

image_path = 'Image compression'
os.mkdir(image_path)

for picture in glob.glob('*.webp'):
	image = Image.open(picture)
	image.save(f"{image_path}/{picture}", 'webp', optimize=True, quality=30)
  
