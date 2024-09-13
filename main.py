1. Combined wideresnet and bdcn, implemented inference code, considered fusion strategy, then passed through classifier to check results.
a. Today, I finished the inference code using three layers of features from Wideresnet as classifier inputs. I initially encountered out-of-memory errors, which were due to using hooks to extract Wideresnet features, causing memory to not be released. I switched to using the create_feature_extractor method from torchvision. Training and inference code are now complete.

b. I tested Wideresnet directly as a classifier. Results are in Excel sheet1, rows 4-5-6. It fitted well to training images but had poor generalization to other images. The edges of other images were discontinuous.

c. I then tried merging Wideresnet and BDCN using sum5 and trained the classifier. Results are in sheet1, rows 7-8-9-10-11. For single image training, the best result is in row 9 because I used a high contrast image, enhancing the model's generalization ability. I then trained with another image representing a different type in the dataset, and added dropout. The best result is in row 10, detecting the desired double circles, but with some edges not fully suppressed.
