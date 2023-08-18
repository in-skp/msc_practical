clc;
clear all;

img1 = imread("C:\Playground\msc_practical\sem2\image_processing\images\tool1.png")
img2 = imread("C:\Playground\msc_practical\sem2\image_processing\images\tool2.png")
subplot(2,2,1)
imshow(img1)
title("Image 1")
subplot(2,2,2)
imshow(img2)
title("Image 2")
dif = imabsdiff(img1, img2)
subplot(2,2,3)
imshow(dif)
title("Image 3 = Image1 - Image2")
