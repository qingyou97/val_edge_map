1. Casting dataset - Currently retaining the peak points closest to the inner diameter. Further fine-tuning is needed.
Conclusion: By changing the gradient towards the center, the result improved, filtering out more external edges. Refer to row 41 in the sheet.

2. Casting dataset - Using light and dark alternation algorithm to determine retention of edges.
Conclusion: Two optimization methods were used, but the overall result still found the logic based on the center to be the best.
- The first customized version used the light and dark alternation algorithm to select points after two peak points. The left side of the image only retained left light-right dark, while the right side retained left dark-right light, and similar logic was needed for up and down. A brightness threshold was set to avoid filtering out gaps. The result was average, with many discontinuities and the threshold being hard to control. A high threshold caused necessary edges to break, while a low threshold exposed other gap edges.
- The second version judged which edge had a dark pixel closer to the center and a bright pixel farther away. This was similar to the previous version but optimized the point selection logic, resulting in similar unsatisfactory effects. The threshold remained challenging to control.

3. Test other datasets like groove and cylinder, as the current approach works well for casting. Further fine-tuning can wait.
Conclusion: Tested groove and cylinder using dexined results.
- Cylinder:
  - First version: directly took the point with the largest peak, still resulting in two layers of edges.
  - Second version: Found center using an ellipse in the image, retained edges closer to the center.
  - Third version: Noticed the second layer from the top was often filtered out. Adjusted the threshold to 4, improving retention of the second layer. However, assigning original pixel values during final image rendering caused some previously apparent edges to vanish.
  - Fourth version: Saved all peak points as 255, resulting in more continuous edges.
  - Fifth version: Improved magnitude using the original image, retaining required regions' magnitudes based on AI results and setting others to zero. This gave the best result but edge selection under lighting conditions remains unsolved.
- Groove:
  - First version: direct two peak points. Result was poor with severe discontinuities.
  - Second version: Improved magnitude using the original image as done with cylinder. Resulted in better performance but sometimes introduced extra noise due to noisy AI results.

4. Re-labeled 20 casting images. All images are 224*224 with white single-pixel edges on a black background, ensuring only inner edges are present.
Conclusion: Refer to the new-gt page in the document.
