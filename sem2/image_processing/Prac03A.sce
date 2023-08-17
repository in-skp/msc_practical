clc;
clear all;
a=imread("C:\Playground\msc_practical\sem2\image_processing\images\Lena_dark.png")
subplot(2,2,1)
imshow(a)
title("Original Image")
[r,c]=size(a)
h=zeros(1,256)
for i=1:r
    for j=1:c
        if(a(i,j)==0)
            a(i,j)=1
        end
        k=a(i,j)
        h(k)=h(k)+1
    end
end
subplot(2,2,2)
plot(h)
title("Histogram of the Image")
h1=imhist(a)
subplot(2,2,3)
plot(h1)
title("Histogram of the Image")
