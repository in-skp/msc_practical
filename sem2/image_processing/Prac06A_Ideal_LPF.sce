img = imread("C:\Playground\msc_practical\sem2\image_processing\images\cameraman.tif")
a1=double(img)
r=size(a1,1);
c=size(a1,2);
d0=input('enter the cut off frequency (Radius):-'); 
for u=1:1:r
    for v=1:1:c
        d=(((u-(r/2))^2)+((v-(c/2))^2))^0.5;
        if d<=d0 
            h(u,v)=1;
        else
            h(u,v)=0;
        end 
    end 
end
b=fft2(a1); 
c=fftshift(b); 
new=h.*c;
new1=abs(ifft(new)); 
subplot(1,2,1); 
imshow(uint8(a1)); 
title('original image'); 
subplot(1,2,2); 
imshow(uint8(new1));
title(['Filtered Image with radius=',string(d0)]);
