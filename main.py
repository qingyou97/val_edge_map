0711 Daily Scrum  
15:47-16:41 PM
Han Xu:
1. Use the industrial-5i dataset. Get out-of-box results for all classes in top123. Do not pretrain initially.
2. Record inference time, etc.
3. If pmnet doesn't work, try other variants of decama or hsnet. If that doesn't work, train from scratch.
0716 Daily Scrum 
13:00-13:43 PM
Duan Shengqing:
1. Schedule a separate meeting tomorrow to explain the results of edge detection.
2. Can start the generalization task now.
Li Zhe:
1. In method 2, check the paper to see how pruning was done.
2. Li Zhe should explain it clearly to Duan, and Duan should also learn by himself and organize it well before explaining it to Zhao.
3. Each result needs to be traceable.
4. Source code should be uploaded to GitLab. Once a day.
Han Xu:
1. Train for a few rounds first.
Wang Chao:
1. KNN, organize the GitLab repository.
0717 Daily Scrum 
10:30-11:00 AM
Han Xu:
1. Meeting in the afternoon to discuss datasets;
2. Need to organize visualization results for subsequent testing;
Wang Chao:
1. Review the simplified KNN project to ensure it can run on their machines, then write instructions for implementation;
Duan Shengqing:
1. Implement and test both structured and unstructured methods from the official PyTorch documentation;
2. If time permits, review structured pruning in link 2;
Li Zhe:
1. Change the activation function to sigmoid and test the results.
14:00-15:00 PM
Duan:
1. Before the meeting, it was mentioned about the generalization tasks. A plan on how Li Zhe and I will proceed in parallel needs to be prepared, and we will discuss it tomorrow.
2. Today's meeting is about presenting an overall summary of edge detection. The following points are all regarding edge detection (the timing for them depends on when the generalization task ends):
3. In the Canny algorithm, avoid binarizing after the Sobel operator, generate a result, and check if the HHA result is still subpar.
4. Retrain 200 images with Dexined, and compare the improvements after retraining.
5. Compare the results of three different methods after training on one image.
6. What is the backbone of PIDInet, and what is the proportion of inference time spent on the backbone.
7. What structure in Dexined leads to its good performance.
Han Xu:
1. Organize the above content for further sharing.
2. Determine how to split the training and testing datasets.
3. Decide how to train the three models.
0718 Daily Scrum 
10:30-11:00 AM
Han and Wang:
1. Continue discussing the experimental plan in the afternoon;
Duan:
1. Find and organize the images that previously could not be detected but can be detected after pruning, as they can serve as a standard for judgment.
2. Perform torch-pruning on the models selected by Li Zhe and document the process.
3. Write the description for the AUROC metric.
Li Zhe:
1. Compare the models trained on 10 images with those trained on 5 images to see which one is more overfitted. Finally, select one model.
2. Prune the selected models using the official PyTorch pruning method, test the metrics, and produce documentation.
3. Write the description for the AUROC metric.
14:00-14:30 PM
Han Xu, Wang Chao:
1. Investigate how long it will take to modify the dataset code if we want to unify the training set, and discuss it with him.
2. Sort out the division of the train and test data.
0719 Daily Scrum 
10:30-11:10 AM
Han Xu, Wang Chao:
1. Need to specify how much data is used for training and testing. Continue discussing this in the afternoon meeting.
2. What will the test results be used for? Continue discussing this in the afternoon meeting.
Li Zhe, Duan Shengqing:
1. Output should be in grayscale images.
2. Re-check the sigmoid function to understand why the output values are not normalized.
3. For the baseline model’s results, re-examine the most overfitted model.
4. Duan should re-check other folders to see if images that were undetectable before become detectable after pruning.
13:30-14:00 PM
Han Xu, Wang Chao:
1. Upload the source code to GitLab.
2. Organize and refine the planned documentation.
3. Plan how to select different types of support and query (no rush, think it through).
4. Add grayscale images to the results and convert the probability to grayscale for easier viewing.
5. Determine methods to avoid over-detection.
6. Summarize all results and formulate a strategy for item 5.
7. Check top123 first, then baseline; if all three are unsatisfactory, don't consider baseline.
8. Consolidate all visualized data sets into an Excel file.
0722 Daily Scrum
10:30-11:10 AM
Wang Chao:
1. We need to consider how to format the comparison of the three methods and decide on the best approach.
2. Review the visualization results tomorrow.
Duan:
1. Test all other pruning methods and check the visualization results. It’s also acceptable to put the raw datasets into NAS.
2. Continue selecting overfitted models.
3. Write down how to cooperate in the future.
Li Zhe:
1. Upload previous results to NAS. At least the useful data should be retained.
2. Color defect in grayscale training is not considered overfitting. If it can't be detected on red yet was trained on gray, it's not counted as overfitting. Duan continues to select overfitted models.
3. Clarify the experimental range and record the range and parameters.
16:00-16:30 PM
Duan:
1. Explain the torch-pruning method and which importance calculation methods can be used by the metapruner.
2. Discuss the three diagrams of coefficient training, their correlation in abc, and which one the author used.
0723 Daily Scrum  
10:30-11:00 AM
Wang Chao:
1. Simple conclusions need to be written in the daily report.
2. Check the effect within the same defect category.
3. Check the effect of the mixed model for the same defect. It needs to be categorized.
Li Zhe and Duan:
1. GitLab.
2. First, check if recall improves after pruning. If it does, then look at the visualization results.
3. Today, merge Duan's "for" and Li Zhe's "for" loop code.
4. Add code for four pruning ranges in the code.
5. Illustrate which pattern to prune at which layer with a graph.
6. After each pruning method, find the one with the highest recall (set a threshold, balance with other sorted results to avoid overly high values).
0724 Daily Scrum
10:30-11:00 AM
Han Xu:
1. First, construct a one-shot dataset of the same defect type, ensuring both the support and query sets are of the same defect type.
2. Once step 1 is completed, proceed with training.
3. Record all code modifications and procedures used.
Wang Chao:
1. Update the task table, recording daily conclusions and issues, and synchronize with Duan's task pool.
Duan:
1. Complete the remaining dataset training.
2. Explain the four importance methods tomorrow. Discuss the rationale behind the settings and their effects.
3. Include images in GitLab.
4. Filter and visualize the results.

