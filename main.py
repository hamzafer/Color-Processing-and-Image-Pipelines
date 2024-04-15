import colour
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def main():
    # Test numpy
    arr = np.array([1, 2, 3])
    print(f"Numpy array: {arr}")

    # Test matplotlib
    plt.plot(arr)
    plt.show()

    # Test colour-science
    rgb = colour.XYZ_to_sRGB(arr)
    print(f"RGB values: {rgb}")

    # Test opencv-python
    img = np.zeros((100, 100, 3), np.uint8)
    cv2.imshow('image', img)

    # Test Pillow
    img = Image.fromarray(np.uint8(img))
    img.show()


if __name__ == "__main__":
    main()
