1025 Morning Meeting from 10:00 to 10:40:

Duan:
1. Further optimize the algorithm for finding the four contours of the ring.
2. Fix ROI in the groove dataset first, then test top and bottom edges to check detection effect.

Han:
3. Compare dCAMa results, organize previous and today's results for comparison.
4. Add instnorm after each conv, test the effect.
5. Usually, clip + tanh causes instability; suggest switching to sigmoid.
6. Add continuity constraints to the edge, converting them to loss.
