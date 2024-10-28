1. Fix the ROI in the groove dataset and then test the upper and lower edges to check the detection effect.
Conclusion: Currently, fixing the ROI and then testing the upper and lower edges, both edges are quite smooth, and the effect is good. Attempt to start testing on the entire dataset.

2. Test results of automatic ROI selection in groove dataset.
Conclusion:
① Directly select the point with the highest peak value in each box. Phenomenon: There are many discontinuities. Reason: After finding this peak point, if it is not within the AI result, it is filtered out. Refer to lines 14-17.
② From the highest to lowest peak points, find the largest peak within the AI area. Phenomenon: In many large AI areas, the original image is not very clear, and the intensity value fluctuates greatly. Refer to lines 18-21.
③ Expand 4 pixels outward for the pixels within the AI area and increase contrast in the original image. Effect: Many areas became more continuous, and the detected lines became smoother. Refer to lines 22-25.
④ Detect vertical lines as well. Current results are in lines 26-29.
