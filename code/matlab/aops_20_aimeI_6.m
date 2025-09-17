function visual(mode, azimuth, elevation)
    close all;
    fig = figure('Visible', 'off');
    r2 = 160 / 13;
    r = sqrt(r2);
    
    cos_a = (7/2) * sqrt(13 / 160);
    sin_a = sqrt(1 - cos_a^2);
    
    [u, v] = meshgrid(linspace(0, 2*pi, 50), linspace(0, pi, 50));
    x = r * cos(u) .* sin(v);
    y = r * sin(u) .* sin(v);
    z = r * cos(v);
    
    O1 = [0, 0, 0];
    O2 = [2*r*cos_a,  0, -2*r*sin_a];
    
    surf(x + O1(1), y + O1(2), z + O1(3), 'FaceAlpha', 0.5, 'EdgeColor', 'none');
    hold on
    surf(x + O2(1), y + O2(2), z + O2(3), 'FaceAlpha', 0.5, 'EdgeColor', 'none');
    
    [Xp, Yp] = meshgrid(linspace(-r, O2(1)+r, 50), linspace(-r, O2(2)+r, 50));
    Zp = zeros(size(Xp)) - r;
    surf(Xp, Yp, Zp, 'FaceColor', [0.8 0.8 0.8], 'FaceAlpha', 0.8, 'EdgeColor', 'none');
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
    