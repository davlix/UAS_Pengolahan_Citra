import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import cv2
from google.colab import files
from scipy.ndimage import convolve

#gambar
unggah = files.upload()
nama_gambar = list(unggah.keys())[0]
gambar = imageio.imread(nama_gambar, mode='L')

#Roberts
roberts_x = np.array([[1, 0], [0, -1]])
roberts_y = np.array([[0, 1], [-1, 0]])
tepi_roberts_x = convolve(gambar, roberts_x)
tepi_roberts_y = convolve(gambar, roberts_y)
tepi_roberts = np.sqrt(tepi_roberts_x**2 + tepi_roberts_y**2)
tepi_roberts = (tepi_roberts / tepi_roberts.max()) * 255

#Sobel
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
tepi_sobel_x = convolve(gambar, sobel_x)
tepi_sobel_y = convolve(gambar, sobel_y)
tepi_sobel = np.sqrt(tepi_sobel_x**2 + tepi_sobel_y**2)
tepi_sobel = (tepi_sobel / tepi_sobel.max()) * 255

#Canny
tepi_canny = cv2.Canny(gambar, 100, 200)

#Prewitt
prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
tepi_prewitt_x = convolve(gambar, prewitt_x)
tepi_prewitt_y = convolve(gambar, prewitt_y)
tepi_prewitt = np.sqrt(tepi_prewitt_x**2 + tepi_prewitt_y**2)
tepi_prewitt = (tepi_prewitt / tepi_prewitt.max()) * 255

#hasil
fig, axes = plt.subplots(1, 5, figsize=(20, 5))
axes[0].imshow(gambar, cmap='gray')
axes[0].set_title('Gambar Asli')
axes[0].axis('off')

axes[1].imshow(tepi_roberts, cmap='gray')
axes[1].set_title("Deteksi Tepi Roberts")
axes[1].axis('off')

axes[2].imshow(tepi_sobel, cmap='gray')
axes[2].set_title("Deteksi Tepi Sobel")
axes[2].axis('off')

axes[3].imshow(tepi_prewitt, cmap='gray')
axes[3].set_title("Deteksi Tepi Prewitt")
axes[3].axis('off')

axes[4].imshow(tepi_canny, cmap='gray')
axes[4].set_title("Deteksi Tepi Canny")
axes[4].axis('off')

plt.show()
