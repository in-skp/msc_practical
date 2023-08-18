// First order derivative filter - Sobel Operator
//prewitt
clc; clear all;
p=imread('C:\Playground\msc_practical\sem2\image_processing\images\edge2.tif'); 
figure;
subplot(2,2,1);
imshow(p); title('Original Image');
v1=[1,0,-1;2, 0, -2;1, 0, -1]; //x-direction
h1=[-1, -2, -1; 0, 0 ,0; 1, 2, 1 ]; //y-direction
v2=[-1, 0, 1; -2, 0, 2; -1, 0, 1];
h2=[1, 2, 1; 0, 0, 0; -1, -2 ,-1];
gv1=abs(imfilter(double(p),v1));
gh2=abs(imfilter(double(p),h2));
gh1=abs(imfilter(double(p),h1)); 
subplot(2,2,2);
imshow(gh1); 
title('horizontal Edges');
gv2=abs(imfilter(double(p),v2)); 
subplot(2,2,3);
imshow(gv2); 
title('vertical2 Edges');
finaledge=gh1+gv2+gh2+gv1; 
subplot(2,2,4); 
imshow(finaledge); 
title('Final Image');
