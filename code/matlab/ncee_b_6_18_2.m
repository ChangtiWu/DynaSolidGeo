function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_C1, point_B1)
    close all;
    fig = figure('Visible', 'off');
    
    A = [2, 0, 0];
    B = [0, 0, 0];
    C = [-1, sqrt(3), 0];
    A1 = [2, 0, 4];
    B1 = [0, 0, 2];
    C1 = [-1, sqrt(3), 1];
    
    hold on;
    
    patch([A1(1) B1(1) C1(1)], [A1(2) B1(2) C1(2)], [A1(3) B1(3) C1(3)], 'c', 'FaceAlpha', 0.2);
    patch([A(1) B(1) B1(1) A1(1)], [A(2) B(2) B1(2) A1(2)], [A(3) B(3) B1(3) A1(3)], 'm', 'FaceAlpha', 0.2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), A(1)], [C(2), A(2)], [C(3), A(3)], 'k-', 'LineWidth', 1.5);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 1.5);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 1.5);
    plot3([C1(1), A1(1)], [C1(2), A1(2)], [C1(3), A1(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([A(1), B1(1)], [A(2), B1(2)], [A(3), B1(3)], 'r--', 'LineWidth', 2.5);
    plot3([A(1), C1(1)], [A(2), C1(2)], [A(3), C1(3)], 'b--', 'LineWidth', 2.5);
    
    all_points = {A, B, C, A1, B1, C1};
    labels = {point_A, point_B, point_C, point_A1, point_B1, point_C1};
    offset = 0.15;
    
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
        text(pt(1) + offset, pt(2) + offset, pt(3) + offset, labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
    end

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
    