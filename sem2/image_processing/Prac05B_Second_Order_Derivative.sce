figure;
img = imread("C:\Playground\msc_practical\sem2\image_processing\images\morpex.png")
subplot(1,2,1)
imshow(img)
title("Original image")
d = double(img)

v = [0 1 0;1 -4 1;0 1 0]
[r1,c1] = size(img)

for i=2:1:r1-1
    for j=2:1:c1-1
        newv(i,j) = (v(1) * d(i-1,j-1)) + (v(2) * d(i-1,j)) + (v(3) * d(i-1,j+1)) + (v(4) * d(i,j-1)) + (v(5) * d(i,j)) + (v(6) * d(i,j+1)) + (v(7) * d(i+1,j-1)) + (v(8) * d(i+1,j)) + (v(9) * d(i+1,j+1))
    end
end
subplot(1,2,2)
imshow(newv)
title("Image after applying laplasian filter")

