1. Try applying the generalization method of training BDCN on a single image to other works and see the results.
Conclusion: Previously, using the Adam optimizer with dropout significantly improved the discontinuous edge issues seen with SGD. However, it also caused some previously suppressed edges to appear slightly. I tried Adam+dropout on the cylinder dataset and found the same result. So, using Adam+dropout improves discontinuous edges but may cause some suppressed edges to reappear.

2. Try the three-class classifier on other datasets to see if the results are similar and check for issues like poor suppression or competing losses.
Conclusion: Using a three-class classifier on ball-screw and cylinder datasets, I found the results very unstable and hard to fit the ground truth (gt). The ball-screw dataset occasionally showed some fitting but became poor in the next iteration. The cylinder dataset did not fit the gt at all.

3. Change the classifier to a binary classifier. Earlier issues might be due to competing losses; now use a binary classifier consistent with the gt.
Conclusion: Switching to binary classification with binary cross-entropy loss still failed to fit the gt. There was a lot of noise, and the out-of-box edge results were mostly retained.

4. Try an initial segmentation and then integrate it into this one-shot method. This might be a new approach.
Conclusion: I tried a new approach. I found edge-detected grayscale images were not effective for classification since they lack texture and internal information, only providing an outline of objects. Classification needs rich pixel details and context, which edges fail to provide. Therefore, the classifier struggles to extract enough features from edge images, resulting in poor performance. So, I stopped using fused results and the gt for classification learning; instead, I combined the original image with the gt for learning. The training images fit well, but other images need further improvement.
