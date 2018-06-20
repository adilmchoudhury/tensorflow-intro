import os
import tensorflow as tf
import skimage.data
import numpy as np

def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory)
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f)
                      for f in os.listdir(label_directory)
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels

ROOT_PATH = "/Users/Shared/Documents/Project/pyCharm/"
train_data_directory = os.path.join(ROOT_PATH, "BelgiumTSC/xTraining")
test_data_directory = os.path.join(ROOT_PATH, "BelgiumTSC/Testing")

images, labels = load_data(train_data_directory)

images = np.asarray(images)
labels = np.asarray(labels)


# Print the `images` dimensions
print(images.ndim)

# Print the number of `images`'s elements
print(images.size)

# Print the first instance of `images`
#print(images[0])

# Print the `labels` dimensions
print(labels.ndim)

# Print the number of `labels`'s elements
print(labels.size)

# Count the number of labels
print(len(set(labels)))

print(labels)