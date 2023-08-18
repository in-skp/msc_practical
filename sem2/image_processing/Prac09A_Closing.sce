img = imread("C:\Playground\msc_practical\sem2\image_processing\images\circbw.tif")
d=img;
[r,c]=size(d); 
m=ones(3,3);
for i=2:1:r-1 
    for j=2:1:c-1
        new=[(m(1)*d(i-1,j-1)) (m(2)*d(i-1,j)) (m(3)*d(i-1,j+1)) (m(4)*d(i,j-1)) (m(5)*d(i,j)) (m(6)*d(i,j+1)) (m(7)*d(i+1,j-1)) (m(8)*d(i+1,j)) (m(9)*d(i+1,j+1))];
        A1(i,j)=max(new); 
        end
end 
d=A1;
[r,c]=size(d);
for i=2:1:r-1 
    for j=2:1:c-1
        new=[(m(1)*d(i-1,j-1)) (m(2)*d(i-1,j)) (m(3)*d(i-1,j+1)) (m(4)*d(i,j-1)) (m(5)*d(i,j)) (m(6)*d(i,j+1)) (m(7)*d(i+1,j-1)) (m(8)*d(i+1,j)) (m(9)*d(i+1,j+1))];
        A2(i,j)=min(new); 
    end
end
subplot(1,2,1); 
imshow(img); 
title('Original Image'); 
subplot(1,2,2); 
imshow(A2);
title('processed image - closing');
