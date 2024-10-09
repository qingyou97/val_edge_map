def plot_peak_coordinates(peak_coordinates, ix, iy):
    # 按照x坐标从小到大排序
    peak_coordinates.sort(key=lambda coord: coord[1])

    coords = [(i[1], i[0]) for i in peak_coordinates]  # x, y
    intensities = [i[2] for i in peak_coordinates]

    plt.figure()
    if len(peak_coordinates) > 1:
        max_intensity_index = np.argmax(intensities)
        plt.plot(range(len(coords)), intensities, marker='o')
        plt.text(max_intensity_index, intensities[max_intensity_index], f"Max: {coords[max_intensity_index]}", fontsize=12, color='red')
    
        plt.title('Intensity Profile')
        plt.xlabel('Pixel Coordinates')
        plt.ylabel('Intensity Value')

        # 设置横轴刻度
        plt.xticks(range(len(coords)), [f"({c[0]},{c[1]})" for c in coords], rotation=45)

        plt.grid()
        plt.show()
