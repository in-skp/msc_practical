//gray level slicing without background
clc;
clear all;
p=imread ("C:\Playground\msc_practical\sem2\image_processing\images\Lena_dark.png");
z=double (p) ;

[row col]=size(z);

for i=1:1:row
for j=1:1:col
if(z(i,j)>50)&&(z(i,j)<100)
z(i,j)=220;
else
z(i,j)=20;
end
end
end
subplot (1,2,1);
imshow (p) ;
title ('Original-Image');
subplot (1,2,2);
imshow (uint8(z)) ;
title ('Gray level slicing without background');
