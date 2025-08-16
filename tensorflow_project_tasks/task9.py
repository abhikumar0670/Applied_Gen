import matplotlib.pyplot as plt
import numpy as np

# Dummy test images
test_images = np.random.rand(5, 150, 150, 3)

index_to_plot = 1
plt.imshow(test_images[index_to_plot])
plt.title("Test Image using Extract Features Model")
plt.axis('off')
plt.show()