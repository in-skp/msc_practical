clc;
clear all;
img = imread("C:\Playground\msc_practical\sem2\image_processing\images\peppers.png")
R=img(:,:,1);
G=img(:,:,2);
B=img(:,:,3);
subplot(2,2,1); 
imshow(img); 
title("Original Image"); 
subplot(2,2,2); 
imshow(R);
title("Red Component Image");
subplot(2,2,3);
imshow(G);
title("Green Component Image"); 
subplot(2,2,4);
imshow(B);
title("Blue Component Image");
figure;
//Get histValues for each channel 
[yR,x]= imhist(R);
[yG,x]= imhist(G);
[yB,x]= imhist(B);
//Plot them together in one plotx 
plot(x,yR,x,yG,x,yB,"LineWidth",2); 
xlabel("RGB Intensity");
ylabel("No of Pixels");
set(gca(),"grid",[1,1])
