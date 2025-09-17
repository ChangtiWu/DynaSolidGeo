function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D)
    close all;
    fig = figure('Visible', 'off');
    hold on;

    A = [0, 0, 0];
    B = [1, 0, 2];
    C = [0, 1, 4];
    D = [1, 1, 6];

    s = norm(B - A);
    normal = cross(B - A, C - A);
    unit_normal = normal / norm(normal);

    E = A + s * unit_normal;
    F = B + s * unit_normal;
    G = C + s * unit_normal;
    H = D + s * unit_normal;

    faces = {
        [A; B; D; C];
        [E; F; H; G];
        [A; B; F; E];
        [B; D; H; F];
        [D; C; G; H];
        [C; A; E; G];
    };

    for i = 1:length(faces)
        patch('Vertices', faces{i}, 'Faces', [1 2 3 4], ...
              'FaceColor', 'none', 'FaceAlpha', 0.3, 'EdgeColor', 'k');
    end
    vertices = {point_A, A; point_D, H; ...
                point_B, E; point_C, D};

    for i = 1:size(vertices, 1)
        name = vertices{i, 1};
        coord = vertices{i, 2};
        text(coord(1), coord(2), coord(3), ['  ' name], ...
            'FontSize', 12, 'FontWeight', 'bold', ...
            'Color', 'black');
    end

    z_plane_x = [-2 2 2 -2];
    z_plane_y = [-2 -2 2 2];
    fill3(z_plane_x, z_plane_y, zeros(1, 4), [0.8 0.8 0.8], ...
        'FaceAlpha', 0.2, 'EdgeColor', 'red');

    axis equal;
    axis off;
    set(gca, 'XDir', 'reverse');
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
    