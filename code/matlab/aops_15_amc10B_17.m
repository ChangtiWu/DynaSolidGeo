function visual(mode, azimuth, elevation, point_A)
    close all;
    fig = figure('Visible', 'off');
    L = 4;
    W = 5;
    H = 3;
    
    A = [0 0 0];
    B = [L 0 0];
    C = [L W 0];
    D = [0 W 0];
    E = [0 0 H];
    F = [L 0 H];
    G = [L W H];
    H_ = [0 W H];
    
    vertices = [A; B; C; D; E; F; G; H_];
    
    faces = [
        1 2 3 4;
        5 6 7 8;
        1 2 6 5;
        2 3 7 6;
        3 4 8 7;
        4 1 5 8
    ];
    
    hold on
    
    for i = 1:size(faces,1)
        fill3(vertices(faces(i,:),1), vertices(faces(i,:),2), vertices(faces(i,:),3), ...
              [1 1 1], 'FaceAlpha', 0.3, 'EdgeColor', 'k', 'LineWidth', 2);
    end
    mid_AB = (A + B)/2;
    mid_AD = (A + D)/2;
    mid_AE = (A + E)/2;

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
    