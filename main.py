1. There was an issue with the casting code, reran it.
Conclusion: Used the same version result, modified the code slightly. The effect on the casting dataset improved greatly, the offset issue was solved. Previously, many points were taken outside, this time most points are on the inner side, perfectly capturing the inner edge. File link:

2. Regarding the unsolved issue of the double edges on casting, the new plan is to expand the circle using polar coordinates around the center. Convert the circle to Cartesian coordinates, with horizontal axis representing blocks and vertical axis representing each extended line and intensity value. Map and average in regions, use sliding window to judge which point to keep. Test casting effect.
Conclusion: Many breakpoints, needs improvement. Current plan is to take a line every degree, average every five degrees to get the top two points. Poor effect. File link:

3. Organize the best version results of all datasets into an Excel. Include original image, black-and-white result, overlay result.
Conclusion: Done, file link:

4. Test Han Xu’s one-shot after receiving it.
Conclusion: For the current one-shot result, I took all the AI regions and applied a rule-based method. Result has many noisy points in AI output, so current rule-based result is poor. Today, I will set a threshold on AI results to filter out some noise and reevaluate the results. File link:
