Regarding the implementation of the classification layer added after BDCN, the following has been completed and the code uploaded to GitLab:

1. Added a simple classification layer, code in classifier.py.
2. Solved the gradient back-propagation issue; loss now decreases normally. The cause was modified SGD parameters. Haven't yet investigated why passing weight_decay and momentum led to constant loss.
3. Moved BDCN fuse process and data loading outside the training loop, time is reduced.
4. Changed classification to three categories, including background as the third category.
5. Changed the loss function to CrossEntropyLoss.
6. Currently, inference code is not complete. Training on 20 casting images is ongoing. On Tuesday, I will write the test code and test the model.
