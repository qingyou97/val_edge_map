1. Two-class classification: Removed fuse and tried sum1-5.
Conclusion: Using the previous classifier and tried sum1-5, but still couldn't suppress undesired ground truth (gt). Also tried variants like sum1234, sum123, sum12, and sum24. Found that almost all edges were detected without suppressing the unwanted gt.

2. Two-class classification: Followed requirements for convolution and up-sampling with nearest neighbor interpolation to help merge various feature layers.
Conclusion: Tried four architectures: summed sum1-sum2-sum3, summed sum2-sum3-sum4, summed sum1-sum2-sum3-sum4, and summed sum1-sum2. Documented every architecture and code in the 'classifiers' sheet. Found that using high-level features (sum4, sum5) degrades results significantly, even with parameter adjustments. Including low-level features (sum1, sum2) can lead to noise reduction, which helps distinguish internal circles with parameter tuning.

3. Tried the 128 channels feature layer from the VGG backbone.
Conclusion: Initially found poor results with two-class classification; documented results. Concluded that two-class classification might not be appropriate and merging desired pixel and background into one class seems unreasonable. Tried three-class classification and found better results, especially in detecting undesired rings. Noticed that most similar images could detect out-of-box features with good extraction.
