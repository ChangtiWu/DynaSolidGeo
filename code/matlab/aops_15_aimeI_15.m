function visual(mode, azimuth, elevation, point_A, point_B, point_O)
    close all;
    fig = figure('Visible', 'off');
    r = 3;
    h = 6;
    n = 1000;
    dy = 2;
    
    theta_top = deg2rad(210);
    theta_bottom = deg2rad(150);
    x1 = r * cos(theta_top);  y1 = r * sin(theta_top);  z1 = h;
    x2 = r * cos(theta_bottom); y2 = r * sin(theta_bottom); z2 = 0;
    x3 = -x1; y3 = -y1; z3 = 0;
    x4 = -x2; y4 = -y2; z4 = h;
    
    p1 = [x1, y1, z1];
    p2 = [x2, y2, z2];
    p3 = [x3, y3, z3];
    v1 = p2 - p1;
    v2 = p3 - p1;
    normal = cross(v1, v2);
    a = normal(1); b = normal(2); c = normal(3);
    d = -dot(normal, p1);
    
    [theta, z] = meshgrid(linspace(0, 2*pi, n), linspace(0, h, n));
    x = r * cos(theta);
    y = r * sin(theta);
    
    plane_val = a * x + b * y + c * z + d;
    
    mask_up = plane_val >= 0;
    x_up = x; x_up(~mask_up) = NaN;
    y_up = y; y_up(~mask_up) = NaN;
    z_up = z; z_up(~mask_up) = NaN;
    

    surf(x_up, y_up - dy, z_up, 'FaceAlpha', 0.5, 'EdgeColor', 'none');
    hold on;
    
    plot3([x1 x2], [y1 y2] - dy, [z1 z2], 'k-', 'LineWidth', 2);
    plot3([x2 x3], [y2 y3] - dy, [z2 z3], 'k-', 'LineWidth', 2);
    plot3([x3 x4], [y3 y4] - dy, [z3 z4], 'k-', 'LineWidth', 2);
    plot3([x4 x1], [y4 y1] - dy, [z4 z1], 'k-', 'LineWidth', 2);
    
    fill3([x1 x2 x3 x4], [y1 y2 y3 y4] - dy, [z1 z2 z3 z4], ...
          [0.5 0.5 0.5], 'FaceAlpha', 0.2, 'EdgeColor', 'none');
    
    mask_down = plane_val <= 0;
    x_down = x; x_down(~mask_down) = NaN;
    y_down = y; y_down(~mask_down) = NaN;
    z_down = z; z_down(~mask_down) = NaN;
    
    surf(x_down, y_down + dy, z_down, 'FaceAlpha', 0.5, 'EdgeColor', 'none');
    
    plot3([x1 x2], [y1 y2] + dy, [z1 z2], 'k-', 'LineWidth', 2);
    plot3([x2 x3], [y2 y3] + dy, [z2 z3], 'k-', 'LineWidth', 2);
    plot3([x3 x4], [y3 y4] + dy, [z3 z4], 'k-', 'LineWidth', 2);
    plot3([x4 x1], [y4 y1] + dy, [z4 z1], 'k-', 'LineWidth', 2);
    
    fill3([x1 x2 x3 x4], [y1 y2 y3 y4] + dy, [z1 z2 z3 z4], ...
          [0.5 0.5 0.5], 'FaceAlpha', 0.2, 'EdgeColor', 'none');

    view(3);
    grid on;


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
    