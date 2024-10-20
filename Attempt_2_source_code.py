from PIL import Image
import numpy as np
from PIL import Image, ImageOps

with open("aes.bmp.enc", "rb") as enc_file:

    encrypted_data = enc_file.read()
encrypted_array = np.frombuffer(encrypted_data,dtype=np.uint8)
width = int(len(encrypted_array)**0.5) *2
height = len(encrypted_array)//(width)
trimmed_array = encrypted_array[:width * height]
image_array = trimmed_array.reshape((height,width))
img = Image.fromarray(image_array)
img = img.transpose(Image.FLIP_TOP_BOTTOM)
#img.show()
img1 = img.save("encrypted_visualizedtest.bmp")
# creating an image object
#img = Image.open(r"encrypted_visualizedtest.bmp").convert("L")

# image colorize function
img = ImageOps.colorize(img, black="blue", white="red")
img2 = img.save("bmpCOlorCOnverted.bmp")
img.show()
