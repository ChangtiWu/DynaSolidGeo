function visual(mode, azimuth, elevation)
    close all;
    fig = figure('Visible', 'off');

    s = 2;
    h = 2;
    r = 0.5;

    theta_hex = (0:5) * pi / 3;
    hex_x = s * cos(theta_hex);
    hex_y = s * sin(theta_hex);

    bottom_hex_pts = [hex_x; hex_y; zeros(1, 6)];
    top_hex_pts = [hex_x; hex_y; ones(1, 6) * h];

    theta_circ = linspace(0, 2 * pi, 100);
    circ_x = r * cos(theta_circ);
    circ_y = r * sin(theta_circ);

    bottom_circ_pts = [circ_x; circ_y; zeros(1, 100)];
    top_circ_pts = [circ_x; circ_y; ones(1, 100) * h];

    hold on;

    plot3(top_hex_pts(1, [1:6, 1]), top_hex_pts(2, [1:6, 1]), top_hex_pts(3, [1:6, 1]), 'k-', 'LineWidth', 2);
    plot3(top_circ_pts(1, :), top_circ_pts(2, :), top_circ_pts(3, :), 'k-', 'LineWidth', 2);
    
    plot3(bottom_hex_pts(1, [1:6,1]), bottom_hex_pts(2, [1:6,1]), bottom_hex_pts(3, [1:6,1]), 'k-', 'LineWidth', 2);
    plot3(bottom_circ_pts(1, :), bottom_circ_pts(2, :), bottom_circ_pts(3, :), 'k-', 'LineWidth', 2);

    plot3([bottom_hex_pts(1, 1), top_hex_pts(1, 1)], [bottom_hex_pts(2, 1), top_hex_pts(2, 1)], [bottom_hex_pts(3, 1), top_hex_pts(3, 1)], 'k-', 'LineWidth', 2);
    plot3([bottom_hex_pts(1, 2), top_hex_pts(1, 2)], [bottom_hex_pts(2, 2), top_hex_pts(2, 2)], [bottom_hex_pts(3, 2), top_hex_pts(3, 2)], 'k-', 'LineWidth', 2);
    plot3([bottom_hex_pts(1, 6), top_hex_pts(1, 6)], [bottom_hex_pts(2, 6), top_hex_pts(2, 6)], [bottom_hex_pts(3, 6), top_hex_pts(3, 6)], 'k-', 'LineWidth', 2);
    plot3([bottom_hex_pts(1, 3), top_hex_pts(1, 3)], [bottom_hex_pts(2, 3), top_hex_pts(2, 3)], [bottom_hex_pts(3, 3), top_hex_pts(3, 3)], 'k-', 'LineWidth', 2);
    plot3([bottom_hex_pts(1, 4), top_hex_pts(1, 4)], [bottom_hex_pts(2, 4), top_hex_pts(2, 4)], [bottom_hex_pts(3, 4), top_hex_pts(3, 4)], 'k-', 'LineWidth', 2);
    plot3([bottom_hex_pts(1, 5), top_hex_pts(1, 5)], [bottom_hex_pts(2, 5), top_hex_pts(2, 5)], [bottom_hex_pts(3, 5), top_hex_pts(3, 5)], 'k-', 'LineWidth', 2);
    
    % Draw transparent cylinder without top and bottom faces
    [X,Y,Z] = cylinder(r, 50);
    Z = Z * h;
    % Only draw the side surface
    surf(X(:,1:end-1), Y(:,1:end-1), Z(:,1:end-1), 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'FaceColor', 'blue');
    
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
    