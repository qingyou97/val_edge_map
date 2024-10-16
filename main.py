1. Overlay the known result with the original gt image to check if the wanted gt is extracted.
Conclusion: Some well-performing images show gt and results almost overlapping.
First, some images like B33 in datav3-cylinder page are affected by light at the bottom edge, causing some vertical fluctuation.
Second, some images like C33 in datav3-cylinder page show that AI detected other noise, exposing many unwanted edges, and this happens a lot.
Third, images like D33 in datav3-cylinder page show AI detecting two layers of edges; if the lower peak is larger, an unwanted edge is retained, and this can't be solved by proximity to the center.
Fourth, in images like E33 in datav3-cylinder page, wanted edges are blocked or obscured by light, leading AI to detect different edges, resulting in poor outcomes.

2. Evaluate the gt annotation and impact of lighting in the cylinder dataset.
Conclusion: Four layers of edges (from top to bottom as first to fourth). Edges 1, 2, and 4 meet the annotation requirements. The third edge has two layers, similar to casting, so I re-annotated the third edge.

3. Arrange and compare results from Han Xu's new version of dexined from yesterday.
Conclusion:
First, for the casting dataset, gt and my peak values are similar, but in some regions (like J15 in datav4-casting page), AI's results deviate from gt, which is more accurate. Solution attempts are in progress.
Second, the cylinder dataset hasn't improved, still showing excess edges.
Third, groove dataset shows that detected edges are generally good, but many edges are still missing, and some are fragmented.

4. Compare each result for the three datasets.
Conclusion: For casting, most images have fewer detected edges compared to before. By setting points closer to the inner diameter, detected edges are mostly on the inside now.
For the cylinder dataset, about half the images show reduced noise at the first and second boundary, though many needed edges are also filtered out.
Groove images show only a few improvements; most have fewer detected edges compared to before.

5. Explore if rule-based methods can solve some noise issues.
Conclusion: Applied opening operation with dilation and erosion to fill gaps. The preliminary result was ok, but full data operation showed poor outcomes with large white areas in many images.
