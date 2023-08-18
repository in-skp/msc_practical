//thresholding
clc;
clear all;

p=imread("C:\Playground\msc_practical\sem2\image_processing\images\cameraman.tif")
subplot(1,2,1);
imshow(p);
title('Original Image');
k=55
z=double(p);
[row col]=size(p);
for i=1:1:row
for j=1:1:row
if ((z(i,j)>k))
z(i,j)=255;
else
z(i,j)=0;
end
end
end
subplot(1,2,2);
imshow(uint8(z));
title('Thresholding Image');
