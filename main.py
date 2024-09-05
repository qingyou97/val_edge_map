1. Comparison with out-of-box: whether illumination causes performance degradation

Conclusion:

① Casting dataset: Images labeled with a yellow background have detection performance degraded due to illumination effects. Images with a pinkish background have poor detection due to the object's outer contour being jagged. Images with a green background are extremely affected by alternating light and dark due to illumination.

② Cylinder dataset: The reflective surface of the object leads to non-continuous edges. This situation is common.

③ Groove dataset: The lowest horizontal stripe is highly reflective and very bright, causing the two parallel lines at the bottom to fail detection. Images with a pinkish background indicate low light, causing low contrast at the bottom edge and thus failing detection.

2. BDCN fine-tuning and generalization improvement

Conclusion: The dropout method significantly solves the problem of discontinuous edges and greatly improves generalization.

① Sheet1 includes experiments with distinctive and representative results. For example, when using the SGD optimizer: although unwanted edges were greatly suppressed, the internal contours became extremely discontinuous, suppressing many desired edges.

② After switching to the Adam optimizer: fitting improved, internal contours remained discontinuous, but the results were much better than those with SGD, even though many desired edges were still suppressed.

③ Increasing the learning rate: resulted in retaining more desired edges but also introduced issues with unwanted edges appearing.

④ Seeking solutions: The dropout method was found. Adding dropout after each ReLU and setting it to 0.5 and other parameters significantly solved the discontinuity problem of edges, greatly improving generalization. Many shallow edges could now detect both contours, but some unwanted edges still remained.
