Conclusion:

1. Can specified edges be extracted from a single image?
   In 5 datasets, the model is effective on 4-ball-screw, which has small inter-class distance. However, for 5-Cylinder and 5-groove, also with small inter-class distance, the performance is poor. For images with larger inter-class distance, like 1-Aero-engine-defect and 2-casting-product-image, training on a single image works well for similar images. This may improve by changing data selection and quantity.

2. Does training on a single image cause overfitting?
   Currently, training on one image results only in insufficient fitting, with no overfitting observed. This could be due to the short training epochs.

3. What is the minimum number of images required?
   For 4-ball-screw, one image is sufficient. For 1-Aero-engine-defect and 2-casting-product-image, it depends on the number of image types in the dataset.

4. Training on 100 images yields good performance, fitting each image’s ground truth well.