Li Zhe:
1. Organize deliverables following Duan’s format.
2. Filter and visualize the results.
0725 Daily Scrum
10:30-11:00 AM
Han Xu:
1. Consider whether Han Xu continues to conduct a new survey.
2. Discuss the follow-up project management tomorrow.
Wang Chao:
1. Find time today to discuss the follow-up new task; he tends toward few-shot tasks for Wang Chao, mainly engineering-based.
2. Discuss the follow-up project management tomorrow.
Duan:
1. Assign the task of checking visualization results to Li Zhe.
2. I will start looking for new ways to improve generalization, with post-training methods prioritized, followed by training methods.
3. Find ways that guarantee 100% improvement in generalization.
Li Zhe:
1. Continue checking visualization results and organize the relationship between generalization and pruning.
14:30-15:00 PM
Li Zhe:
1. Prune the layers a bit higher, such as down4 or up1, and test this on two or three datasets.
2. Focus on the grid and hazelnut datasets.
Duan:
1. Return to edge detection next week. He will break down follow-up tasks into multiple tasks. (Dong asked if there is any possibility of doing these tasks in parallel with others. Zhao replied that it can't be parallelized and must be done sequentially.)
2. MVTec dataset, images for industrial inspection. We will need to find this dataset later.
0726 Daily Scrum 
10:30-11:00 AM
Han Xu:
1. Summarize fine-grained or other data and classify them in a table.
2. Organize few-shot data for Wang Chao today and discuss in the afternoon. There's no specified start time for edge detection after the discussion.

Wang Chao:
1. Training and testing can be conducted together.
2. Testing can be assigned to Han today.

Duan:
1. Find other methods to improve generalization.

Li Zhe:
1. Fine-tune the scope and parameters of pruning in more detail.
2. Document the problems encountered yesterday.
3. Upload images to the NAS.
4. Organize and visualize according to Duan's format.
17:00-17:30 PM
Han Xu and Wang Chao:
1. Visualize task pool issues with images. Discuss with Duan how to summarize. Both Wang Chao and Han Xu should know the conclusions.
2. Wang Chao will summarize the images.
3. Organize the conclusions, including overall summaries and each point's strengths and weaknesses. Highlight the supporting data for each issue, outline the overview, priorities, and severity. Wang Chao will summarize.
0729 Daily Scrum 
10:30-11:00 AM
Next Meeting:
1. Jira maintenance and updates, post documents and deliverables in the comments.
2. Click "done" on previously completed tasks.
Han Xu:
1. Jira summary.
2. Create a problem list with explanations, and provide them to Duan.
3. Summary and overview. Complete by Tuesday.
4. Start edge detection today.
Wang Chao:
1. What tasks are remaining?
2. Duan should create a few-shot task.
Duan:
1. Find a dataset for edge detection.
2. Discuss new pruning methods in the afternoon meeting.
Li Zhe:
1. Estimate when a certain task will be completed and discuss in Teams.
16:00-16:47 PM
1. Li Zhe should write the details on the tickets, and everyone else too.
2. Write the experiment's format and the status of whether it's done or not, and which parameters are optimal.
3. Once parameters are selected, directly paste the graph.
4. If a certain parameter range is good, directly run more granular values of that parameter.
5. After analyzing the above, try the ECE method proposed by Duan.
6. Later, reply to the current task of Li Zhe.
0730 Daily Scrum 
10:30-11:00 AM
1. Organize JIRA like Duan and assist others.
2. The daily report needs to include why the previous plans were not completed.
Wang Chao:
1. There was a spreadsheet from Han Xu before. Clarify what is still unfinished and how much longer it will take. We’ll meet in the afternoon.
2. Reflect this in JIRA.
Li Zhe:
1. Change the scope.
2. Use spreadsheets for future recordings, don’t use memos.
3. Fill in the other pixel-level results first.
4. Look at other major losses and show them.
5. Post the JIRA link.
6. Post images of other work under the same conditions (up1up2) for oil.
7. Post branches and commits to JIRA.
Duan and Han:
1. Report again at 2 pm Japan time.

13:00-13:37 PM
Duan:
1. Check if the Halcon dataset meets the requirements.
2. Look for other datasets.
3. Train one and check the detection results.
4. Train a few and find the best effect.
5. Crack images are more like segmentation rather than edge detection.
6. If the training effect is poor, change the image and retrain within 200 iterations, try different combinations.
7. Train one image, if the effect is bad, train two images together; use indicators to filter.
8. Create tickets for all anticipated experiments.
9. Discuss the overview tomorrow. Record any urgent matters in the overview.
10. Dexined and PIDined training results are different; no other edges in PIDinet, gray levels in the dexined flower.
11. Retrain on the flower, check the effect on other similar images.

Han Xu:
1. Discuss the few-shot overview in the afternoon meeting, cooperate with Wang Chao.
2. Prior to the meeting with Zhao, reach consensus with Duan on subsequent edge detection materials.

17.30-19:00 PM
Han Xu, Wang Chao:
1. There is still an FSS task, mix industrial net with query train, Duan will create a ticket.
2. Include non-fine-grain results as well.
3. Record all remaining experiments and later decide on priorities.
4. Industrial net, mix query train,
5. DecAMA, retrain; all bad, mix bad
0731 Daily Scrum 
10:30-11:00 AM
Wang Chao:
1. Review the finalized PPT this afternoon
2. How to improve the shortcomings, such as passing the inspection or undetected issues, by retraining to learn the method
3. Train today. Discuss priorities
Li Zhe:
1. Check other graphs with the same parameters
2. Also organize the unstructured data, perform different methods on the same work
Duan:
1. Discuss the dataset in the afternoon
Han Xu:
1. Later discuss feasible directions, Incremental FSS for Few-shot learning, and Light-weight architecture design
2. Parameter-efficient training methods (explain in the afternoon)
13:30-14:00 PM
Duan:
1. Not defect detection, but edge detection datasets for industrial scenarios before size measurement. Metal types. Engines, drive shafts, easily affected by lighting. Contrast is very low due to some lighting effects. If we want to capture the edge, it's not very precise. We don't have particularly well-constructed datasets on hand. These data should be collected properly.
2. Similar to PatchCore mechanism, the process of creating the vector for this image (he calls it logging?) takes just a few seconds, subsequent inference is also fast.
3. Anomaly detection, SVDD, PatchCore still have many heads design. Don't tweak parameters, fine-tuning, because it's very slow.
4. Training uses images one, two, three at a time.
Han Xu:
1. Summarize and then explain
2. Quantities, whether they meet our requirements
3. Any additional potential for extending the Light-weight architecture design, needs research.
16:42-17:46 PM
Wang Chao:
1. Two coarse trains not done
2. Paste the path of the result files in the spreadsheet
3. color messing dcama mix mix
4. Annotate the results under each condition
5. What's good about each algorithm
6. segget, which condition is optimal, choose within the condition
7. Abstract and further refine the conclusions
8. Discuss again after organizing things tomorrow afternoon
9. Paste the support for "Inability to get fine segmentation, high inaccuracy caused by soft diffusive boundaries."
Han Xu:
1. Discuss Incremental FSS tomorrow
0801 Daily Scrum
10:30-11:00 AM
Wang Chao:
1. Organize the afternoon meeting materials.

Li Zhe:
1. What is the conclusion, and what chart corresponds to the conclusion? Summarize it in the document. Post the document on Jira.
2. For torch-pruning, arrange the experimental conditions. Post the information on Jira.

Duan:
1. Select a few datasets to discuss further in the afternoon.
2. Organize the number of images and label status. Schedule a meeting once it's organized.

Han Xu:
1. Discuss the organized research materials in the afternoon.

14:00-15:16 PM
Duan:
1. Extract all the data that meet the requirements for train and test datasets. (Priority 1)
2. First label 20 training images. (Priority 4)
3. Find a tool for edge annotation. (Priority 3)
4. Conduct an out-of-box test. (Priority 2)

Han Xu:
1. Review these methods further. Summarize which ones are usable and which are not, and provide the theoretical basis.
2. Explain the internal review to Duan.
3. Meet again tomorrow.

17:46-18:39 PM
1. Write the steps for GitLab, including branching, commit, and how to modify parameters for testing.
2. Is the difference between 5-shot and 1-shot reflected in the data (is there an overlap that affects the results) or in the method?
3. Compare Five-shot with One-shot: test the middle sample in One-shot.
4. What is the reason for the poor performance in One-shot, is it due to the data?
5. What are the task analysis and problem analysis?
0802 Daily Scrum 
10:30-10:50 AM
Wang Chao:
1. The characteristics of different methods, such as which detections arise from which data directions.
Li Zhe:
1. What are commit and branch, how to set up experiments in GitLab and Source, and write documentation.
2. Summarize what's missing.
3. The difference between two methods.
Duan:
1. Only label the edges that are needed when annotating, with the focus on training.
Han Xu:
1. Give an overview in the afternoon. Confirm the future directions.
16:00-17:00 PM
Han Xu:
1. How fast is it, and how much does it help us?
2. Review the paper on PEFT and linear layers.
3. Analyze improvement suggestions for the Patch Core direction.
4. A table overviewing opinions and corresponding research papers (priority list).
5. Create a ticket.
All Members:
1. Update TIME for all members.
2. How to logout. Once Duan knows, inform Wang Chao and Li Zhe.
Duan:
1. Consolidate into one table, indicating which edges.
