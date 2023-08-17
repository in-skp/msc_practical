clc;
clear all;
img=imread("C:\Playground\msc_practical\sem2\image_processing\images\cameraman.tif")

c=255;//L-1
img2=c-img;//L-1-r

subplot(1,2,1)
imshow(img)
title("original image")

subplot(1,2,2)
imshow(img2)
title("image negative")
