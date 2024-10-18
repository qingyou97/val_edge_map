10.18 Morning meeting 10:00-10:10：

Duan:
1. Regarding the issue of casting two-layer edges not being fully resolved, the new solution is to expand according to the polar coordinates of the center of the circle. Flatten the circle into horizontal and vertical coordinates, with the horizontal being each block and the vertical being each extension line and strength value. Each time, we can map the area and take the average value using a sliding window to determine which point to keep. Determine the casting effect.
2. Organize the best version of datasets into one Excel file, including original images, black and white results, and overlay results.
3. Test once Han Xu provides oneshot.

Han:
1. Think and test why multi-support has more noise than single support and how to improve.
2. Improve the merge part to ensure that zeroshot can be detected and ultimately output.
3. DCAMA results needed by Monday.
