function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    P10 = [0, 0, 0];          
    P8  = [3, 0, 0];          
    P9  = [1.5, 2.598, 0];    
    
    
    P1  = [1.5, 0.866, 4];    
    
    
    P2 = (P1 + P10) / 2;      
    P3 = (P1 + P8) / 2;       
    P4 = (P1 + P9) / 2;       
    P5 = (P10 + P8) / 2;      
    P6 = (P9 + P8) / 2;       
    P7 = (P9 + P10) / 2;      
    
    

    hold on;
    
    
    plot3([P1(1), P10(1)], [P1(2), P10(2)], [P1(3), P10(3)], 'k-', 'LineWidth', 2); 
    plot3([P1(1), P8(1)],  [P1(2), P8(2)],  [P1(3), P8(3)],  'k-', 'LineWidth', 2); 
    plot3([P1(1), P9(1)],  [P1(2), P9(2)],  [P1(3), P9(3)],  'k-', 'LineWidth', 2); 
    plot3([P10(1), P8(1)], [P10(2), P8(2)], [P10(3), P8(3)], 'k-', 'LineWidth', 2); 
    plot3([P8(1), P9(1)],  [P8(2), P9(2)],  [P8(3), P9(3)],  'k-', 'LineWidth', 2); 
    plot3([P9(1), P10(1)], [P9(2), P10(2)], [P9(3), P10(3)], 'k-', 'LineWidth', 2); 
    
    
    
    
    
    
    
    
    
    
    
    
    
    all_points = [P1; P2; P8; P3; P4; P5; P6; P7];
    scatter3(all_points(:,1), all_points(:,2), all_points(:,3), 50, 'k', 'filled');
    
    
    text(P1(1), P1(2), P1(3), 'P_1', ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'center', 'FontSize', 14, 'FontWeight', 'bold');
    text(P10(1), P10(2), P10(3), 'P_{10}', ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    text(P8(1), P8(2), P8(3), 'P_8', ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(P9(1), P9(2), P9(3), 'P_9', ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(P2(1), P2(2), P2(3), 'P_2', ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    text(P3(1), P3(2), P3(3), 'P_3', ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(P4(1), P4(2), P4(3), 'P_4', ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(P5(1), P5(2), P5(3), 'P_5', ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'center', 'FontSize', 14, 'FontWeight', 'bold');
    text(P6(1), P6(2), P6(3), 'P_6', ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    text(P7(1), P7(2), P7(3), 'P_7', ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');


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
    