function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M, point_N, point_P, point_E, point_F)
    close all;
    fig = figure('Visible', 'off');

    side_len = 6;
    prism_height = sqrt(24);
    
    A = [0, 0, 0];
    altitude_len = side_len * sqrt(3) / 2;
    B = [-side_len/2, altitude_len, 0];
    C = [side_len/2, altitude_len, 0];

    A1 = [0, 0, prism_height];
    B1 = [-side_len/2, altitude_len, prism_height];
    C1 = [side_len/2, altitude_len, prism_height];

    M = (B + C) / 2;
    N = (B1 + C1) / 2;
    O = (A1 + B1 + C1) / 3;
    
    dist_PM = prism_height / tan(pi/3);
    ratio_AP = (altitude_len - dist_PM) / altitude_len;
    P = ratio_AP * M;
    
    E = ratio_AP * B;
    F = ratio_AP * C;

    hold on;

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), C1(1)], [A1(2), C1(2)], [A1(3), C1(3)], 'k-', 'LineWidth', 2);
    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    
    plot3([A1(1), N(1)], [A1(2), N(2)], [A1(3), N(3)], 'k--', 'LineWidth', 1.5);
    plot3([B1(1), E(1)], [B1(2), E(2)], [B1(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([F(1), C1(1)], [F(2), C1(2)], [F(3), C1(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), M(1)], [A(2), M(2)], [A(3), M(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k--', 'LineWidth', 1.5);
    plot3([C1(1), N(1)], [C1(2), N(2)], [C1(3), N(3)], 'k--', 'LineWidth', 1.5);
    plot3([B1(1), C(1)], [B1(2), C(2)], [B1(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 1.5);
    
    all_points = {A, B, C, A1, B1, C1, M, N, O, P, E, F};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
    end
    
    text(A(1), A(2)-0.3, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)-1, B(2), B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2), C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(A1(1)-0.5, A1(2)-0.3, A1(3), point_A1, 'FontSize', 12, 'FontWeight', 'bold');
    text(B1(1)-1, B1(2), B1(3), point_B1, 'FontSize', 12, 'FontWeight', 'bold');
    text(C1(1)+0.2, C1(2), C1(3), point_C1, 'FontSize', 12, 'FontWeight', 'bold');
    text(M(1), M(2)+0.4, M(3), point_M, 'FontSize', 12, 'FontWeight', 'bold');
    text(N(1)+0.2, N(2)+0.4, N(3), point_N, 'FontSize', 12, 'FontWeight', 'bold');
    
    text(P(1), P(2)-0.5, P(3), point_P, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1)-0.5, E(2)-0.2, E(3), point_E, 'FontSize', 12, 'FontWeight', 'bold');
    text(F(1)+0.2, F(2)-0.2, F(3), point_F, 'FontSize', 12, 'FontWeight', 'bold');
    
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
    