0709 4:00-5:30 PM:
Li Zhe:
1. Plan experiments for other 10*10 and 15*15 datasets.
2. Test the train model as well.
3. Image level: AUROC.
4. OpenVINO pruning method: if OpenVINO doesn't support, look for other pruning methods.
5. Internally coordinate goals. Identify sub-tasks.

Han Xu:
6. Attach screenshots of metrics as proof. Summarize the findings. Due tomorrow.
7. Use PANET (as baseline) at the end.
8. TOP3: IndustrialNet, PMNet, SegGPT.

0710 daily scrum 10:30-11:00:

Duàn:
1. The Canny threshold is set too high. He thinks we need to use 128 and half of 128.
2. Test this model on other test images and organize the results.

Hán Xù:
3. Write an experiment plan when implementing. Then, discuss it.
4. Start with IndustrialNet first.

Lǐ Zhé:
5. Continue researching pruning methods because he wants to reduce model size.
6. Discussion in the afternoon (1:00-1:30). Bring your own ideas and pruning methods. Also, look into the principles of weight compression.

0710, 1:00-1:15 PM:

Zhe Li:

1. Zhao provided 4 links about sparsity. Need to read them.
2. Additionally, search for other pruning methods in PyTorch. Discuss after searching.
3. Highest priority is to choose and implement a pruning method.
4. Check task pool background problems with Duan and record in task pool. (Low priority)

0710, 5:50-6:24 PM
Zhe Li:

1. Zhao thinks that every interface function in link 1 has an explanation and hopes we can provide a description. Li Zhe should cooperate with Duan. Write the descriptions to a level that is understandable. Li Zhe should summarize while investigating.
2. Duan started reporting on the four types of pruning methods on Teams. Zhao feels that now they know what we are doing but not the reasons and which method we should choose for each link.
3. In future meetings, writing a not very detailed document is fine.
4. Duan should organize the task priorities (first implement the methods in link 2, then roughly investigate the principles of each method).
