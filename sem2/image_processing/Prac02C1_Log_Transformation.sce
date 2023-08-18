//log transformation
clc;
clear all;

img2=imread("C:\Playground\msc_practical\sem2\image_processing\images\log.tif")

c=15
s=c* log( 1 + double(img2));
o=uint8(s)
subplot(2,2,1)
imshow(img2)
title("original image")
subplot(2,2,2)
imshow(o)
title("Log transformed image")
