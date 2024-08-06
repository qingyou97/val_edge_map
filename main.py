1. First, I used a single-annotated ground truth (gt) and a seven-annotated ground truth for experiments. Compared to DexiNed, PiDiNet overfits significantly. The gt doesn't affect PiDiNet's results; both overfit the flower contour without noise.
2. Second, I utilized a pre-trained model and a model pre-trained on 200 BSDS images. Both showed PiDiNet overfitting.
3. I used a single-annotated gt and increased the epochs to 200 (PiDiNet author originally used 12 epochs; DexiNed author used 20 epochs). DexiNed did not overfit, while PiDiNet's edges became finer with less noise.
4. I read some codes and forum posts. Summarized the training processes and unique features of DexiNed and PiDiNet. Some people mentioned that PiDiNet's CSAM and CDCM modules reduce noise impact.
5. I trained and inferred using the PiDiNet-l model (without CSAM and CDCM modules). It overfits slower than the standard PiDiNet but eventually still overfits the flower contour.
