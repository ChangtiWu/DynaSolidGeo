function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M)




    close all;
    fig = figure('Visible', 'off');
    
    
    
    A = [0, 0, 0];
    B = [1, 0, 0];      
    C = [1, 2, 0];      
    D = [0, 2, 0];
    A1 = [0, 0, sqrt(3)];   
    B1 = [1, 0, sqrt(3)];
    C1 = [1, 2, sqrt(3)];
    D1 = [0, 2, sqrt(3)];
    
    
    
    M = [1, 1, 0];      

    hold on;
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([C1(1), D1(1)], [C1(2), D1(2)], [C1(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([D1(1), A1(1)], [D1(2), A1(2)], [D1(3), A1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), M(1)], [A(2), M(2)], [A(3), M(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), A1(1)], [M(2), A1(2)], [M(3), A1(3)], 'k--', 'LineWidth', 1.5);
    plot3([A1(1), D(1)], [A1(2), D(2)], [A1(3), D(3)], 'k--', 'LineWidth', 2);
    
    
    plot3([B(1), M(1)], [B(2), M(2)], [B(3), M(3)], 'k--', 'LineWidth', 1.5);
    plot3([D(1), M(1)], [D(2), M(2)], [D(3), M(3)], 'k--', 'LineWidth', 1.5);
    
    
    
    
    text(A(1), A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1), B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1), D(2), D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1), A1(2), A1(3), point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B1(1), B1(2), B1(3), point_B1, 'FontSize', 14, 'FontWeight', 'bold');
    text(C1(1), C1(2), C1(3), point_C1, 'FontSize', 14, 'FontWeight', 'bold');
    text(D1(1), D1(2), D1(3), point_D1, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1), M(2), M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    
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
    