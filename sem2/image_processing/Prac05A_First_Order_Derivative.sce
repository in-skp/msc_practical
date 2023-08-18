figure;
img = imread("C:\Playground\msc_practical\sem2\image_processing\images\morpex.png")
subplot(3,2,1)
imshow(img)
title("Original image")
d=double(img)

v=[1 0 -1;2 0 -2;1 0 -1]
h=[-1 -2 -1;0 0 0;1 2 1]
[r1,c1]=size(img)

for i=2:1:r1-1
    for j=2:1:c1-1
        newv(i,j) = (v(1) * d(i-1,j-1)) + (v(2) * d(i-1,j)) + (v(3) * d(i-1,j+1)) + (v(4) * d(i, j-1))  + (v(5) * d(i,j))   + (v(6) * d(i, j+1)) + (v(7) * d(i+1, j-1))+ (v(8) * d(i+1, j))+ (v(9) * d(i+1, j+1))
    end
end
subplot(3,2,2)
imshow(uint8(newv))
title("Image after applying vertical sobel operator")

for i=2:1:r1-1
    for j=2:1:c1-1
        newh(i,j)=(h(1)*d(i-1,j-1))+(h(2)*d(i-1,j))+(h(3)*d(i-1,j+1))+(h(4)*d(i,j-1))+(h(5)*d(i,j))+(h(6)*d(i,j+1))+(h(7)*d(i+1,j+1))+(h(8)*d(i+1,j))+(h(9)*d(i+1,j+1));
  end 
end
subplot(3,2,3); 
imshow(uint8(newh));
title("Image after applying horizontal sobel operator");

v1=[-1 0 1; -2 0 2; -1 0 1];
h1=[1 2 1; 0 0 0; -1 -2 -1];

for i=2:1:r1-1 
    for j=2:1:c1-1
        newv1(i,j)=(v1(1)*d(i-1,j-1))+(v1(2)*d(i-1,j))+(v1(3)*d(i-1,j+1))+(v1(4)*d(i,j-1))+(v1(5)*d(i,j))+(v1(6)*d(i,j+1))+(v1(7)*d(i+1,j+1))+(v1(8)*d(i+1,j))+(v1(9)*d(i+1,j+1));
    end 
end
subplot(3,2,4);
imshow(uint8(newv1));
title("Image after applying vertical sobel operator rotated 180 degree"); 

for i=2:1:r1-1
    for j=2:1:c1-1
        newh1(i,j)=(h1(1)*d(i-1,j-1))+(h1(2)*d(i-1,j))+(h1(3)*d(i-1,j+1))+(h1(4)*d(i,j-1))+(h1(5)*d(i,j))+(h1(6)*d(i,j+1))+(h1(7)*d(i+1,j+1))+(h1(8)*d(i+1,j))+(h1(9)*d(i+1,j+1));
    end 
end
subplot(3,2,5); 
imshow(uint8(newh1));
title("Image after applying horizontal sobel operator rotated 180 degree"); 

finalimg=uint8(newv) | uint8(newh) | uint8(newv1) | uint8(newh1);
subplot(3,2,6);
imshow(finalimg);
title("Final Image");

