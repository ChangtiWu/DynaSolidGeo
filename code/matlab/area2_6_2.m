function visual(mode, azimuth, elevation, point_B, point_C, point_D, point_E, point_A, point_F, point_A1)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    xB = 0;    yB = 0;     zB = 0;   
    xC = 3;    yC = 0;     zC = 0;   
    xD = 2;    yD = 2;     zD = 0;   
    xE = 0;    yE = 2;     zE = 0;   
    
    
    xF = (xC + xD) / 2;  
    yF = (yC + yD) / 2;  
    zF = (zC + zD) / 2;   
    
    xA1 = xF; yA1 = 1;    zA1 = 3;  
    
    

    hold on;
    
    
    
    plot3([xB, xC], [yB, yC], [zB, zC], 'k-', 'LineWidth', 2);  
    plot3([xC, xD], [yC, yD], [zC, zD], 'k-', 'LineWidth', 2);  
    plot3([xD, xE], [yD, yE], [zD, zE], 'k-', 'LineWidth', 2);  
    plot3([xE, xB], [yE, yB], [zE, zB], 'k-', 'LineWidth', 2);  
    
    
    plot3([xA1, xB], [yA1, yB], [zA1, zB], 'k-', 'LineWidth', 2);  
    plot3([xA1, xC], [yA1, yC], [zA1, zC], 'k-', 'LineWidth', 2);  
    plot3([xA1, xD], [yA1, yD], [zA1, zD], 'k-', 'LineWidth', 2);  
    plot3([xA1, xE], [yA1, yE], [zA1, zE], 'k-', 'LineWidth', 2);  
    
    
    plot3([xA1, xF], [yA1, yF], [zA1, zF], 'k-', 'LineWidth', 2);  
    
    
    
    text(xB, yB, zB, point_B, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xC, yC, zC-0.2, point_C, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xD, yD+0.2, zD-0.2, point_D, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xE, yE, zE, point_E, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xF, yF, zF-0.2, point_F, ...
        'VerticalAlignment', 'middle', 'HorizontalAlignment', 'center','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xA1, yA1, zA1+0.2, point_A1, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'center','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');







    axis equal;
    axis off;
    view(azimuth, elevation);
    
    set(gca, 'Color', 'white');
    set(gcf, 'Color', 'white');
    set(gcf, 'ToolBar', 'none');
    set(gcf, 'MenuBar', 'none');
    
    
    set(gcf, 'Position', [100, 100, 1024, 1024]);

    
    
    if mode == 0
        img_dir = fullfile('..', '..', 'data', 'images');
        if ~exist(img_dir, 'dir')
            mkdir(img_dir);
        end
        img_path = fullfile(img_dir, [mfilename, '.png']);
        frame = getframe(gcf);

        imwrite(frame.cdata, img_path);
        fprintf('Image saved as: %s \n', img_path);
    elseif mode == 1
        vid_dir = fullfile('..', '..', 'data', 'videos');
        if ~exist(vid_dir, 'dir')
            mkdir(vid_dir);
        end
        vid_path = fullfile(vid_dir, [mfilename, '.mp4']);
        video = VideoWriter(vid_path, 'MPEG-4');
        video.FrameRate = 24;
        open(video);

        set(gca, 'CameraViewAngleMode', 'manual');
        set(gca, 'CameraPositionMode', 'manual');
        set(gca, 'CameraTargetMode', 'manual');

        camzoom(0.7);

        for angle = (azimuth+3):3:(azimuth+360)
            view(angle, elevation);
            frame = getframe(gcf);
            writeVideo(video, frame);
        end

        close(video);
        fprintf('Video saved as: %s \n', vid_path);
    end
    hold off;
    close(fig);
end
    