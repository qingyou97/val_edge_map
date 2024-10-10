1. In the AI results area, combined with the edges detected by Sobel on the original image, find the point with the strongest intensity in the gradient direction's extended line for all points, and keep this point. Check this logic against the ground truth (GT).
Conclusion: The result indeed has thinner edges, but there are discontinuities, and due to illumination artifacts, there are double edges. This logic selects a point and then extends along the gradient direction from that point, sampling five consecutive points with intensity 0 on both sides (chosen to avoid merging dense edges from other datasets). Perhaps five points is too few, resulting in a smaller range and double edges. Second, visual inspection of these artifacts shows thicker edges, so detecting two edges is normal. Some manual method may be needed to specify which edge to keep.
My calculation steps file link:
2. Future milestone for combining AI results with rule-based methods.
Conclusion: My file link xxxx
