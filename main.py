0805 Morning meeting: 10.30-11
Paragraph:
1. The problem of edge fitting between dexined and pidinet.
2. Looking for a labeling tool for edge detection and labeling the dataset.
Han:
1. Fewshot overview. Tomorrow
2. An overview of edge detection. Meeting this afternoon.

4.00-4.11
Han Xu:
1. Join Priority: Level 3 or Level 5
2. How many man-hours are required for the survey?
3. How are vewpoints divided?
4. Pros and cons need reasons
5. Which direction do you want to do first?

Han Xu 17.32-18:
1. Fill in the reason again.
2. Which ones have been researched, and which ones need to be researched in the future.
3. Directly do the combination of pidinet and fss, second, foundation model ( 7.8.12.13 )
4. Quickly screen the papers and see if there are any other papers
5. Search for 7 papers
6. How to search, what are the keywords, what is the list
7. Research and implementation are priced separately, and tasks can be communicated at any time.

0806 10.00-10 Morning meeting:
Paragraph:
1. Pidinet training, how to deal with 7persn, whether the few people are deleted, and dexined also see if there is such a mechanism.
2. How is the training result of a single image of BDCN? Let's test it.
3. Try training with dexined and adjust the Learning Rate to see if it can achieve the effect of pidinet.
4. Select 20 datasets.
5. Looking for tools for edge annotation.
Han Xu:
1. Drag the receipt to the sprint
2. Define what the output of each jira is
3. Fill in the scheduled working hours
4. What are the subtasks of fss-pidinet?

0807 Morning meeting 10.00-10 46:
Section: Today's plan
1. What is the tool for dexined annotation?
2. When testing the remaining images, delete those that do not meet the requirements. (For future training, use 20 for training.)
3. When training flowers with dexined, first, 70 epochs is too few, try more to see if it can fit. Second, don't let the Learning Rate drop, just train at 0.001 and see the effect. Third, what does mean lr?
4. Train on bdcn using an image.
5. After labeling the data, try training with an image.
Han Xu:
1. Msanet, let's see how to combine it with the new plan
2. BAM, consider if there is a new architecture
3. What is the overall plan? Discuss with Duan to achieve direct push or a small amount of image enhancement, train in a few seconds, and report tomorrow.

0808 Morning Meeting 10.30-11:
Han Xu:
1. Now do pidinet, later switch to dexined.
2. Re-evaluate whether your own architecture is valid.
3. Zhao Hui turned the requirements into text: it can be pushed without support, and the edges that need to be added can be detected by adding support, and the edges that need to be ignored can also be ignored.
4. We will have a meeting in the afternoon to discuss the architecture.
Paragraph:
1. Go check the labelme annotation. I saw this morning that labelme can draw polygons, not closed lines.
2. Test the other out-of-box results of these two models.
3. Train one image at a time for training.

0809 Morning Meeting 10.00-10:
Paragraph:
1. Try training an image with dexined again.
2. How to combine dexined with fss. (Future plans)
3. Zhao recommended the new paper TEED, tested it, out-of-box, and compared it with the other three papers.
4. The new paper needs to include training content after TEED. (Future plans)
5. In the afternoon, we can use machines to experiment with anything we touch and run. After returning from vacation and training, we can directly conduct analysis.
6. PDINET, Dexined, and BDCN both train all five datasets for image experiments. As our own pre-trained model, we will also review this experiment this afternoon.
7. In the future, when doing testing and analysis, we can reason about the train image because of the gt. (Future plan)
8. Annotate two more datasets.
9. What is the result of BDCN 7person?
Han Xu:
1. Gitlab, daily update source code
2. Refer to the previous detection results and adjust the network architecture.

0809 15.00-15.30
Han Xu:
1. Priority, starting vote
Paragraph:
1. Normal

0819 Morning meeting 10-00-10
Duan Shengqing:
1. Normal
Han Xu:
1. List all experiments, write down priorities, implementation deadlines, and touch them tomorrow
2. Start implementation
3. Sort out the following three plans.
Matcher
SAM-edge-detection
DINOV2

0820 Morning Meeting 10.00-10:
Paragraph:
1. TEED train
2. Confirm the interpolation method after resizing to see if resizing too thick will cause the GT edge to disappear.
3. Let's check the overall schedule tomorrow. The schedule completed by the end of September.
Han Xu:
1. Introduce the follow-up ideas and algorithms
2. After 34, which one can be zero-shot? Share it, how to achieve it, and what effect can be achieved. Tomorrow afternoon.
3. What should I do if it's not feasible? I'll give the result tomorrow.

