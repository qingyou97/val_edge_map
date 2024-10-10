1. Overlay GT and original image to confirm which layer GT is on:
Conclusion: First, the GT I drew is not precise and overlaps the artifact outlines. Second, dilation causes learning of edges on both layers. (Images in the xxx file’s sheet at row 29). Third, GT adjustments will be completed this morning.

2. Handwritten rule: Keep points closer to the inner diameter.
Conclusion: Done. Comparatively, it's better than taking the maximum peak point. (Images in the xxx file’s sheet at row 29)
Circle center rule: Read grayscale image and apply morphological opening and closing operations to denoise. Use thresholding to convert the image to binary and apply Laplace transform for edge detection to find contours. Fit each contour to an ellipse and select the one with the smallest axis ratio as the most circular ellipse.
Point filtering rule: Take points in both positive and negative gradient directions until five continuous points with an intensity of 0 are found. From these points, find two peak points and select the one closer to the circle center. (Explanation is in the last section of the xxx word file)
Effect: Better than taking the maximum peak point but retained some outer points. Since some gradients were selected in non-perpendicular directions to the contour, our logic couldn't interfere, causing extra points. (Explanation is in the last section of the xxx word file)

3. Team management meeting and data organization.

4. Handwritten rule: Retain points from light to dark on the innerside edges; if AI doesn’t work, use rule-based customization to solve edges.
Conclusion: Not started yet.

5. Experiment with Han’s Dexined results.
Conclusion: Not received yet.
