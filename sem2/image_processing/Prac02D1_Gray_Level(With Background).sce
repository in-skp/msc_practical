//gray level slicing with background
clc;
clear all;

p=imread("C:\Playground\msc_practical\sem2\image_processing\images/cameraman.tif")
subplot(1,2,1);
imshow(p);
title('Original Image');
z=double(p);
[row col]=size(p);
for i=1:1:row
for j=1:1:row
if ((z(i,j)>50) && (z(i,j)<100))
z(i,j)=200;
else
z(i,j)=p(i,j);
end
end
end
subplot(1,2,2);
imshow(uint8(z));
title('Gray level slicing image with background');