0821 Morning Meeting 10.00-11:
Paragraph:
1. New addition, modify the algorithm for training multiple images. For example, after training 2, if a certain image is found to have poor performance, add a new image.
2. Results prediction and indicator organization of BDCN and Pidinet.
3. Sort out the milestones with Han Xu, report tomorrow.
Han Xu:
1. Conclusion of major time nodes and initial results.
2. What is the reason for the delay in scheduling? How to avoid it in the future? Report tomorrow.

0822 Morning meeting 10.30-11:
Paragraph:
1. Consider partial fine tuning and Adapter next week
2. Bdcn visual analysis and indicator calculation
3. Teed training
Han:
1. Let's see if the following is feasible before starting the experiment
Reweight
tuning
2. Optimize the follow-up plan
3. Good ticket


0823 Morning Meeting 10.00-10:
Paragraph:
1. Test the other tests and stick it
2. Stick out-of-box
3. Test all the results of pidinet
4. Changes to the teed selection image mechanism
Han:
1. The result of each part of the zero technique and the composite result.
2. Is OneHot feasible?
3. Feasibility of merging zeroshot and oneshot (starting ticket)
4. Select specific works.
5. Result of parameter tuning
6. Look at the above next time
7. Other solutions, next week's schedule, what is next week's goal, and whether to follow the schedule next week

0826 Morning Meeting 10.00-10:
Han Xu:
1. Viewpoints are listed
2. Good ticket
Paragraph:
1. Make a table of the completion status
2. Search for methods to accelerate training, such as fixed layers, adapters, and adding classification layers
3. Let's touch these methods and perspectives tomorrow

0827 Morning meeting 10.00-11:
Paragraph:
1. Summarized document
2. Add a classification layer at the end of BDCN for implementation and testing
Han:
1. Adjusting distance
2. Try dcama direction
3. Adjust the small ticket and move it to jira.

0828 Morning Meeting 10.00-10:
Paragraph:
1. Summarize the fine-tuning of the document, change the generalization part of the test to three lines, original image, gt, result image
2. The fuse results before the newly added classifier can be placed in front to reduce time
3. The current way of reading and calculating loss in gt needs to add the background as a three-class classification and change the loss.
Han Xu:
1. Pidinet verification distance, change from l2 to cosine distance
2. Write a list of experiments and then communicate.
3. Reproduce the previous dexined result
4. Minimum receipt


0829 - 10:30-10:53 Morning meeting
Han
Be sure to commit after each result is released.
2. Summary of the results, write down the corresponding experimental conditions, and improve them in the form of a table.
Correspondence between experimental conditions and viewpoints, output results (Ps: Table in reference section)
3, ★ ★ scheduled homework, afternoon appointment with the listup of opinions, unified consciousness.
4. Summarize the effects of feature · and distance
5. What is the decama verification viewpoint? Need to be conscious
Priority projects after the meeting
Goal consensus, the existing implementation mode of OneSHot for this week's goal is feasible. Judge the feasibility of integration

0830 - 10:00-10:19 Morning meeting
Han
1. Today's goals and appointments, write ★ OneNote
2. ★ ★ ① Tasklist supplement, decama verification and other tasks are not recorded
3. ★ GitHub updates at least once a day
4, Sam2 and SegGPT verification want to do, discuss in the afternoon. Appointment ★ ★ ② Goals to be completed this week and next week
Priority projects after the meeting


0903 Morning meeting 10.00-10 39:
Paragraph:
1. Comparison table of four algorithms: For the aero dataset, test several images other than 4; for the ball-twist and casting datasets, paste several other images; for the model trained with 100 images, test other test data and analyze it.
2. Continue to do generalization precision tuning, try to change the optimizer, and try to do a work.
3. Newly added classifier, trying to change the optimizer
4. Write the inference code for the newly added classifier and test the results
5. Make a task list, write the priority, and touch it.
Han Xu:
1. Miou is not suitable for edge evaluation, and the evaluation indicators written in a different paragraph are changed.
2. Check what loss you are using and keep it consistent with the segment's loss
3. Change the backbone. The backbone trained by Coco is not suitable for reflecting the edge, so change it to the backbone of Pidinet.
4. What is the calculation method for each graph, record it
5. Record the specific calculation method for each experiment
6. Test other datasets and compare the final result with the segment

