clear all;
img = imread("C:\Playground\msc_practical\sem2\image_processing\images\Lena_dark.png");
disp("size of original image", size(img));
subplot(3,3,1)
imshow(img)
title("original image")

j1=imresize(img, 0.8)
disp("size of resized image", size(j1))
subplot(3,3,2)
imshow(j1)
title("resized image 0.8")

j2=imresize(img, 0.7)
disp("size of resized image", size(j2))
subplot(3,3,3)
imshow(j2)
title("resized image 0.7")

j3=imresize(img, 0.6)
disp("size of resized image", size(j3))
subplot(3,3,4)
imshow(j3)
title("resized image 0.6")

j4=imresize(img, 0.5)
disp("size of resized image", size(j4))
subplot(3,3,6)
imshow(j4)
title("resized image 0.5")

j5=imresize(img, 0.4)
disp("size of resized image", size(j5))
subplot(3,3,7)
imshow(j5)
title("resized image 0.4")

j6=imresize(img, 0.3)
disp("size of resized image", size(j6))
subplot(3,3,8)
imshow(j6)
title("resized image 0.3")

j7=imresize(img, 0.2)
disp("size of resized image", size(j7))
subplot(3,3,5)
imshow(j7)
title("resized image 0.2")

j8=imresize(img, 0.1)
disp("size of resized image", size(j8))
subplot(3,3,9)
imshow(j8)
title("resized image 0.1")
