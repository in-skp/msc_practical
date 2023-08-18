//Power law transformation
//s=c*r^gamma
itemp = imread("C:\Playground\msc_practical\sem2\image_processing\images\moon.tif")
r = double(itemp)/255   //normalize the image
c=1   // constant
gamma=3     //to make image dark take value of gamma > 1 to ma take value of gamma < 1
s = c*(r).^gamma;
subplot(2,2,1)
imshow(uint8(itemp))
title("Original image")
subplot(2,2,2)
imshow(s)
title("Powe Law transformed image")
