1. Confirm interpolation method after resizing to see if resizing thickens edge and causes gt edge loss.
Conclusion: Checked my code, default is bicubic interpolation, which thickens edges. PIDInet code previously set threshold to 0.1, filtering out some values. Lowered PIDInet threshold to prevent this issue. Switched to nearest neighbor interpolation, which keeps edge thickness at 1 but causes discontinuity in edges. Decided to stick with bicubic interpolation (`order=3`), re-binarized greyscale values through post-processing.
2. Re-trained PIDInet and BDCN with images scaled to 512x512. Trials include training with a single image, and randomly with 2/3/5/7/9/11 images, and all 100 images. PIDInet re-trained on the BIPEDv2 dataset.
Conclusion: As of this morning, PIDInet has trained extensively on the large BIPED dataset; only two small metal datasets remain. Similarly, BDCN also only has two small metal datasets left.
3. Finished training scripts for three settings in dexined: training with a single image, 2/3/5/7/9/11 images, and all 100 images to see different effects.
Conclusion: This morning, checked Wang Chao's machine. Dexined nearly done training the first dataset. Suppose dexined performs inference and auto-saves model in the same path after each model training, slowing things down.

Today's Plan:
4. Forecast results and metrics for bdcn and pidinet.
5. TEED inference under three cases: training with 1 image, training with 2/3/5/7/9/11 images, and training all 100 images.
6. Study how TEED fusion module is improved.
