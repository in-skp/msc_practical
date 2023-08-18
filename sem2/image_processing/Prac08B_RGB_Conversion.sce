figure;
img = imread("C:\Playground\msc_practical\sem2\image_processing\images\peppers.png")
subplot(2,2,1);
title("Original Image") 
imshow(img);
HSV=rgb2hsv(img);
subplot(2,2,2);
title("RGB2HSV") 
imshow(HSV);
CMY=imcomplement(img);
subplot(2,2,3); 
title("RGB2CMY") 
imshow(CMY);
