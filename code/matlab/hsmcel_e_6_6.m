function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_P, point_Q, point_M)
    close all;
    fig = figure('Visible', 'off');

    a = 5;
    theta_deg = 30;
    theta_rad = deg2rad(theta_deg);

    mh_len = a / sqrt(1 + sin(theta_rad)^2);

    M = [0, 0, 0];
    H = [mh_len * cos(theta_rad), mh_len * sin(theta_rad), 0];
    P = [H(1), H(2), H(2)];
    mq_len = mh_len * 1.8;
    Q = [mq_len * cos(theta_rad), mq_len * sin(theta_rad), 0];
    N = [H(1), 0, 0];

    plane_half_width = 5;
    plane_half_depth = 5;
    
    B = [-plane_half_width, 0, 0];
    C = [plane_half_width, 0, 0];
    
    A_corner = [C(1), plane_half_depth, plane_half_depth];
    B_corner_up = [B(1), plane_half_depth, plane_half_depth];

    D_corner = [C(1), plane_half_depth, 0];
    B_corner_down = [B(1), plane_half_depth, 0];

    hold on;

    % Fill plane ABC with semi-transparent color
    fill3([B_corner_up(1), A_corner(1), C(1), B(1)], ...
          [B_corner_up(2), A_corner(2), C(2), B(2)], ...
          [B_corner_up(3), A_corner(3), C(3), B(3)], ...
          'b', 'FaceAlpha', 0.3);

    % Fill plane DCB with semi-transparent color
    fill3([D_corner(1), C(1), B(1), B_corner_down(1)], ...
          [D_corner(2), C(2), B(2), B_corner_down(2)], ...
          [D_corner(3), C(3), B(3), B_corner_down(3)], ...
          'r', 'FaceAlpha', 0.3);

    plot3([B_corner_up(1), A_corner(1)], [B_corner_up(2), A_corner(2)], [B_corner_up(3), A_corner(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B_corner_up(1)], [B(2), B_corner_up(2)], [B(3), B_corner_up(3)], 'k-', 'LineWidth', 2);

    plot3([B_corner_down(1), D_corner(1)], [B_corner_down(2), D_corner(2)], [B_corner_down(3), D_corner(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B_corner_down(1)], [B(2), B_corner_down(2)], [B(3), B_corner_down(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D_corner(1)], [C(2), D_corner(2)], [C(3), D_corner(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), A_corner(1)], [C(2), A_corner(2)], [C(3), A_corner(3)], 'k-', 'LineWidth', 2);
    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([P(1), M(1)], [P(2), M(2)], [P(3), M(3)], 'k-', 'LineWidth', 2);
    plot3([M(1), Q(1)], [M(2), Q(2)], [M(3), Q(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), Q(1)], [P(2), Q(2)], [P(3), Q(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), H(1)], [P(2), H(2)], [P(3), H(3)], 'k-', 'LineWidth', 2);
    
    plot3([H(1), N(1)], [H(2), N(2)], [H(3), N(3)], 'k--', 'LineWidth', 2);
    plot3([M(1), H(1)], [M(2), H(2)], [M(3), H(3)], 'k--', 'LineWidth', 2);

    all_points_mat = [P; Q; M; N; H; B; C];
    scatter3(all_points_mat(:,1), all_points_mat(:,2), all_points_mat(:,3), 25, 'k', 'filled');

    text_offset = 0.2;
    text(A_corner(1) - 1, A_corner(2), A_corner(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1) - text_offset*2, B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1) + text_offset, C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D_corner(1), D_corner(2) - text_offset, D_corner(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1), P(2), P(3) + text_offset, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(Q(1) + text_offset, Q(2) + text_offset, Q(3) + text_offset, point_Q, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1) - text_offset, M(2) - text_offset, M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    
    
    axis equal;
    axis off;
    view(azimuth, elevation);
    
    set(gcf, 'Color', 'white');
    
    
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
    