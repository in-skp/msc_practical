clc; 
clear all;
p=imread('C:\Playground\msc_practical\sem2\image_processing\images\edge2.tif'); 
figure;
subplot(2,2,1); 
imshow(p); 
title('Original Image'); 
d=double(p); 
thresh=0.02; 
sigma=3; // 3, 5, 7
E=edge(d, 'canny', thresh, sigma); 
subplot(2,2,2);
imshow(E);
title('Canny Edge Image');
