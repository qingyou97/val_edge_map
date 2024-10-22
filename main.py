1. Confirm the issues with casting and some breakpoints to determine if they are caused by AI or rule-based systems.
Conclusion: Two reasons. First, AI results are redundant, leading to many points being considered during the extension line calculation, including strong AI-passed areas closer to the center, which are retained. Second, rule-based detection picks the top two edge intensity points on the extension line as outside edges, while the inner edge is ranked third, thus picking the outer edge. File link:
2. Tried setting peak points to the top three for issue 1.
Conclusion: Improved individual images like 15 and 17, where previously the top 2 did not include the inner edge, causing edge deviation. Now selecting the nearest top 3 to the center improves such images. But AI result redundancy causing edge noise remains unsolved.
3. Polar coordinate algorithm has issues. Should use interpolation to expand the half-sector into a rectangle, enveloping the edge area. Missed points in the half-sector should be interpolated for results. Then average and select the maximum as the edge.
Conclusion: Testing in progress; found and fixing bugs.
4. v6 data: Apply a threshold on oneshot AI results to filter some noise and analyze results.
Conclusion: Chose a threshold of 75 to keep fewer disconnects while maintaining thicker edges. The current result is not better than the previous best 4 support merge version but is better than other versions, though noisier compared to the optimal 4 support merge.
