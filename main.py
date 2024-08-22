1. Communicate with Han-san about the schedule, finalize the timeline and milestones.
2. Tested the GitLab upload method with Han-san. Some faiss files in his folder had issues due to Git configuration causing newline characters to switch from LF to CRLF, which is common on Windows. Tried various methods to enforce Git to use LF or CRLF, but none worked well. Decided not to upload these faiss files for now.
3. Since the three machines (bdcn, pidinet, dexined) have not finished training, I ran the teed training code on my PC and wrote codes for three types of loop training.
Today's plan:
4. pidinet has one more biped experiment and one random image experiment to finish. I will complete the biped today and skip the random algorithm for now. I will visualize and calculate metrics for all cases.
5. BDCN training will finish this morning. I will visualize and calculate metrics for all cases.
6. I will run teed on Sun's machine, both for single image training and full training.
7. dexined is only on the second dataset so far. I plan to pause it and change the logic to not do inference during training.
8. I will examine teed's fusion module and understand the differences from lcd and dexined fusion modules.
