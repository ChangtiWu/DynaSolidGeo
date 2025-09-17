function visual(mode, azimuth, elevation, point_S, point_A, point_B, point_C, point_D, point_M, point_N)
    close all;
    fig = figure('Visible', 'off');

    a = 4;
    h = sqrt((2*a)^2 - (a*sqrt(2)/2)^2);
    
    A = [a/2, -a/2, 0];
    B = [a/2, a/2, 0];
    C = [-a/2, a/2, 0];
    D = [-a/2, -a/2, 0];
    S = [0, 0, h];
    
    N = (S + D) / 2;
    M = (S + B) / 2;
    
    P = C + N - B;
    Q = A + M - D;
    
    hold on;
    
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), C(1)], [S(2), C(2)], [S(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), D(1)], [S(2), D(2)], [S(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);

    plot3([B(1), N(1)], [B(2), N(2)], [B(3), N(3)], 'k--', 'LineWidth', 2);
    plot3([D(1), M(1)], [D(2), M(2)], [D(3), M(3)], 'k--', 'LineWidth', 2);
    
    all_points_labels = {point_S, point_A, point_B, point_C, point_D, point_M, point_N};
    all_points_coords = {S, A, B, C, D, M, N};
    offsets = {[0, 0.3, 0.3], [0.3, -0.3, 0], [0.3, 0.3, 0], [-0.3, 0.3, 0], [-0.3, -0.3, 0],...
               [-0.3, -0.3, 0.3], [0.3, 0.3, 0.3]};

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
    