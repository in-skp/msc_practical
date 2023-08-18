clear all;
img = imread("C:\Playground\msc_practical\sem2\image_processing\images\Lena_dark.png");
subplot(2,3,1)
imshow(img)
title("original image")

img=double(img)

k1=(img*255)/64
subplot(2,2,2)
k1=uint8(k1)
imshow(uint8(k1))
title("Quantization 64")

k2=(img*255)/32
subplot(2,2,3)
k2=uint8(k2)
imshow(uint8(k2))
title("Quantization 32")

k3=(img*255)/16
subplot(2,2,4)
k3=uint8(k3)
imshow(uint8(k3))
title("Quantization 16")
