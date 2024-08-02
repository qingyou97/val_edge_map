针对AERO数据集的飞机涡轮叶片，对于我们想要的边缘，dexined的检出能力更强，能检测出来很多我们需要的边缘。但是对于一些对比度较弱的边缘，还是检测的不多，但优于其他两个算法。
对于casting-product数据集，对于我们想要的边缘，dexined的检出能力更强，且检测的最多，pidinet明显噪声较多，BDCN检测出我们需要的边缘较少。
对于Industrial-Dataset下的round数据，对于我们想要的边缘，dexined的检出能力更强，且检测的最多，pidinet丢失了很多边缘，且检测的轮廓很粗。BDCN的检测边缘也粗，而且很多细节检测不到。
对于Industrial-Dataset下的square数据，对于我们想要的边缘，dexined的检出能力更强，且检测的最多，pidinet丢失了很多边缘，且检测的轮廓很粗。BDCN的检测边缘也粗，而且很多细节检测不到。
对于Industrial-Tools数据集下的ball-screw数据，对于我们想要的边缘，BDCN平衡了检出数量和噪声数量，pidinet的噪声过多，而dexined部分边缘并没有检测出来。
对于Industrial-Tools数据集下的valve数据，对于我们想要的边缘，dexined平衡了检出数量和噪声数量，bdcn和pidinet的边缘很模糊，且检出数量不够。
对于apple-company数据集下的Cylinder数据，对于我们想要的边缘，dexined平衡了检出数量和噪声数量，bdcn检出数量不够，pidinet有些地方很抽象。
对于apple-company数据集下的Croove数据，对于我们想要的边缘，pidinet检出数量最多，而dexined检测的数量不够，bdcn噪声太多。
对于apple-company数据集下的Ring数据，对于我们想要的边缘，dexined平衡了检出数量和噪声数量，pidinet的噪声也多，但bdcn噪声是最多的。
对于mvtec的bottle类别，三者都不太好，dexined检出的数量已经算最多的了。
1. For the AERO dataset of aircraft turbine blades, DexiNed has a stronger detection ability for the edges we want and can detect many of the edges we need. However, it still detects few low-contrast edges, but it is better than the other two algorithms.

2. For the casting-product dataset, DexiNed has a stronger detection ability for the edges we want and detects the most. PiDiNet has significantly more noise, and BDCN detects fewer edges we need.

3. For the round data in the Industrial-Dataset, DexiNed has a stronger detection ability for the edges we want and detects the most. PiDiNet loses many edges and detects very coarse contours. BDCN also detects coarse edges and misses many details.

4. For the square data in the Industrial-Dataset, DexiNed has a stronger detection ability for the edges we want and detects the most. PiDiNet loses many edges and detects very coarse contours. BDCN also detects coarse edges and misses many details.

5. For the ball-screw data in the Industrial-Tools dataset, BDCN balances the detection quantity and noise number. PiDiNet has too much noise, and DexiNed misses some edges.

6. For the valve data in the Industrial-Tools dataset, DexiNed balances the detection quantity and noise number. BDCN and PiDiNet have blurred edges and insufficient detection quantity.

7. For the Cylinder data in the apple-company dataset, DexiNed balances the detection quantity and noise number. BDCN has insufficient detection quantity, and PiDiNet is abstract in some places.

8. For the Croove data in the apple-company dataset, PiDiNet detects the most, but DexiNed does not detect enough, and BDCN has too much noise.

9. For the Ring data in the apple-company dataset, DexiNed balances the detection quantity and noise number. PiDiNet also has much noise, and BDCN has the most noise.

10. For the bottle category of mvtec, all three are not very good, but DexiNed detects the most.
