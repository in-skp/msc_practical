clc;
clear all;
p1=imread("C:\Playground\msc_practical\sem2\image_processing\images\moon.tif")

pmin=imnoise(p1, 'salt & pepper', 0.002)
figure;
subplot(1,2,1)
imshow(pmin)
title("Noisy Image")

[r1, c1]=size(pmin)

for i=2:1:r1-1
    for j=2:1:c1-1
        a1=[pmin(i-1,j-1) pmin(i-1,j) pmin(i-1, j+1) pmin(i,j-1) pmin(i,j) pmin(i,j+1) pmin(i+1, j-1) pmin(i+1,j) pmin(i+1,j+1)]
        a2=min(min(a1))
        newmin(i,j)=a2
    end
end
subplot(1,2,2)
imshow(newmin)
title("Image after min filtering")
