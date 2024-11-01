1. When finding the peak, it is necessary to use all points for the calculation and then locate the peaks within the AI-designated regions. After correcting problem 1 and other error-tolerant mechanisms, the dataset was tested and compared.
Conclusion:
The ball-screw dataset has been processed. After implementing the error tolerance handling and filtering of peak points within the AI region, the edges have become distinctly continuous. This proves that this method is effective and has strong generalization ability. Other datasets may suffer from poorly set sliding windows, leading to very jagged edges with a lot of noise. However, the results are better than expected, and the code logic is highly adaptable.

2. I need to review the best document tomorrow morning, considering branches, how to execute, reproduce the results, and maintain a separate Excel sheet including all works. The best results compiled from the ball-screw highlight that last night's version outperforms all previous solutions. For the other five datasets, previous outcomes are still better.

3. A comparison between the generalized algorithm's effectiveness and previous results.
Conclusion: It may be due to the length and width of the sliding window, which was set to suit the edges of the ball-screw. Other results still need further adjustment.
