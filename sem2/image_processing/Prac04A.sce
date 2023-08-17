clc
clear all
a=imread("C:\Playground\msc_practical\sem2\image_processing\images\moon.tif")
c=imnoise(a, 'gaussian', 0.003)
d=double(a)
b=d

[r1,c1]=size(a)
for i=2:r1-1
    for j=2:c1-1
        a1=d(i-1,j-1)+d(i-1,j)+d(i-1,j+1)+d(i,j-1)+d(i,j)+d(i,j+1)+d(i+1,j-1)+d(i+1,j)+d(i+1,j+1);
        b(i,j)=a1*(1/9)
    end
end
subplot(1,3,1)
imshow(a)
title("Original Image")
subplot(1,3,2)
imshow(c)
title("Noisy Image")
subplot(1,3,3)
imshow(uint8(b))
title("Filtered Image")

