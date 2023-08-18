clc;
clear all;
figure;
a=imread('C:\Playground\msc_practical\sem2\image_processing\images\seed.tif')
subplot(1,2,1)
imshow(a)
title('Low Contrast Image')
subplot(1,2,2)
h2=imhist(a)
plot(h2)

figure;
a=imread('C:\Playground\msc_practical\sem2\image_processing\images\seed.tif')
a=a+100;
subplot(1,2,1)
imshow(a)
title('Bright Image')
subplot(1,2,2)
h3=imhist(a)
plot(h3)

figure;
a=imread("C:\Playground\msc_practical\sem2\image_processing\images\seed.tif")
a=a-80
subplot(1,2,1)
imshow(a)
title("Dark Image")
subplot(1,2,2)
h4=imhist(a)
plot(h4)

figure;
a=imread("C:\Playground\msc_practical\sem2\image_processing\images\seed.tif")
mmin=min(a(:))
mmax=max(a(:))
lmin=0
lmax=255

a1=(a-mmin)*((lmax-lmin)/(mmax-mmin))+lmin
subplot(1,2,1)
imshow(a1)
title("High Contract Image")
subplot(1,2,2)
h5=imhist(a1)
plot(h5)
