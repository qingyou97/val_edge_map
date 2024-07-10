1. Low threshold: The first threshold. Pixels below this value are considered non-edges and are directly discarded.
2. High threshold: The second threshold. Pixels above this value are considered definite edges, called strong edges.
3. Dual threshold: Pixels between the two thresholds are called weak edges. Their edge status is determined by their connection to definite edges. If a weak edge pixel is connected to a strong edge pixel (8-connected), it is considered an edge. If a weak edge pixel is not connected to a strong edge pixel, it is suppressed.
