1. Filtered visualization results of the Lnstructured method with n equals 1 and quantity 0.2, and with n equals 2 and quantity 0.2. I didn't check many other folders where the recall is close to 1.
Conclusion: Currently, in these two folders, there is an image that the baseline model can't detect, but the pruned model can. Also, this image is the same in both cases. Many other images show larger and more continuous outlines.

2. Investigated why the output values in the source code are logits instead of values normalized by softmax.
Conclusion: The values I read for the foreground are indeed logits and not softmax normalized. I believe this is because, during inference, categories can be determined without softmax normalization before binarizing the images. I checked the code and noticed that normalization only occurs when calculating the dice_loss, as shown in the lines I wrote and the author's. I have also saved this result as a grayscale image, but the probability is too low for anything to be visible in the grayscale image. So I think the thresholding method is necessary to extract the foreground. Grayscale images are for visualization analysis only.

3. Learned part of the principles of torch-pruning.
Conclusion: Torch-pruning is based on structured pruning but includes the concepts of grouping and sparse training, which improve pruning performance. The overall process includes grouping, calculating importance, coefficient training, and pruning.
