When I use pidinet to loop train on 20 images, I notice the third image has a size of 3000x4000, causing memory issues. GitHub mentions that pidinet cannot train on high-resolution images. I think resizing the image and gt to 512x512, similar to dexined preprocessing, might help. Do you think this is reasonable?
