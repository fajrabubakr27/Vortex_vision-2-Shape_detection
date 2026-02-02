# Task 2: Geometric Shape Detection

This task is a computer vision application built with Python and OpenCV that automatically detects, classifies, and counts geometric shapes in an image.

##  Features
- Detects four types of shapes: **Triangles, Squares, Rectangles, and Circles**.
- Filters out noise and background artifacts.
- Automatically labels each shape in the output image.
- Saves the final result to the `assets/output_results/` directory.
- Displays a summary of the shape counts in the terminal.

##  Logic & Algorithm
The script follows these steps to achieve high accuracy:
1. **Preprocessing**: Converts the image to grayscale and applies Gaussian Blur to reduce noise.
2. **Edge Detection**: Uses the Canny algorithm to find the boundaries of the shapes.
3. **Contour Approximation**: 
   - Uses `cv2.findContours` to extract shapes.
   - Applies `cv2.approxPolyDP` to simplify contours and count the number of vertices.
4. **Classification Logic**:
   - **3 Vertices**: Triangle.
   - **4 Vertices**: Checks the **Aspect Ratio** (Width/Height). If it's close to 1.0, it's a **Square**; otherwise, it's a **Rectangle**.
   - **7+ Vertices**: Classified as a **Circle**.
5. **Noise Filtering**: Ignores very small contours (noise) or very large ones (frame boundaries).

