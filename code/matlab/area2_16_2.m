function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_T, point_M)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    xA = 0;    yA = 1;     zA = 0;   
    xB = 2;    yB = 0;     zB = 0;   
    xC = 2;    yC = 2;     zC = 0;   
    xD = 0;    yD = 3;     zD = 0;   
    
    
    xP = 1;    yP = 1;     zP = 3;   
    
    
    xM = 1;  yM = 1.75;     zM = 1.5; 
    xT = 1;    yT = 2.5;   zT = 0;   
    
    
    hold on;    

    
    
    
    plot3([xA, xP], [yA, yP], [zA, zP], 'k-', 'LineWidth', 2); 
    plot3([xB, xP], [yB, yP], [zB, zP], 'k-', 'LineWidth', 2); 
    plot3([xC, xP], [yC, yP], [zC, zP], 'k-', 'LineWidth', 2); 
    plot3([xD, xP], [yD, yP], [zD, zP], 'k-', 'LineWidth', 2); 
    
    
    plot3([xA, xB], [yA, yB], [zA, zB], 'k-', 'LineWidth', 2); 
    plot3([xB, xC], [yB, yC], [zB, zC], 'k-', 'LineWidth', 2); 
    plot3([xC, xD], [yC, yD], [zC, zD], 'k-', 'LineWidth', 2); 
    plot3([xD, xA], [yD, yA], [zD, zA], 'k-', 'LineWidth', 2); 
    
    
    plot3([xA, xM], [yA, yM], [zA, zM], 'k--', 'LineWidth', 1.5); 
    plot3([xB, xM], [yB, yM], [zB, zM], 'k--', 'LineWidth', 1.5); 
    plot3([xP, xT], [yP, yT], [zP, zT], 'k--', 'LineWidth', 1.5); 
    plot3([xA, xC], [yA, yC], [zA, zC], 'k--', 'LineWidth', 1.5); 
    
    
    text(xA, yA, zA, point_A, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xB, yB, zB, point_B, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xC, yC, zC, point_C, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xD, yD, zD, point_D, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xP, yP, zP, point_P, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xM, yM, zM, point_M, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xT, yT, zT, point_T, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');

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
    