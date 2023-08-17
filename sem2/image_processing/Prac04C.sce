clc;
clear all;
p1=imread("C:\Playground\msc_practical\sem2\image_processing\images\moon.tif")

pmax=imnoise(p1, 'salt & pepper', 0.002)
figure;
subplot(1,2,1)
imshow(pmax)
title("Noisy Image")

[r1, c1]=size(pmax)

for i=2:1:r1-1
    for j=2:1:c1-1
        a1=[pmax(i-1,j-1) pmax(i-1,j) pmax(i-1, j+1) pmax(i,j-1) pmax(i,j) pmax(i,j+1) pmax(i+1, j-1) pmax(i+1,j) pmax(i+1,j+1)]
        a2=max(max(a1))
        newmax(i,j)=a2
    end
end
subplot(1,2,2)
imshow(newmax)
title("Image after max filtering")
