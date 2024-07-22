1JHCAI-64
1.1 Had a meeting with you to explain the pruning methods in torch-pruning.
Conclusion: Through code testing, metapruner can use four importance calculation methods: GroupNormImportance, BNScaleImportance, LAMPImportance, and FPGMImportance. Will continue to read today to understand what these four methods entail.

2JHCAI-61
2.1 Wrote a for-loop script to train data from 7 folders. Completed
2.2 Selected the first training model and viewed the detection results of the baseline model on cable images.
Conclusion: Currently believe there is no overfitting on cable images, and the detection results are pretty good. Completed
2.3 Wrote a for-loop script for iterative pruning and inference in torch-pruning.
Conclusion: The automatically adjusted parameters include the importance method (4 types), p (l1 norm or l2 norm), the number of pruned elements, and the number of iterations (how many iterations to complete this pruning). Pruning for cable has been completed; others need further testing.

Scrum Manager
3.1 Created subsequent plans in the afternoon. Completed
