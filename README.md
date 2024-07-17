汇报了边缘检测的成果物,部分修改意见等以后有时间再继续完善。
I have reported the results of edge detection and some modification suggestions. I will continue to improve them when I have time.

完成了image级别和pixel级别的精确度、召回率和f值的代码编写。
I have completed coding for image-level and pixel-level accuracy, recall, and F-score.

测试了global_unstructured剪枝方法的结果,重新选取了unet中的编码器的卷积层作为剪枝的输入,测试了RandomUnstructured和L1Unstructured方法的剪枝数量分别在0.1,0.2,0.3下的image级别和pixel级别的精确度、召回率和f值。
The results of testing the global_unstructured pruning method were obtained. The convolutional layers of the encoder in the unet were re-selected as the input for pruning. The image-level and pixel-level precision, recall, and F-score were tested for the pruning amounts of RandomUnstructured and L1Unstructured methods at 0.1, 0.2, and 0.3.

实装了Instructured剪枝方法的结果。测试了分别
n=1,2,无穷大,无穷小以及剪枝数量分别在0.1,0.2
下的image级别和pixel级别的精确度、召回率和f
值。
Implemented the results of the Instructured Pruning method. Tested the accuracy, recall, and F-score at the image level and pixel level for n=1, 2, infinitely large, infinitely small, and pruning amounts of 0.1 and 0.2, respectively.

记录了以上所有结果的可视化结果图。
A visual representation of all the results recorded above.

Conclusion: The results of RandomUnstructured are very poor. Image-level metrics are almost all zero because they predict everything as foreground, causing pixel-level recall rates to approach 1. L1Unstructured shows no significant changes on the training set, but there is a slight increase in recall on the test set. In_structured performs very poorly when n equals positive or negative infinity. For n=1 and 2, there's a noticeable increase in recall on the test dataset.

Created a follow-up parallel plan for generalized tasks.
