function visual(mode, azimuth, elevation, point_V, point_A, point_B, point_C)
    close all;
    fig = figure('Visible', 'off');

    h = 3;
    a = 2;
    
    O = [0, 0, 0];
    P = [0, 0, h];
    r = a / sqrt(3);
    A = [r, 0, 0];
    B = [r*cos(2*pi/3), r*sin(2*pi/3), 0];
    C = [r*cos(4*pi/3), r*sin(4*pi/3), 0];
    D = (B + C) / 2;
    
    t = dot(B-A, P-A) / dot(P-A, P-A);
    E = A + t*(P-A);
    
    hold on;

    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([C(1), E(1)], [C(2), E(2)], [C(3), E(3)], 'k--', 'LineWidth', 1.5);

    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), O(1)], [P(2), O(2)], [P(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 1.5);

    all_points_labels = {point_A, point_B, point_C};
    all_points_coords = {A, B, C, D, E};
    offsets = {[0.2, 0, 0], [-0.1, 0.2, 0], [-0.1, -0.2, 0], ...
               [0, -0.2, 0], [0.1, 0, 0.1]};

    for i = 1:length(all_points_coords)
        pt = all_points_coords{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    for i = 1:(length(all_points_coords)-2)
        pt = all_points_coords{i};
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
    