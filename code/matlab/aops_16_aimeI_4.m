function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D)
    close all;
    fig = figure('Visible', 'off');
    r = 1;
    h = 2;
    theta = linspace(0, 2*pi, 7);
    
    x = r * cos(theta);
    y = r * sin(theta);
    z1 = zeros(size(x));
    z2 = h * ones(size(x));

    hold on
    
    for i = 1:6
        x_rect = [x(i) x(i+1) x(i+1) x(i)];
        y_rect = [y(i) y(i+1) y(i+1) y(i)];
        z_rect = [z1(i) z1(i+1) z2(i+1) z2(i)];
        fill3(x_rect, y_rect, z_rect, [1 1 1], 'EdgeColor', 'k', 'FaceAlpha', 0.3, 'LineWidth', 2);
    end
    
    fill3(x, y, z1, [1 1 1], 'EdgeColor', 'k', 'FaceAlpha', 0.3, 'LineWidth', 2);
    fill3(x, y, z2, [1 1 1], 'EdgeColor', 'k', 'FaceAlpha', 0.3, 'LineWidth', 2);
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
    