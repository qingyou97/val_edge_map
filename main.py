1. BDCN training completed in the morning. Visual analysis and metric ranking for all cases. Conclusion: For extracting specified edges from an image:

- In the 1.5 category dataset, it fits well for images with small inter-class distances like 4-ball-screw. However, it performs poorly for 5-Cylinder and 5-groove even though they also have small inter-class distances.
- For images with larger inter-class distances, such as 1-Aero-engine-defect and 2-casting-product-image, training on a single image works well if the subsequent data is very similar. We expect improvements after changing the data selection logic and quantity.
- Training on a single image does not cause overfitting; it only leads to underfitting. This may be due to the small number of training epochs.

For the minimum number of images required currently:
- One image is enough for 4-ball-screw.
- For 1-Aero-engine-defect and 2-casting-product-image, consider the number of categories in the dataset.

2. Deployed Teed's code on Sun's machine and ran both single-image and full-set training codes.

3. The logic for adding the image with the lowest F1 score to Teed's new training set is incomplete. I finished the training and evaluation part; need to add new images and continue training. This should be runnable today.

4. Organized materials for the team meeting.
