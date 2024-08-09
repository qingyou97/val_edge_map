from torchvision import transforms

   transform = transforms.Compose([
       transforms.Resize((512, 512)),  # 统一尺寸
       transforms.ToTensor()
   ])

   dataset = CustomDataset(transform=transform)
