1. Current training completion status of four algorithms (Table):

| Algorithm | Training Completion Status     |
| --------- | ------------------------------ |
| Algorithm A | Completed                     |
| Algorithm B | Completed                     |
| Algorithm C | In progress                   |
| Algorithm D | Not started                   |

2. Visual analysis of pidinet training on 100 images.

Conclusion: Currently, pidinet is not fitting as well as bdcn when training on 100 images. Pidinet fits well on ball-screw and groove images but introduces some noise. For the other three types—cylinder, casting, aero-engine—it does not fully fit the ground truth (gt).

3. TEED training includes testing and adding the image with the lowest F1 score each time.
Conclusion: Script has been modified. Training is in progress.

4. TEED training results on a single image vs. all images.
Conclusion: Fitting performance is poor; it does not detect the needed edges in the gt. It detects all edges in the image with a lot of noise. This behavior is the same for all datasets.

5. Tested pidinet trained on biped.
Conclusion: The training result is below expectations with a lot of noise. Though the number of detected edges is decent, noise is still a problem.

6. Searched for methods to accelerate training, also studied adapter techniques.
Conclusion: After reviewing adapter tuning, it appears to reduce training time and computational resources because only a specific small set of parameters are trained, without adjusting the whole model. Also, parameter freezing methods: 

1. Freezing early network layers (reused in multiple tasks as they learn general features).
2. Experiment to identify layers with minimal gradient change for freezing.
3. Gradient clipping to ensure gradient values remain in range, accelerating convergence (e.g., achieving the same efficacy in 100 epochs vs. 150 epochs without clipping).
4. Adding a classification layer for finer resolution in classification.
