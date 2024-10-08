import cv2
import numpy as np
import matplotlib.pyplot as plt



def cal_magnitude_direction(image):

    # 使用Sobel算子计算梯度
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # 计算梯度强度和方向
    magnitude = cv2.magnitude(grad_x, grad_y)
    direction = cv2.phase(grad_x, grad_y, angleInDegrees=True) #参数 angleInDegrees 默认为false，即弧度，当置为true时，则输出为角度
    # print(np.unique(magnitude))
    print(f'magnitude shape:{magnitude.shape}')
    print(f'direction shape:{direction.shape}')


    # 保存
    # magnitude_save = np.uint8(np.clip(magnitude / magnitude.max() * 255, 0, 255))
    # cv2.imwrite('magnitude_pr.png',magnitude_save)
    

    # 绘制 Edge Magnitude 图像
    plt.figure(figsize=(6, 6))
    plt.title('Edge Magnitude')
    plt.imshow(magnitude, cmap='gray')
    plt.axis('off')
    plt.savefig('edge_magnitude.png', bbox_inches='tight')  # 保存 Edge Magnitude 图像
    plt.show()

    # 可视化梯度方向
    '''
    在这种可视化中，不同的颜色表示梯度方向的角度。
    1. 彩虹色映射：“hsv”（色调-饱和度-明度）映射通常用于表示角度。这意味着每种颜色代表一个特定的角度。例如：
       - 红色：0度（或360度）
       - 黄色：90度
       - 绿色：180度
       - 青色：270度
    
    2. 色调变化：色彩环上的颜色是按 angular 周期性分布的，当从0度变化到360度时，颜色从红色过渡到黄色、绿色、青色，最后回到红色。
    所以，通过这种可视化方式，你可以很直观地看出图像中每个点的梯度方向。
    '''
    # 绘制 Edge Direction 图像
    plt.figure(figsize=(6, 6))
    plt.title('Edge Direction')
    plt.imshow(direction, cmap='hsv')
    plt.axis('off')
    plt.savefig('edge_direction.png', bbox_inches='tight')  # 保存 Edge Direction 图像
    plt.show()

if __name__ == '__main__':
    # 读取图像并转换为灰度图
    image = cv2.imread(r'cast_def_0_2.jpeg', cv2.IMREAD_GRAYSCALE)
    cal_magnitude_direction(image)
