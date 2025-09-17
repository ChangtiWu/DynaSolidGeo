function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_P)





    close all;
    fig = figure('Visible', 'off');
    
    
    
    
    
    
    A = [0, 0, 0];
    B = [sqrt(3), 0, 0];        
    C = [sqrt(3)/3, 2*sqrt(6)/3, 0];  
    
    
    B1 = [sqrt(3), 0, 1];       
    A1 = [0, 0, 1];
    C1 = [sqrt(3)/3, 2*sqrt(6)/3, 1];
    
    
    t = 1/3;  
    P = [A1(1) + t*(B(1)-A1(1)), A1(2) + t*(B(2)-A1(2)), A1(3) + t*(B(3)-A1(3))];
    
    hold on;
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), A(1)], [C(2), A(2)], [C(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([C1(1), A1(1)], [C1(2), A1(2)], [C1(3), A1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C1(1)], [P(2), C1(2)], [P(3), C1(3)], 'k--', 'LineWidth', 2);
    
    
    plot3([A1(1), B(1)], [A1(2), B(2)], [A1(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([A1(1), P(1)], [A1(2), P(2)], [A1(3), P(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k--', 'LineWidth', 1.5);
    
    
    
    text(A(1), A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1), B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1), A1(2), A1(3), point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B1(1), B1(2), B1(3), point_B1, 'FontSize', 14, 'FontWeight', 'bold');
    text(C1(1), C1(2), C1(3), point_C1, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1), P(2), P(3), point_P, 'FontSize', 14, 'FontWeight', 'bold');
    
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
    