 try:
        with open(os.path.join(self.root, self.imgList[index]), 'rb') as f:
            img = Image.open(f)
            img = img.convert('RGB')
            img = self.transform(img)
            filename = Path(self.imgList[index]).stem
            return img, filename
    except (IOError, UnidentifiedImageError):
        # 如果不是图片类型，或者打开文件失败，返回 None 表示跳过
        return None
