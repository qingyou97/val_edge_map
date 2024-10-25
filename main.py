1. Optimized the algorithm for finding circular contours. Locating inner and outer contours of two rings based on AI results. Occasionally, some AI results aren't fully contained. Now, checking points not within the rings and expanding rings based on point position and distance until all AI regions are covered. Time optimization also achieved, previously each calculation recomputed sector and rectangular mapping and saved images, causing delay. Now achieving under 1-second per image.

2. Changed threshold filtering method to two types. First method uses high-to-low thresholds, filtering first point above 300; if not within AI region, filtering first point above 200, and so on.
Conclusion: Some images show AI regions with extra steep gradients and points close to the circle center. This leads to retention of the first threshold point over 300. Reference to lines 26-29 in the xx file.

3. Changed to another threshold filtering method. Set thresholds at 1000, 800, 600, and so on. Filter peak points based on these thresholds. Select the first peak point within the AI region as the result.
Conclusion: Good effect, suppresses some convex parts of AI regions. However, the edge results of other images are not as smooth as the previous version. Both versions have issues; if the ring services are not well detected, three out of twenty images are affected. Reference to lines 22-25 in the xx file.

4. Also checked the groove dataset.
Conclusion: Just wrote the image bounding box retrieval. Considered different edge mapping directions for horizontal and vertical. ROI areas found in horizontal and vertical directions. Vertical pixel stacks located using templates that scan the image to find pixels similar to the template, detecting vertical pixel stacks. Contour detection draws bounding rectangles as ROI areas. For horizontal pixel stacks, subtract the vertical stacks from the image, then locate the largest horizontal bounding rectangles as ROI areas.
