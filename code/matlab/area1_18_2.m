function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_P)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    xB = 0;    yB = 0;     zB = 0;   
    xC = 3;    yC = 0;     zC = 0;   
    xD = 0;    yD = 2;     zD = 0;   
    xE = 2;    yE = 2;     zE = 0;   
    xP = 1.5;  yP = 1;     zP = 3;   
    
    

    hold on;

    
    
    plot3([xB, xP], [yB, yP], [zB, zP], 'k-', 'LineWidth', 2); 
    plot3([xC, xP], [yC, yP], [zC, zP], 'k-', 'LineWidth', 2); 
    plot3([xB, xC], [yB, yC], [zB, zC], 'k-', 'LineWidth', 2); 
    plot3([xB, xE], [yB, yE], [zB, zE], 'k--', 'LineWidth', 1.5); 
    plot3([xB, xD], [yB, yD], [zB, zD], 'k-', 'LineWidth', 2); 
    
    plot3([xD, xP], [yD, yP], [zD, zP], 'k-', 'LineWidth', 2); 
    plot3([xE, xP], [yE, yP], [zE, zP], 'k-', 'LineWidth', 2); 
    plot3([xD, xE], [yD, yE], [zD, zE], 'k-', 'LineWidth', 2); 
    plot3([xC, xE], [yC, yE], [zC, zE], 'k-', 'LineWidth', 2); 
    
    
    text(xB, yB, zB, point_B, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xC, yC, zC, point_C, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xD-0.2, yD, zD, point_D, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xE+0.2, yE, zE, point_E, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xP, yP, zP+0.2, point_P, ...
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

        camzoom(0.6);

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
    