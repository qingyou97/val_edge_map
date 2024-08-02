1. What are commit and branch, how to set up experiments for GitLab and Source, documenting them.
2. The results from torch-pruning for inferior images are summarized too.
The conclusion is: zipper combined and cable combined defects.
3. What is the summary of official pytorch methods and torch-pruning methods?
The conclusion is:
1. From the results of torch-pruning experiments, it is clear that the parameters that perform well in each defect detection method are not universal, just like in pytorch pruning methods. Different types of data images and the degree of model overfitting after training lead to different optimal pruning parameter settings, including pruning strategy, pruning scope, and pruning amount.
2. Both PyTorch pruning methods and torch-pruning performed better than the baseline on tile-oil and crack defect pruning. Torch-pruning performed well on the pill, but the pytorch method did not. So, different pruning methods cannot achieve similar results on the same baseline.
3. The results of pytorch and torch-pruning are as follows: From the perspective of the oil defect in tile, because during annotation, the oil area and background area are mixed together as ground truth, but the model learned the fine-grained segmentation area of the oil; it is currently believed to be in an overfitted state. In this case, pruning and parameter removal will produce a generalization effect. Both pruning methods verified the same excellent generalization effect in this scenario.
