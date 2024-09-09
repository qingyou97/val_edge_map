1. Original image and GT classification edge detection network
Conclusion: No significant results achieved on Monday due to poor generalization. The reasons include the low similarity between the edges in the GT and other images, and the strong influence of lighting.
   a. Tried adding positional encoding information, specifically XY grid coordinates and sine/cosine positional encoding to capture different frequency information. XY grid coordinates marginally suppressed some edges, while sine/cosine encoding had no noticeable effect.
   b. Added regularization in Adam and Dropout in the network, which slightly suppressed some edges, but the effect was minimal.
   c. Also added BN layers, deepened the network, and tried different weight initialization methods (Xavier and Kaiming), but observed no significant improvement.
2. Retrained the previous three-class results using the original image as input
Conclusion: At least the 0-2 shapes seemed to be fit, indicating normal network operation. The issue earlier might have been due to the network setup, since using fused grayscale images yielded too little information for stable learning.
3. New idea: Match the desired location in the original image using point feature matching network, then extract out-of-box points from the corresponding positions.
Conclusion: Tried LightGlue network but found that it matched very few points on the outer circle of the casting, with more points matched internally. This idea is temporarily shelved.
