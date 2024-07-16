1. Subsequent training and inference need to use a for loop.
2. In the implementation of the UNet model, change the final output layer from a binary classification activation function (often softmax or another function that outputs 0 or 1) to a sigmoid activation function.
3. Solve the overfitting issue on the background. Regarding Li Zhe's previous background overfitting issue, determine if it is due to insufficient training. You can plot a loss curve, just like Dan does, to analyze the process.
