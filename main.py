import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def non_max_suppression_extended(magnitude, angle):
    M, N = magnitude.shape
    Z = np.zeros((M, N), dtype=np.int32)
    angle = angle * 180.0 / np.pi
    angle[angle < 0] += 180

    # 延长线确定
    for i in range(1, M-1):
        for j in range(1, N-1):
            q, r = [], []
            x, y = i, j
            L = []

            dx, dy = None, None
                
            if (0 <= angle[x, y] < 22.5) or (157.5 <= angle[x, y] <= 180):
                dx, dy = 0, 1
            elif 22.5 <= angle[x, y] < 67.5:
                dx, dy = 1, 1
            elif 67.5 <= angle[x, y] < 112.5:
                dx, dy = 1, 0
            elif 112.5 <= angle[x, y] < 157.5:
                dx, dy = 1, -1

            if dx is not None:
                for direction in [-1, 1]:
                    for k in range(1, min(M, N)):
                        nx, ny = x + direction * k * dx, y + direction * k * dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if magnitude[nx, ny] == 0 and len(L) >= 5:
                                break
                            L.append((nx, ny, magnitude[nx, ny]))
                        
                if any(delV == 0 for _, _, delV in L[:5]) and any(delV == 0 for _, _, delV in L[-5:]):
                    bestL = [ij for ij, mu in [max(enumerate(L), key=lambda kts: kts[1][2])]]
                
                    Z[i, j] = max(m_value for (_, _, m_value) in L)
                
                    x_coords = [nx for nx, _, _ in L]
                    y_coords = [ny[:3] for nx, ny, mV in L]

                    # 插入标注与存为直方图
                    plt.figure()
                    plt.plot(y_coords, x_coords)
                    plt.xlabel("X axis pairing on bad frames")
                    plt.ylabel("Y axis Estimated M Values.")
                    plt.title("f(x, y) peaks observed.")
                
                    plt.show()
                        
    return Z
