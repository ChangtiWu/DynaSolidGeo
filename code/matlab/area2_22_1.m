function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    xA = 0;    yA = 0;     zA = 0;   
    xB = 2;    yB = 0;     zB = 0;   
    xC = 2;    yC = 2;     zC = 0;   
    xD = 0;    yD = 2;     zD = 0;   
    
    
    xA1 = 0;   yA1 = 0;    zA1 = 2;  
    xB1 = 2;   yB1 = 0;    zB1 = 2;  
    xC1 = 2;   yC1 = 2;    zC1 = 2;  
    xD1 = 0;   yD1 = 2;    zD1 = 2;  
    
    
    xM = 0;    yM = 1;     zM = 2;   
    xN = 2;    yN = 2;     zN = 0.8;   
    
    

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
    
    
    
    plot3([xA1, xM], [yA1, yM], [zA1, zM], 'k--', 'LineWidth', 1.5);
    plot3([xB1, xM], [yB1, yM], [zB1, zM], 'k-', 'LineWidth',2);
    
    
    plot3([xM, xN], [yM, yN], [zM, zN], 'k--', 'LineWidth', 1.5);
    plot3([xN, xD], [yN, yD], [zN, zD], 'k-', 'LineWidth', 2);
    plot3([xM, xB], [yM, yB], [zM, zB], 'k--', 'LineWidth', 1.5);
    
    plot3([xA1, xD1], [yA1, yD1], [zA1, zD1], 'k--', 'LineWidth', 1.5);
    
    
    
    text(xA, yA, zA, point_A, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xB, yB, zB, point_B, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xC, yC, zC, point_C, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xD, yD, zD, point_D, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    
    text(xA1, yA1, zA1, point_A1, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xB1, yB1, zB1, point_B1, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xC1, yC1, zC1, point_C1, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(xD1, yD1, zD1, point_D1, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    
    text(xM, yM, zM, point_M, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left','FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    

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
    