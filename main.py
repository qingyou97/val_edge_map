0903 Morning Meeting 10:00-10:39:

Duan's tasks:
1. Comparison table for four algorithms: Test with aero dataset using images other than the 4; for ball-screw and casting datasets, add more images; test the models trained with 100 images on other test data and analyze.
2. Continue tuning accuracy for generalization, try changing the optimizer, and do a work trial.
3. Try changing the optimizer on the newly added classifier.
4. Write the inference code for the new classifier and test the results.
5. List tasks and set priorities; discuss them.

Hanxu's tasks:
6. miou is not suitable for edge evaluation, use the metric written by Duan.
7. Check which loss you are using and align it with Duan's loss.
8. Change backbone as coco-trained backbone is not suitable for edge; use pidinet's backbone instead.
9. Record the calculation method for each image.
10. Record the specific calculation method for each experiment.
11. Test other datasets and compare final results with Duan's.
