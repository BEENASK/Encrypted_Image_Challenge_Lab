#!/usr/bin/env python3
import sys
import random
from PIL import Image

file_path = "aes.bmp.enc"
output_path = "output_image.bmp"

# Colorize repetitive blocks in a file
 
def colorize(file_path,output_path,blocksize =16):
	with open(file_path, 'rb') as f:
		data = f.read()

#Ensure blocksize is an integer and process blocks
	blocks = [data[i:i + blocksize] for i in range(0, len(data), blocksize)]

# Create a simple random color palette
	palette = [random.randint(0, 255) for _ in range(256 * 3)]

# Map each block to a random color
	unique_blocks = list(set(blocks)) 
	block_colors = {block: unique_blocks.index(block) % 256 for block in unique_blocks}

# Create image data from blocks
	total_blocks = len(blocks)
	print(f"total_blocks:", total_blocks)
	width = int(((total_blocks ** 0.5)))
	print(width)
	height = (total_blocks + width - 1) // width
	print(height)
	img_data = [block_colors[block] for block in blocks]
	
# Create and display the image
 	img = Image.new('P', (width, height))
	img.putpalette(palette)
	img.putdata(img_data[:width * height])
	img = img.transpose(Image.FLIP_TOP_BOTTOM)
	img.save(output_path)
	print(f"Image saved to {output_path}")
	img.show() 

# Run the function if file is provided

if __name__ == "__main__":
	colorize(file_path,output_path)

