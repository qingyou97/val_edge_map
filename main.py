Based on AI results, I used a rule-based method and compared it with applying rule-based methods directly on the original image and against the ground truth (GT) to determine if it matched the specific GT edge locations. 

Conclusion: Using a custom skeletonization function (repeated dilation and erosion, then image difference to update skeleton), I could extract very thin edges directly from the AI result which matched well with the GT upon comparison. 

Previously tried methods at the meeting had poor results:

a. Directly applying the rule-based method on AI results (rule-based sheet row 11) and on the original image (rule-based sheet row 7). The result on AI is not single-pixel edges. The gradient found is on the outer contour of the yellow area, so the comparison with GT (rule-based sheet row 13) did not match the GT's thin edge.

b. To solve non-single-pixel edges from Sobel, I applied NMS (Non-Maximum Suppression). This ensured thin edges (rule-based sheet row 15), but the comparison with GT still didn’t match the GT's thin edge (rule-based sheet row 17).

c. In the rule-based approach, finding peak intensity and exploring direction (phase). I applied Sobel on the original image to get intensity (magnitude&phase sheet row 9) and direction (magnitude&phase sheet row 11), and on the AI result (magnitude&phase sheet row 15 and row 17). Used HSV mapping for angle visualization. Did not utilize intensity and direction effectively, so switched to skeletonization.

Skeletonization methods:

d. Used an old recommended skimage library method but likely due to improper parameter settings or preprocessing, results did not meet expectations (skeletonize sheet row 9).

e. Using the repeated dilation-erision method, directly got very thin edges from the AI result (skeletonize sheet row 11). This matched well with the GT upon comparison (skeletonize sheet row 13).
