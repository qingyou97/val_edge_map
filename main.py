0906 Morning Meeting 10:00-10:50:

Duan:
1. Apply the plan to improve the generalization of one-image training in BDCN to other works and see the effect.
2. Change the classifier to binary classification. Previous results were not good, possibly due to loss conflict. Align classifications with ground truth this time.
3. Try the previous three-class classification on other works to verify consistency and check if the suppression effect or loss conflict was the issue.
4. Try segmenting first, using SEG module, then add the one-shot approach; this may become a new plan.
5. Learn and implement Optuna in the future, but note that implementation will take time; consider it for later use.

Han Xu: 
6. Change the backbone in patch core and check the results.
7. Assign the PC with Duan, run experiments over the weekend.
8. Improve the one-shot plan further to completion and make a summary.
9. Run 3, 4, 5 experiments:
  a. Try image augmentation of support.
  b. Use different upstream blocks in Pidinet.
  c. Adjust weights for each backbone block.
10. Train DCAMA with 100 samples to see if it's a training issue.
