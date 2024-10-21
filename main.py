10-21 Morning Meeting 10:00-10:40:
Duan: 
1. Confirm the cause of the breakpoint issues in casting. Is it AI or rule-based? 
2. The polar plot algorithm has problems. Should use interpolation to expand the semi-sector into a rectangle. The semi-sector covers the edge area I need. The points not in the semi-sector should be calculated using interpolation. For example, if they are floating pixel coordinates, interpolation should be used to get the result. Then average them, and take the maximum value as the edge.
3. Set a threshold on the oneshot AI results to filter out some noise points. Analyze the results afterward.

Han Xu:
1. Check the images after training to see if there are also breakpoint issues. Judge the results of these four supports.
2. Need to improve the merge section to ensure that edges detected by zeroshot can also be output after merging.
3. If the merge still doesn't work, increase capacity and add more layers to see the effect.
4. Create a simple plan for the dcama experiment list and dexined merge, and discuss it tomorrow.
