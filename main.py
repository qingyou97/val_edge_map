1. If Han Xu's multi-support results come out, continue testing and comparison analysis (test both pidinet and dexined).
Conclusion: For this version, the number detected is generally more than before, but each dataset has 3-5 images with obvious large noise areas. Need to resolve this.
For the bottle dataset, v5 has the fewest breaks, while previous results had many breaks.
For casting, the detected edges of this version are the same as V3 (dexined-1) and the edges are more continuous, but there are still individual images with noise that needs to be suppressed.
For cylinder: this version obviously suppressed a lot of noise between the first and second edges, and it also picked up many edges in areas with significant lighting influence, but there are issues with vertical oscillation.
For groove: this version has ten images with better results than V3 (dexined-1), detecting more edges, but for half of the images, V3 was better while v5 had average results.
For aero: clearly, most of the effects of V5 are better than all previous versions.

2. Test all other datasets.
Conclusion: I tested and organized all the data for V2 (pidinet) V3 (dexined-1) V4 (dexined-2).
For bottle, V3 (dexined-1) and V4 (dexined-2) both have five best results, performing similarly.
For casting, all results from V3 (dexined-1) are the best with fewer breaks and more orderly edges.
For cylinder, V4 (dexined-2) has 16 best points, performing the best with less noise and more continuous edges. V5 detects the most.
For groove, V3 (dexined-1) has 11 best points, and V4 (dexined-2) has 8. V3 (dexined-1) is the best with more detected edges. V5 detects the most.
For aero, V3 (dexined-1) has 3 best points, and V4 (dexined-2) has 9. V4 (dexined-2) performs the best with more detected edges. V5 detects the most.
For ball-screw: V2 (pidinet) has 4 best points, and V4 (dexined-2) has 14. V4 (dexined-2) is the best with more detected edges.

3. Perform morphological operations on V4 results to see if extra edges can be removed.
Conclusion: Currently found that using combined tests, first using a 2x2 structuring element (kernel) to perform erosion, then the same kernel to perform dilation, followed by median filtering with a 3x3 window to smooth the image and reduce noise. This effect achieves a balanced state for one image but will not completely filter out all noise. Morphological operations are suitable for already continuous edges with some extra unconnected noise like in casting, cylinder.
Bottle: not much change because bottle has less noise.
Casting: more continuous edges than the original V4.
Cylinder: noticeably less noise.
Groove: since this dataset has many needed edges with breaks, erosion also removed many needed edges while suppressing noise.
Aero: since this dataset has many needed edges with breaks, erosion also removed many needed edges while suppressing noise.
Ball-screw: V4 detection was already good; while taking the peak, a lot of thick noise was also removed. Hence, the effect did not improve, but some lines with gaps now have bigger gaps.
