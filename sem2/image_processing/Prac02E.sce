//bit plane  slicing
clc, clear all;

B=imread('C:\Playground\msc_practical\sem2\image_processing\images\coins.png');

[r, c]=size (B);

for i=1:r

for j=1:c

MSB (i, j)=bitand (B (i, j), bin2dec ('10000000'));

LSB (i, j)=bitand (B (i,j), bin2dec ('00000001'));

Second (i, j)=bitand (B (i,j), bin2dec ('01000000'));

Third (i,j)=bitand (B (i,j), bin2dec ('00100000'));

Fourth (i, j)=bitand (B (i,j), bin2dec ('00010000'));

Fifth (i,j)=bitand (B(i,j), bin2dec ('00001000')); Sixth (i, j)=bitand (B (i,j), bin2dec ('00000100'));

Seventh (i, j)=bitand (B (i,j),bin2dec ('00000010'));

end

end

subplot (4,4,1); imshow (MSB); title("Bit Plane 7")

subplot (4,4,2); imshow (Second); title("Bit Plane 6")
