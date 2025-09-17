function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M, point_N)
    close all;
    fig = figure('Visible', 'off');
    
    A = [0, 0, 0];
    B = [2, 0, 0];
    C = [0, 2, 0];
    A1 = [0, 0, 2];
    B1 = [1, 0, 2];
    C1 = [0, 1, 2];
    
    M = (B + C) / 2;
    N = (A + B) / 2;
    
    hold on;
    
    patch([A(1), M(1), C1(1)], [A(2), M(2), C1(2)], [A(3), M(3), C1(3)], 'm', 'FaceAlpha', 0.3);
    patch([A(1), C(1), C1(1), A1(1)], [A(2), C(2), C1(2), A1(2)], [A(3), C(3), C1(3), A1(3)], 'g', 'FaceAlpha', 0.2);
    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), C1(1)], [A1(2), C1(2)], [A1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    
    plot3([A1(1), N(1)], [A1(2), N(2)], [A1(3), N(3)], 'b--', 'LineWidth', 1.5);
    plot3([A(1), M(1)], [A(2), M(2)], [A(3), M(3)], 'r--', 'LineWidth', 1.5);
    plot3([M(1), C1(1)], [M(2), C1(2)], [M(3), C1(3)], 'r--', 'LineWidth', 1.5);
    
    all_points = {A, B, C, A1, B1, C1, M, N};

    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    
    text(A(1)-0.2, A(2)-0.2, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)-0.1, C(2)+0.1, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(A1(1)-0.2, A1(2)-0.2, A1(3)+0.1, point_A1, 'FontSize', 12, 'FontWeight', 'bold');
    text(B1(1)+0.1, B1(2)-0.1, B1(3)+0.1, point_B1, 'FontSize', 12, 'FontWeight', 'bold');
    text(C1(1)-0.1, C1(2)+0.1, C1(3)+0.1, point_C1, 'FontSize', 12, 'FontWeight', 'bold');
    text(M(1), M(2)+0.1, M(3)-0.15, point_M, 'FontSize', 12, 'FontWeight', 'bold');
    text(N(1), N(2)-0.15, N(3), point_N, 'FontSize', 12, 'FontWeight', 'bold');
    
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

            camzoom(0.8);

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
    