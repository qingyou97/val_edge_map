1030 Morning Meeting 10:00-10:34:

Duan:
1. Modify the latest generalization algorithm to first perform horizontal sliding window within the AI area, then calculate the average gradient direction within this window. Rotate the window to this gradient direction, then map and select peak points. Following this idea of generalization, write the logic, test on 6 datasets, and record the effects.
2. Compare and organize the results of this generalized algorithm with the previously set ROI results.
3. Find the cause of breakpoints in the aero algorithm.

Han:
1. Add some support, test the effect, and organize.
2. Impose some constraints on the loss, such as adding constraints to adjacent pixels to make results smoother and more connected.
3. Reduce the number of feature layers, test the effect, and organize.
4. Post the best results of each dataset to OneNote.
