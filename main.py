Morning Meeting 0910  10:00-11:07:

Duàn:
1. Draw a flowchart for each solution up to now.
2. For the classifier solution, the features inputted are the multi-channel features before the activation layer, not the final single-channel features. The number of channels and whether they go through an activation function will have a certain impact.
3. For the classifier, the last convolutional layer inputs the multi-channel features as mentioned in point 2.
4. Discuss which tasks can be shared with Han Xu in the meeting tomorrow morning.

Han Xu:
5. Write a separate document as a summary. Briefly introduce each method tried and its impact. Arrange the document according to viewpoints and choose representative images. Even if no clear conclusion can be made, it can be written down.
6. Test the effect when patchsize=1.
7. Test the effect of a single pidinet.
8. Analyze whether the issue of broken edges in the charts from the training results is due to the network or the pasted Excel.
9. First train 10 casting images with dcama and then test the remaining 10 images to see the result.
10. Focus on the merging step next. Summarize how to proceed, whether by percentage or adding another convolutional layer. Determine what Duàn needs to do and follow up in the morning meeting.
