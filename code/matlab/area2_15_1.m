function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    
    xA = -2;    yA = -2;    zA = 0;
    xB = 2;     yB = -2;    zB = 0;
    xC = 2;     yC = 2;     zC = 0;
    xD = -2;    yD = 2;     zD = 0;
    
    
    xA1 = -1;   yA1 = -1;   zA1 = 4;
    xB1 = 1;    yB1 = -1;   zB1 = 4;
    xC1 = 1;    yC1 = 1;    zC1 = 4;
    xD1 = -1;   yD1 = 1;    zD1 = 4;
    
    
    xO = 0;     yO = 0;     zO = 0;    
    xO1 = 0;    yO1 = 0;    zO1 = 4;   
    
    

    hold on;    
    
    
    
    plot3([xA, xB], [yA, yB], [zA, zB], 'k-', 'LineWidth', 2);
    plot3([xB, xC], [yB, yC], [zB, zC], 'k-', 'LineWidth', 2);
    plot3([xC, xD], [yC, yD], [zC, zD], 'k-', 'LineWidth', 2);
    plot3([xD, xA], [yD, yA], [zD, zA], 'k-', 'LineWidth', 2);
    
    
    plot3([xA1, xB1], [yA1, yB1], [zA1, zB1], 'k-', 'LineWidth', 2);
    plot3([xB1, xC1], [yB1, yC1], [zB1, zC1], 'k-', 'LineWidth', 2);
    plot3([xC1, xD1], [yC1, yD1], [zC1, zD1], 'k-', 'LineWidth', 2);
    plot3([xD1, xA1], [yD1, yA1], [zD1, zA1], 'k-', 'LineWidth', 2);
    
    
    plot3([xA, xA1], [yA, yA1], [zA, zA1], 'k-', 'LineWidth', 2);
    plot3([xB, xB1], [yB, yB1], [zB, zB1], 'k-', 'LineWidth', 2);
    plot3([xC, xC1], [yC, yC1], [zC, zC1], 'k-', 'LineWidth', 2);
    plot3([xD, xD1], [yD, yD1], [zD, zD1], 'k-', 'LineWidth', 2);
    
    
    plot3([xO, xO1], [yO, yO1], [zO, zO1], 'k--', 'LineWidth', 1.5); 
    scatter3(0, 0, 0, 15, 'k', 'filled');
    scatter3(0, 0, 4, 15, 'k', 'filled');
    
    
    text(xA, yA, zA, point_A, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right');
    text(xB, yB, zB, point_B, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left');
    text(xC, yC, zC, point_C, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left');
    text(xD, yD, zD, point_D, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
    

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
    