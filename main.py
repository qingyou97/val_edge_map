import sys
import cv2 as cv
import os


def main(img_folder, save_path):
     ddepth = cv.CV_16S
     kernel_size = 3

     if not os.path.exists(save_path):
          os.makedirs(save_path,exist_ok=True)

     img_list = os.listdir(img_folder)

     for img in img_list:
          img_path = os.path.join(img_folder, img)

          src = cv.imread(img_path, cv.IMREAD_COLOR) # Load an image

          if src is None:
               print('Error opening image')
               print('Program Arguments: [image_name -- default lena.jpg]')
               return -1


          # Remove noise by blurring with a Gaussian filter
          src = cv.GaussianBlur(src, (3, 3), 0)

          # Convert the image to grayscale
          src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

          # Apply Laplace function
          dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)

          # converting back to uint8
          abs_dst = cv.convertScaleAbs(dst)
          abs_dst = 255 - abs_dst
          name = img.split('.')[0]
          cv.imwrite(os.path.join(save_path, f'{name}.png'), abs_dst)
     print('计算完成')
     return 0
if __name__ == "__main__":
     img_folder = r'E:\DexiNed-master\data'
     save_path = r'result/laplacian'
     main(img_folder, save_path )
