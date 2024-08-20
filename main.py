1. teed's out-of-box inference results comparison.

Conclusion: Although TEED’s edges are thinner as the paper claims, it loses a lot of details. There are datasets where other three algorithms performed well, but TEED didn’t. TEED's architecture is similar to dexined, with the only change being the reduction from 6 blocks to 4 blocks.

2. pidinet trained with 5 datasets; 121 scenarios.

Have completed predictions for 121 scenarios at 100, 200, and 299 epochs, and calculated recall, precision, F1 regarding gt, and sorting.

Conclusion: Each model’s three metrics are recorded in Excel. With datasets having 20 images with small gaps, training one image results in the highest precision and F1. For datasets with larger gaps, the highest metrics occur when training with 7 or 9 images. Training with all 100 images does not always result in the highest metrics.

3. BDCN trained with 3/5/7/9 images. 

Conclusion: Finished writing the for loop, but still have about half of the datasets left to train.

4. pidinet training with biped dataset. 

Read the augmentation steps for biped training:

i) Split each high-resolution image in half along the width;
ii) Rotate each resulting image into 15 different angles, and crop using a rectangle oriented along the image axis;
iii) Horizontally flip the images;
iv) Apply two gamma correction values (0.3030, 0.6060). 

Each image generates 288 augmentation images. Training completed.

Today's plan:

1. For pidinet trained with 5 datasets and 121 scenarios. Combine the best images into Excel for a visual comparison.
2. Predict and analyze metrics for bdcn models trained with one image versus 100 images, totaling 101 scenarios, each with three epochs.
3. Evaluate and compile visual results for pidinet trained with the bipedv2 dataset.
4. Train dexined with one image and 20 images.
