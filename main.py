Morning Meeting: 10:00-10:36
Duan:
1. Comparison of rule-based results.
2. Apply rule-based methods like Sobel to generated images, compare with direct rule-based methods, and overlay for comparison.
3. Check if extracted thin edges match ground truth at the pixel level.
4. When doing rule-based, find peak magnitude strength and explore directions, edge strength peaks, and edge directions. Also, consider if peaks and directions can be determined manually.
5. Zhao will be absent next Tuesday, contact Makoto and Ikushima if there are issues.

Han Xu:
1. Patch Core: Change epoch to 1 or 3 and test.
2. Patch Core: Add Instance Normalization during learning processes, normalize individually for each sample.
3. Patch Core: Check batch size.
4. DCAMA: Change backbone to PiDiNet.
5. DCAMA: Explore combining oneshot and zeroshot methods to enhance oneshot capabilities, determine if zeroshot methods can help.
6. Cylinder dataset: Improve the issue of intermittency, find a balance in performance.
