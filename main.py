When adjusting the learning rate on my old classifier network, I found that setting it to 0.001 was still not good. So I wanted to verify whether the issue was with the network or my training method. Without changing the training method, I added two new conv layers and two new bn layers to the network this time. I found that the training results fit the gt well. The images from column L are basically consistent with the gt (with some noise).
