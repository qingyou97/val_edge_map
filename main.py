1. Summary of various aspects of the training of the four networks.
Conclusion: Currently, I have compared the three trained networks from 6 aspects to determine which dataset quantity yields the best results. Yesterday, the teed training was completed, but I haven't run inference and analysis yet, so I conducted the comparison and analysis of the other 6 aspects.

2. In bdcn, add a classification layer at the final fusion layer to suppress unwanted edges.
Conclusion: A classification layer has been added, and ground truth (gt) is correctly input. Positive samples are input gt, and negative samples are edges fused and subtracted from gt. Following pidinet, the fused background is first labeled as 0.5, then the mask is set to 0, so the background is excluded from the calculation. Currently, the loss does not change in each training epoch, and saving the model hasn't been implemented yet. I am looking for the problem.
