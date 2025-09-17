function visual(mode, azimuth, elevation, point_S, point_A, point_B, point_C, point_D, point_K, point_M, point_N)
    close all;
    fig = figure('Visible', 'off');

    w = 2; l = 2.5; h = 3;
    S = [0, 0, h];
    A = [-w, -l, 0]; B = [w, -l, 0]; C = [w, l, 0]; D = [-w, l, 0];

    K = (S + C) / 2;
    tm = 2/3; tn = 2/3; 
    M = S + tm * (B - S);
    N = S + tn * (D - S);

    hold on;

    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), C(1)], [S(2), C(2)], [S(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);

    plot3([S(1), D(1)], [S(2), D(2)], [S(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), M(1)], [A(2), M(2)], [A(3), M(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), K(1)], [M(2), K(2)], [M(3), K(3)], 'k--', 'LineWidth', 1.5);
    plot3([K(1), N(1)], [K(2), N(2)], [K(3), N(3)], 'k--', 'LineWidth', 1.5);
    plot3([N(1), A(1)], [N(2), A(2)], [N(3), A(3)], 'k--', 'LineWidth', 1.5);

    all_points = {S, A, B, C, D, K, M, N};
    point_coords = cell2mat(all_points');
    scatter3(point_coords(:,1), point_coords(:,2), point_coords(:,3), 50, 'ko', 'filled');

    text(S(1), S(2), S(3) + 0.1, point_S, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1) - 0.2, A(2) - 0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1) + 0.1, B(2) - 0.1, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1) + 0.2, C(2) + 0.2, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1) - 0.3, D(2) + 0.2, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(K(1) + 0.2, K(2) + 0.2, K(3), point_K, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1) + 0.2, M(2), M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    text(N(1) - 0.3, N(2), N(3), point_N, 'FontSize', 14, 'FontWeight', 'bold');

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
    