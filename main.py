1. BDCN tested 1000 test data from 5 datasets and pasted the results into a spreadsheet. Conclusion: Due to the large number of images, Excel opened slowly and crashed once. I then split it into 5 Excel files. The conclusion is that the test performance matches that of non-trained images in the training dataset. If the model is fitted to a specific ground truth (gt), it will only detect this gt during testing.

2. BDCN performed out-of-box testing on these 100 training images due to slow selection time, and directly tested and added them to the table as a supplement.

3. Tested pidinet training results on five datasets and organized into 5 spreadsheets. Conclusion: The fifth dataset and the model trained with all 100 images have not been organized yet. The rest are completed. Conclusion is:

4. Implemented the logic for teed's selection image training. After each training, added one image with the lowest f1 score from the remaining images to the training. It is currently training, starting with a minimum of 1 image, up to 6 images. Discovered a problem when 6 images were selected at the end of the first dataset. Checking the logic again and will fix it today.

5. This morning, completed the teed training for a single image and all images.

Today:
6. Test the pidinet model trained with the 100-image dataset.

7. Test the results of pidinet trained with BIPED and compare with the previous out-of-box results to see if it can be used as a pre-trained model.

8. If it can be used as a pre-trained model, use this model as a pre-trained model to train single images and all images from 5 datasets, to evaluate its capability for out-of-box and fine-tuning.

9. Test teed models trained with single images and all images, and perform visual analysis.

10. Modify the teed image selection training logic and initiate training before leaving.
