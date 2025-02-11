import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

#gambar
unggah = files.upload()
nama_gambar = list(unggah.keys())[0]

gambar = cv2.imread(nama_gambar)
gambar = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

pixel_gambar = gambar.reshape((-1, 3))
pixel_gambar = np.float32(pixel_gambar)

jumlah_klaster = 4
kriteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, label, pusat = cv2.kmeans(pixel_gambar, jumlah_klaster, None, kriteria, 10, cv2.KMEANS_RANDOM_CENTERS)

pusat = np.uint8(pusat)
segmen_gambar = pusat[label.flatten()].reshape(gambar.shape)

# hasil
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(gambar)
axs[0].set_title("Gambar Asli")
axs[0].axis('off')

axs[1].imshow(segmen_gambar)
axs[1].set_title(f"Segmentasi K-Means ({jumlah_klaster} Klaster)")
axs[1].axis('off')
plt.show()
