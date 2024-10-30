1. Other four datasets: Consider using a sliding window method to determine the region of interest (ROI), and then adjust the algorithm. Test on other datasets.

Conclusion:
- Bottle: The polar coordinate algorithm makes some edges segmented. It doesn't perform as well as finding points closer to the center.
- Cylinder: Tried to find the ring but failed, so switched to a sliding window across the image width and identified peaks with a distance greater than 4, ultimately finding four peaks in the AI region.
- Ball-screw: In a 224x224 AI result image, locate the uppermost point with the largest x-value. Divide at this point and find four extreme points on the left and three on the right.
- Aero: Use a sliding window of 5 over the entire range to locate peak points.

2. Consolidate all results and place the best results on a single sheet, including the reproduction process.

Conclusion:
- Bottle completed: The best results include 2 versions (one using polar coordinates and one focusing on points closer to the center), with 4 other versions.
- Casting completed: The best results include 2 versions, with 9 other versions.
- Groove completed: The best results include 2 versions, with 8 other versions.
- Cylinder completed: The best results include 2 versions, with 4 other versions.
- Ball-screw completed: The best results include 2 versions, with 3 other versions.
- Aero: The best results include 2 versions, with 3 other versions.

The code is updated in GitLab.
