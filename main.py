1. Previous experiments tested a learning rate of 0.001.
Conclusion: Both the old model (upsampling first, then concat, then conv) and the new model (UNet decoder style) fit the GT after adding BN and ReLU after conv. In the old model, though it also had sum12345, the architecture was not well designed, causing poor results. In the new model, sum12345 outperformed sum234, but both models showed poor generalization on other images.

2. Tried using Wideresnet to replace BDCN as input for new features.
Conclusion: Completed extracting the Wideresnet architecture, using the official torch API instead of GitHub code. Extraction followed Han's three-layer method, with outputs [1, 256, 128, 128], [1, 512, 64, 64], and [1, 1024, 32, 32]. Training code is finished, similar to BDCN's pipeline. Used only Wideresnet for binary classification as it lacks output for GT interpolation needed for three-class classification. Plan to write and test the binary classification code today. If time permits, I will integrate BDCN and use BDCN’s fuse for three-class GT.

3. Deliverables table summary.
Conclusion: Completed. Organized all deliverables from MTG and JIRA in chronological order, including JIRA links, deliverable paths, task descriptions, and conclusions.