0904 Morning Meeting 10.00-10 47:
Han Xu:
1. Testing of ONESHOT global dataset
2. Fine-tuning of dcama, judge if it will exceed patchcore, make a plan
3. After the one-shot is over, judge whether mege is feasible
Paragraph:
1. Will lighting cause performance degradation compared to out-of-box?
2. Bdcn fine-tuning, generalization improvement
3. Fine-tuning of the classifier added by bdcn, it will be judged this week whether it is feasible

0905 Morning Meeting 10.30-11:
Paragraph:
1. The generalization of the training of bdcn can be further improved. Or, by adjusting the parameters and model size without learning, adjusting the pidinet can also be done to suppress some edge pixels. This needs to be considered.
2. The newly added classifier of bdcn currently has a trend of suppressing unwanted effects, but it needs to be further improved, and at least ensure that the trained one has good effects. If a classifier is connected at the end of the fuse, it may cause distance and other relationships to not be used. It can be considered to connect a shallow block to the classifier to see if it can improve the effect. This needs to be considered.
Han:
1. In the future, we need to fix the support for testing so that we can compare it with the results of the segment
2. How to improve generalization (patch core), how to suppress unwanted edges, AERO dataset is quite serious.
3. Dcama only trains on the metal dataset. If you want to adjust the points, write them down and send them to Teams. Priority is higher than 2.
4. Only use pidinet to train dcama.

0906 Morning Meeting 10.00-10:
Paragraph:
1. Bdcn's training program for improving generalization can be applied to other works to see the effect
2. Switch the classifier to binary classification. The previous poor performance may have been due to competition between losses. This time, switch to binary classification and keep the classification consistent with GT.
3. Try other works with the previous three classifications to see if the effect is consistent, whether the inhibition effect is not very good, or whether there is loss competition.
4. You can also try to do a segmentation first, using the SEG module, and then add the form of ONESHOT this time, which may become a new solution.
5. You can also learn about and implement Optuna in the future, but it will take some time to implement, so you can consider using it later.
 
Han Xu:
6. Patch the core and replace the backbone to see the effect.
7. Assign the pc with the segment, the segment is the administrator, and you can add account.
8. Oneshot's plan can be further improved to achieve completion, and a summary can be made
9. 345 can run:
  1. Try image augmentation of support
  2. Pidinet using different upstream blocks
  3. Adjust weights for each backbone block
10. Train dcama, 100 to see if it's a training problem


0910 Morning Meeting 10.00-11:
Paragraph:
1. So far, several solutions have drawn a flowchart
2. Regarding the classifier scheme, we are not looking for the last single-channel feature input to the classifier, but for the multi-channel features that have not been activated before. The number of channels and whether they have been activated will have a certain impact
3. Regarding the classifier, the last convolution layer inputs multi-channel features with 2 hints
4. What tasks can you help Han Xu share? Let's bump into it tomorrow morning.
Han Xu:
5. Write a separate document to summarize, with a brief one-sentence introduction of each attempted method and its impact. Organize the document according to the viewpoint. When selecting images, you can choose some representative ones. If you cannot reach a clear conclusion, you can also write it down.
6. Try the effect with patchsize = 1.
7. How effective is a single test of a pidinet?
8. In the result of training your own excel, the edges of the graph are intermittent. Check if it is a network problem or a problem with pasting excel.
9. Dcama trains 10 casting cards first, and then tests the remaining 10 cards to see how it goes
10. The focus of the follow-up is on merge, such as percentage or adding a convolution layer. Summarize and see which segments need to be done. We will do it tomorrow morning

0911 Morning Meeting 10.00-10:
Paragraph:
1. Delete fuse, try concat of sum1-5
2. For interpolation, try using the nearest neighbor interpolation method for sum1sum2sum3. Also, try other permutations and combinations.
3. You can try the 128 channels and 256 channels of VGG's backbone
4. Write a simple decoder in the classifier to help combine the layers of several features, and write upsample yourself.
Han Xu:
5. Investigate breakpoint issues, look at the input graph, the resized graph, and the graph of each stage to see where the problem lies
6. There is no problem with the allocation of segments
7. We will discuss the method of funetune tomorrow and listen to it in detail.

0912 Morning Meeting 10.30-11:
Paragraph:
1. Try Learning Rate 0.001 in the previous experiment.
2. Try replacing bdcn with wideresnet as the new feature input.
 
Han Xu:
3. Correct the order when organizing images
4. Dcama retraining after finding the problem
5. Patchcore's merge is finished


