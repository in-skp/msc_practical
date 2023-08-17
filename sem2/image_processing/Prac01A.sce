clear all;
img = imread("C:\Playground\msc_practical\sem2\image_processing\images\lena.png")
imshow(img)
s = size(img)
disp("Dimension", s);
disp("height", s(1));
disp("width", s(2));
disp("No of channels", s(3));
disp(img(100,100))
img(100,100) = 50
disp(img(100,100))
