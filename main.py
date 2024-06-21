import cv2
import numpy as np
import os
from skimage import io, filters
from sklearn.cluster import KMeans

def calculate_brightness(image):
    return np.mean(image)

def calculate_contrast(image):
    return image.std()

def calculate_complexity(image):
    edges = filters.sobel(image)
    return np.mean(edges)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append((filename, img))
    return images

def select_diverse_images(images, n_clusters=10):
    features = []
    for filename, img in images:
        brightness = calculate_brightness(img)
        contrast = calculate_contrast(img)
        complexity = calculate_complexity(img)
        features.append([brightness, contrast, complexity])
    
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(features)
    selected_images = []
    for i in range(n_clusters):
        cluster_indices = np.where(kmeans.labels_ == i)[0]
        selected_images.append(images[cluster_indices[0]])
    
    return selected_images

# Load images from the test folder
folder_path = 'path_to_your_test_images_folder'
images = load_images_from_folder(folder_path)

# Select 10 diverse images
selected_images = select_diverse_images(images, n_clusters=10)

# Print selected image filenames
for filename, _ in selected_images:
    print(filename)
