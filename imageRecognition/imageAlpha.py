from PIL import Image
import numpy as np

ei = Image.open("images/test2.png")
eiar = np.array(ei)

print(eiar)
