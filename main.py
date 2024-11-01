1. Process the result of 8support using this algorithm: In each ai result's pixel, extend a line along the gradient direction of the point, then find the point of maximum peak on the extension line. For casting and bottle datasets, choose the pixel point closer to the circle center on the extension line. File link:

2. Process the result of 8support using this algorithm: For circular datasets, convert the sector to a rectangle for coordinate transformation. Use y-axis mapping to find the peak point, taking the maximum average in a 5-pixel length sliding window. For rectangular edge data, perform a sliding window on the rectangle, using size 5 for mapping and averaging. File link:

3. Process the 8support result using this algorithm: Traverse each point in the ai region, lock the point in place with a 10x10 square box, calculate the average gradient direction of all points within the square, rotate this box, then map and calculate the peak point in the rotated square, finally find a peak point within the ai region. File link:
