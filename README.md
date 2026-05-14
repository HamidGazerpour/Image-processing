# Image Processing

A small Python project that demonstrates basic binary image-processing operations implemented from scratch and compares them with the equivalent OpenCV functions.

## Overview

The repository contains custom implementations of:

- **Thresholding**: converts a grayscale image to a binary image using a fixed threshold.
- **Erosion**: removes foreground pixels near object boundaries using a structuring element.
- **Dilation**: expands foreground regions using a structuring element.

`main.py` loads `image1.png`, converts it to grayscale, applies the custom operations, applies the equivalent OpenCV operations, and displays the results side by side with Matplotlib.

## Repository Contents

| File | Description |
| --- | --- |
| `main.py` | Demo script that loads the image, runs the custom and OpenCV image-processing operations, and plots the results. |
| `project_functions.py` | Contains the custom `threshold`, `erosion`, and `dilation` implementations. |
| `image1.png` | Sample input image used by the demo script. |

## Requirements

- Python 3.x
- NumPy
- OpenCV for Python
- Matplotlib

Install the dependencies with:

```bash
pip install numpy opencv-python matplotlib
```

## Usage

From the repository root, run:

```bash
python main.py
```

The script processes `image1.png` and opens a Matplotlib figure containing:

1. Original image
2. Custom threshold result
3. Custom erosion result
4. Custom dilation result
5. Grayscale image
6. OpenCV threshold result
7. OpenCV erosion result
8. OpenCV dilation result

## How It Works

The demo uses a `5 x 5` kernel and a threshold value of `120`:

```python
kernel = np.ones((5, 5), np.uint8)
th = threshold(img_gray, 120)
img_eroded = erosion(th, kernel, iterations=1)
img_dilated = dilation(th, kernel, iterations=1)
```

The OpenCV results are generated with `cv.threshold`, `cv.erode`, and `cv.dilate` so the output can be compared with the custom implementations.

## Notes

- The custom functions are written for educational clarity rather than performance.
- The erosion and dilation functions expect a binary image where foreground pixels are `255` and background pixels are `0`.
- If you use a different input image, update the path passed to `cv.imread` in `main.py`.
