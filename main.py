1. Comparison table of four algorithms:
   - For the aero dataset, test images other than 4.
   - For ball-screw and casting datasets, add more different images.
   - For the model trained on 100 images, test other datasets and analyze.

Conclusion:
① For the aero dataset, tested images other than 4: Found similar test images to 5.jpg. BDCN fits our desired edges well, reducing noise. PIDINET has a lot of noise compared to the out-of-box results without reducing unwanted edges.
② For ball-screw and casting datasets: BDCN is strong on ball-screw, with excellent generalization after training on one image. Casting relies on test-train image similarity to suppress unwanted edges.
③ For a model trained on 100 images:
   - Aero: Can suppress unwanted edges if images are similar to the training set but with some noise, less than PIDINET.
   - Casting: Fits well if edges are smooth, with some breaking. Detects bumpy edges due to unwanted edge suppression.
   - Ball-screw: BDCN performs well, fitting images with some small breakpoints, better than PIDINET.
   - Cylinder: BDCN performs well, fitting images with some small breakpoints, better than PIDINET.
   - Groove: BDCN performs well, fitting most images, with some breakpoints, better than PIDINET.

2. Continue precision tuning for generalization, try different optimizers and test.

Conclusion:
   Tried ADAM optimizer on a casting image:
   - SGD at 100 epochs still leaves unsuppressed edges.
   - ADAM at 1e-6 learning rate: suppresses internal edges by 80th epoch.
   - ADAM at 1e-4 learning rate: suppresses internal edges by 40th epoch, with less continuity. Will test more parameters and optimizers.

3. New classifier with different optimizers.

Conclusion:
   Classifier optimization lower priority, so completed task 4 first.

4. Write and test inference code for the new classifier.

Conclusion:
   Completed inference code, result all white, indicating issues. Found a mistake in loss function input (used activated values instead of logits) and fixed it. Still not ideal, will try more parameters and optimizers later.

5. Task list with priorities:
① Improve BDCN precision generalization after training on one image.
② Tuned precision of updated BDCN with classifier.
③ Increase speed of updated BDCN with classifier.
④ Inference, comparison, analysis of DEXINED results.

6. Team Management Meeting:

Conclusion:
   Preparation of meeting materials and discussion with leaders consumed some time yesterday.
