from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load image
img = Image.open('vsort.jpg')

# Show RGB image
plt.imshow(img)
plt.title("RGB Image")
plt.axis('off')
plt.show()

# Convert image to NumPy array
rgb_array = np.array(img)
print("Image Shape: ", rgb_array.shape)

h, w, _ = rgb_array.shape


gray_array = np.zeros((h, w), dtype=np.uint8)


for i in range(h):
    for j in range(w):
        r, g, b = rgb_array[i][j]
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        gray_array[i][j] = gray


plt.imshow(gray_array, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

x=int(input("Enter the x coordinate: "))
y=int(input("Enter the y coordinate: "))

print("Gray Image Matrix:", gray_array[x][y])