0913 Morning Meeting 10.00-10:
Paragraph:
1. Merge wideresnet and bdcn, the strategy of integration, and see the effect.
2. Run the experiment, and Han will sort out the follow-up.
Han:
3. List the methods for subsequent merges
4. Result format: comparison of one-shot, zero-shot, merge results
5. Find the reason for the poor effect of dcama, make the edges continuous, and then train again
6. Do a training with self-support and casting
7. Sort out the list of Han's achievements.

0918 Morning Meeting 1.00-1:
Han:
1. The overall direction of PATCHCORE is reasonable
2. All the methods planned at the beginning of today can be done. But the patchcore training with full data will be done later.
3. Test multiple supports.
4. Try to create a new solution. When using it, you can further manually adjust the one-shot zero-shot ratio on the detected results (with the difference of pixelwise).
5. Try using the upstream feature of pidinet on merge conv.
6. Select the good pictures of the section.

0919 Morning Meeting 10.30-11:
Han:
1. Continue to improve the performance of the merging network in the form of Unet.
2. Detect GPU settings
3. DCAMA pre-training should include casting
4. Do > 1 support patchcore
5. Design a new network architecture that outputs the weight value of the fusion algorithm, and then conceive a method that can manually adjust the weight. The two are separate directions.


0920 Morning Meeting 10.00-10:
Han:
1. The latest patchcore algorithm has significantly improved the performance and can "successfully" obtain the desired fine edges.
2. Make a to-do list for further improving the model.
3. Continue to increase or decrease the model size, use smaller feature inputs, and see if we can use small downstream fusion models to obtain weight maps and achieve results.
4. We need smaller and faster models.
5. The situation of missed inspections can be further improved.
6. It depends on the prediction results of the new DCAMA model.
7. Continue to test the patchcore supported by > 1
8. Analyze and test why Han's patchcore achieves good results when using a conv algorithm similar to the segment in fusion, but the segment cannot achieve the desired effect. Try removing the product of patchcore and try again.
9. Worktime has been supplemented.
10. Remote machine connection reinstallation
11. Put the latest results into deliverables.

0924 Morning Meeting 10:00-10:30:
Han:
1. The results of Patchcore with small conv-mergers have further improved. Now it needs to be fine-tuned and improved, including finer lines.
2. Add the visualization function of 2-support.
3. The direction of further optimization of the model can be done according to the ideas listed by Han.
4. You can test loss weighting or mask inflation on patchcore and dcama training.
5. To obtain CPU consumption.
6. DCAMA still needs to be improved as a direction to see if smaller parameter quantities can be used.

9-25 Morning meeting 10:00-10:30:
Han:
1. Zhao Renke's current direction. Summarize and showcase the existing model architecture and settings.
2. 1-Support and 2-support for better models
3. Continue to fine-tune to improve patchcore.
4. Apply the inflation method to patchcore.
5. Does not include BSDS data training DCAMA

9-26 Morning meeting 10:30-11:00:
Han:
1. Find support closer to query to do testing
2. Optimize and obtain the result of BCELoss, and find the difference between it and crossentropyloss
3. DCAMA training. This attempt did not use BSDS training from the beginning.
4. Continue in the direction of simple conv, because it is easy to use and lightweight.
5. Try using a simple conv

9-26 Morning meeting 13:00-13:30:
Han:
1. Adjust the conv structure, add sigmoid to the weights of 0-shot/1-shot, and then use clipping on the sum result. The input value range is also (0,1).
2. Try to train for a better result.
3. For DCAMA, retrain again, this time without casting, but including Groove.
4. Prove that 2-support is better than 1-support in the current choice of support

1008- Morning meeting: 10.00-10
Paragraph:
1. Comparison of rulebased results.
2. Compare the generated graph with rulebased or sobel, and stack them together to see the results.
3. Determine whether the resulting thin edges are consistent with gt at the pixel level.
4. When doing rulebased, find the peak magnitude intensity and exploration direction, the peak edge intensity, and the direction of the edge. Also, whether you can decide the peak and direction yourself.
5. Zhao will not be available next Tuesday. If you have any questions, please contact Zhengong and Shengdao.
Han Xu:
1. Patch core: Try changing epoch to 1 or 3
2. Patch core: Add Instance Normalization when learning, normalize on each sample separately
3. Patch core: check the batchsize.
4. Dcama: Try changing backbone to pidinet.
5. Dcama: How to merge oneshot and zeroshot with dcama to improve the oneshot ability of dcama? Can some zeroshot methods and possibilities be used?
6. Cylinder dataset, how to improve intermittent issues and find a balance in performance.
