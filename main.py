1. Casting dataset - Currently, we keep the local maxima points closer to the inner diameter, and further fine-tuning is needed.
Conclusion: Changing the gradient towards the center improved the results, filtering out more outer edges.

2. Casting dataset - Alternating bright and dark algorithm to determine edge retention.
Conclusion: The first custom version retains only left-bright-right-dark on the left half of the image, and left-dark-right-bright on the right half. Also need logic for up and down. Results are mediocre, with intermittent gaps.
The second version determines which edge is closer to the center with darker pixels and further with brighter pixels, removing the need for directional logic. Currently testing this.

3. Try other datasets like groove and cylinder, as the method currently shows good results on casting. Fine-tuning can be done later.
Conclusion: Using dexined results, tested on groove and cylinder.
Cylinder: The first version took the highest peak, showing a double edge. The second version detects an ellipse and keeps the edge closer to the center.
Groove: Currently, it takes the highest peak points.
