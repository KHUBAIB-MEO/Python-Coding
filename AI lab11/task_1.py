from deepface import DeepFace
import matplotlib.pyplot as plt
import matplotlib.image as img

image1 = r"images\Chris Evans img1.jpg"
image2 = r"images\Chris Hemsworth img1.jpg"

test_image1 = img.imread(image1)
test_image2 = img.imread(image2)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(test_image1)
plt.title("Image 1")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(test_image2)
plt.title("Image 2")
plt.axis('off')

plt.tight_layout()
plt.show()
modelName = 'ArcFace'

resp = DeepFace.verify(image1, image2, model_name = modelName)
print(resp)

