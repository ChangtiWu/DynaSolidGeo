function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N, point_P)
    close all;
    fig = figure('Visible', 'off');

    L = 2;
    D = [0, 0, 0]; A = [L, 0, 0]; B = [L, L, 0]; C = [0, L, 0];
    D1 = [0, 0, L]; A1 = [L, 0, L]; B1 = [L, L, L]; C1 = [0, L, L];
    
    P = (D + D1) / 2;
    N = (C1 + D1) / 2;
    M = (B1 + C1) / 2;
    Q = (A + D) / 2;
    R = (A + B) / 2;
    S = (B + B1) / 2;

    plane_points = [M; N; P; Q; R; S];
    
    hold on;
    
    fill3(plane_points(:,1), plane_points(:,2), plane_points(:,3), 'c', 'FaceAlpha', 0.2);

    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([C1(1), D1(1)], [C1(2), D1(2)], [C1(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);

    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([D1(1), A1(1)], [D1(2), A1(2)], [D1(3), A1(3)], 'k-', 'LineWidth', 2);

    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k--', 'LineWidth', 2);
    plot3([N(1), P(1)], [N(2), P(2)], [N(3), P(3)], 'k--', 'LineWidth', 2);
    plot3([P(1), Q(1)], [P(2), Q(2)], [P(3), Q(3)], 'k--', 'LineWidth', 2);
    plot3([Q(1), R(1)], [Q(2), R(2)], [Q(3), R(3)], 'k--', 'LineWidth', 2);
    plot3([R(1), S(1)], [R(2), S(2)], [R(3), S(3)], 'k--', 'LineWidth', 2);
    plot3([S(1), M(1)], [S(2), M(2)], [S(3), M(3)], 'k--', 'LineWidth', 2);
    
    all_points = {A, B, C, D, A1, B1, C1, D1, P, N, M, Q, R, S};
    point_coords = cell2mat(all_points');
    scatter3(point_coords(:,1), point_coords(:,2), point_coords(:,3), 50, 'ko', 'filled');
    
    text(A(1)+0.1, A(2)-0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)+0.1, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)-0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)-0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1), A1(2), A1(3)+0.1, point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B1(1), B1(2), B1(3)+0.1, point_B1, 'FontSize', 14, 'FontWeight', 'bold');
    text(C1(1), C1(2), C1(3)+0.1, point_C1, 'FontSize', 14, 'FontWeight', 'bold');
    text(D1(1)-0.1, D1(2)-0.1, D1(3)+0.1, point_D1, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1)-0.2, P(2)-0.2, P(3), point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(N(1)-0.1, N(2)-0.2, N(3)+0.1, point_N, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)+0.1, M(2), M(3)+0.1, point_M, 'FontSize', 14, 'FontWeight', 'bold');
    

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
    