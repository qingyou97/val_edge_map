我也同时观察了修改了这两个参数后的前几轮的loss对比，我感觉确实是这俩参数的问题。因为之前用10e-6学习率与pertrained两个参数时，前几轮的loss很高，所以并没有延续之前模型的效果。反倒后来改了这俩参数后，前几轮的loss很低，这才是真正的接着训练。I also observed the loss comparison in the first few epochs after modifying these two parameters, and I feel that it is indeed an issue with these two parameters. When using a learning rate of 10e-6 and pre-trained settings before, the loss in the first few epochs was very high, so the model did not continue to perform as before. However, after changing these two parameters later, the loss in the first few epochs was very low, which was a real continuation of the training.
