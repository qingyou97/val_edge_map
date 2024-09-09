def apply_transforms(self, img, gt):
                augmented = Image.fromarray(np.concatenate((np.array(img), np.array(gt)[:, :, np.newaxis]), axis=2))
                if self.data_transforms is not None:
                        augmented = self.data_transforms(augmented)
                
                augmented = np.array(augmented)
                img = Image.fromarray(augmented[:, :, :3])
                gt = Image.fromarray(augmented[:, :, 3])
                
                return img, gt
