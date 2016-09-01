function img_adjusted = adjust()
    
    img = imread('input.jpg');
    img_adjusted = zeros(size(img), 'uint8');

    for ch = 1:size(img,3)

        img_channel = img(:,:,ch);
    
        limits = stretchlim(img_channel, 0);
        
        img_adjusted(:,:,ch) = imadjust(img_channel, limits, []);

    end;

    imwrite(img_adjusted ,'output.jpg')

end

