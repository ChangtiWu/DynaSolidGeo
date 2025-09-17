function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D)
    close all;
    fig = figure('Visible', 'off');

    L = 1;
    h = L * sqrt(3) / 2;

    A = [-L/2, 0, 0];
    B = [L/2, 0, 0];
    C = [0, -h, 0];

    A1 = [-L/2, 0, L];
    B1 = [L/2, 0, L];
    C1 = [0, -h, L];
    
    d = 0.75;
    D = [-L/2, 0, d];
    
    hold on;

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 1.5);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 1.5);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 1.5);
    plot3([A1(1), C1(1)], [A1(2), C1(2)], [A1(3), C1(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 1.5);

    patch([D(1), B(1), C1(1)], [D(2), B(2), C1(2)], [D(3), B(3), C1(3)], [0.85, 0.85, 0.85], 'EdgeColor', 'k', 'LineWidth', 1.5);
    
    all_points = [A; B; C; A1; B1; C1; D];
    scatter3(all_points(:,1), all_points(:,2), all_points(:,3), 30, 'k', 'filled');
    
    text_offset = 0.08;
    text(A(1) - text_offset, A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1) + text_offset/2, B(2), B(3) - text_offset/2, point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2) - text_offset/2, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1) - text_offset, A1(2), A1(3), point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B1(1) + text_offset/2, B1(2), B1(3), point_B1, 'FontSize', 14, 'FontWeight', 'bold');
    text(C1(1) + text_offset/2, C1(2), C1(3), point_C1, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1) - text_offset, D(2), D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');

    axis equal;
    axis off;
    view(azimuth, elevation);
    
    set(gcf, 'Color', 'white');
    
    
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
    