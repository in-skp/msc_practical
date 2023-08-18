img = imread("C:\Playground\msc_practical\sem2\image_processing\images\cameraman.tif")
a1 = double(img)
r=size(a1,1);
c=size(a1,2);
d0=input('Enter the cut-off frequency - (Radius):-'); 
for u=1:1:r
    for v=1:1:c
        d=(((u-(r/2))^2)+((v-(c/2))^2))^0.5
        h(u,v)=exp(-d*d/(2*d0*d0))
    end 
end
b=fft2(a1); 
c=fftshift(b); 
new=h.*c;
new1=abs(ifft(new)); 
subplot(1,2,1); 
imshow(img); 
title('Original Image'); 
subplot(1,2,2); 
imshow(uint8(new1));
title(['Filtered Image with radius = ',string(d0)]);
