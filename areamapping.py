import cv2
import numpy as np
import yaml

map_image_path = "/home/thitipongth/map.pgm"
yaml_path = "/home/thitipongth/map.yaml"

map_image = cv2.imread(map_image_path, cv2.IMREAD_GRAYSCALE)

with open(yaml_path, 'r') as file:
    map_metadata = yaml.safe_load(file)
resolution = map_metadata['resolution'] * 2.75

_, thresholded = cv2.threshold(map_image, 200, 255, cv2.THRESH_BINARY_INV)

occupied_pixels = np.sum(thresholded == 255)

# Calculate the mapped area in m²
mapped_area = occupied_pixels * (resolution ** 2)
print(f"Mapped Area: {mapped_area:.2f} m²")