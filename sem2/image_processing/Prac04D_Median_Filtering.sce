clc;
clear all;
p1=imread("C:\Playground\msc_practical\sem2\image_processing\images\moon.tif")

pmed=imnoise(p1, 'salt & pepper', 0.002)
figure;
subplot(1,2,1)
imshow(pmed)
title("Noisy Image")

[r1, c1]=size(pmed)

for i=2:1:r1-1
    for j=2:1:c1-1
        a1=[pmed(i-1,j-1) pmed(i-1,j) pmed(i-1, j+1) pmed(i,j-1) pmed(i,j) pmed(i,j+1) pmed(i+1, j-1) pmed(i+1,j) pmed(i+1,j+1)]
        a2=gsort(a1)
        med=a2(5)
        newmed(i,j)=med
    end
end
subplot(1,2,2)
imshow(newmed)
title("Image after low pass median filtering")
