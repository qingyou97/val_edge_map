1. Improving the generalization of training one image with BDCN
   Conclusion:
   a. I have fine-tuned the dropout in BDCN; currently, there is one result that is better at suppression than before.
   b. I input this result into the classifier and suppressed the internal edges again. I found that the classifier is effective, and many previously shallow edges were suppressed. So, I think my classifier and logic are temporarily fine. But every time I add the classifier to the fuse, the effect is very unstable and difficult to fit.

2. The scheme of connecting the classifier after the fuse
   Conclusion:
   a. The scheme of connecting the classifier after the fuse was later changed to directly connecting the classifier with the deep2shallow3 block. After adding the classifier with deep2shallow3 block and fuse concatenated, I found that the effect is very unstable and hard to control.
   b. For the scheme of connecting the classifier after the fuse, sometimes fine-tuning a few times, fixing the random seed, and lowering the learning rate can occasionally achieve effects like in lines 12 and 13. But currently, there are still intermittent internal edges and cases where suppression does not occur.
