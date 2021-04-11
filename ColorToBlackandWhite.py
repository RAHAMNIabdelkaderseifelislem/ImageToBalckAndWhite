from PIL import Image
from tkinter.filedialog import *

source = askopenfilenames(filetypes = (("PNG Files", "*.png;"),("JPG Files", "*.jpg;"),("All files", "*.*")))

img = Image.open("".join(source))

blackAndWhite = img.convert("L")
blackAndWhite.save("black_and_white_ver.png")
blackAndWhite.show()