clear all;

img = imread("C:\Playground\msc_practical\sem2\image_processing\images\lena_dark.png")
img = imnoise(img, "salt & pepper", 0.001)
//img = imnoise(img, "gaussian", 0.001)
subplot(1,2,1)
imshow(img)
title("noisy image")

img2 = imadd(img, 50)
subplot(1,2,2)
imshow(img2)
title("Smooth image after performing image addition")

