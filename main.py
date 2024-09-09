 self.data_transforms = transforms.Compose([
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomRotation(15),
                    transforms.RandomResizedCrop((self.crop_size, self.crop_size)) if crop_size else transforms.Resize((224, 224)),
                    transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.05)
                ])
