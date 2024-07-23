1. Collected experimental information into a results table.
a. Organized all information about the currently selected baseline model, including the reason for selecting this baseline and relevant diagrams.
b. Diagrams regarding the pruning range.
c. Details about all implemented pruning methods.
d. Information on parameter tuning for the implemented pruning methods.
   
2. Completed the for-loop code, which tested 3 baseline models and 4 structured pruning methods from torch-pruning in a loop.
a. Added code to set the pruning ranges. There are currently four situations: `[['inc'],['down1', 'down2', 'down3', 'down4'], ['up1', 'up3', 'up4'], ['out']]`.
b. Added code to calculate recall for each pruning parameter setting, and selected the top1 by comparing results under the condition of recall not exceeding 0.9.
   
Conclusion: Testing is complete, and the top1 indicators for the three baselines have been recorded. The results show an improvement in recall for all three baseline models. However, the visualization results have not been reviewed yet. Pruning in the encoder phase yielded better results, and the FPGM method for calculating importance is preferable.
