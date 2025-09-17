function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_S)
    close all;
    fig = figure('Visible', 'off');

    A = [0, 0, 0];
    B = [1, 0, 0];
    D = [0, 0.5, 0];
    C = [1, 1, 0];
    S = [0, 0, 1];
    
    hold on;
    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), C(1)], [S(2), C(2)], [S(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), D(1)], [S(2), D(2)], [S(3), D(3)], 'k-', 'LineWidth', 2);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 2);
    plot3([A(1), S(1)], [A(2), S(2)], [A(3), S(3)], 'k--', 'LineWidth', 2);

    arrow_len = 1.2;
    quiver3(0, 0, 0, arrow_len, 0, 0, 'k', 'LineWidth', 1.5, 'MaxHeadSize', 0.3);
    quiver3(0, 0, 0, 0, arrow_len, 0, 'k', 'LineWidth', 1.5, 'MaxHeadSize', 0.3);
    quiver3(0, 0, 0, 0, 0, arrow_len, 'k', 'LineWidth', 1.5, 'MaxHeadSize', 0.3);
    text(arrow_len+0.1, 0, 0, 'x', 'FontSize', 12, 'FontWeight', 'bold');
    text(0, arrow_len+0.1, 0, 'y', 'FontSize', 12, 'FontWeight', 'bold');
    text(0, 0, arrow_len+0.1, 'z', 'FontSize', 12, 'FontWeight', 'bold');

    all_points_labels = {point_A, point_B, point_C, point_D, point_S};
    all_points_coords = {A, B, C, D, S};
    offsets = {[-0.1, -0.1, 0], [0.1, -0.1, 0], [0.1, 0.1, 0], [-0.1, 0.1, 0], [0, 0.1, 0.1]};

    for i = 1:length(all_points_coords)
        pt = all_points_coords{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
        text(pt(1)+offsets{i}(1), pt(2)+offsets{i}(2), pt(3)+offsets{i}(3), ...
             all_points_labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
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

        camzoom(0.9);

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
    