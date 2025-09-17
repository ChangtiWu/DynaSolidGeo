function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_P, point_Q, point_O)
    close all;
    fig = figure('Visible', 'off');

    R = 5;
    z_H = 3;
    r_base = sqrt(R^2 - z_H^2);

    O = [0, 0, 0];
    P = [0, 0, R];
    Q = [0, 0, -R];
    H = [0, 0, z_H];
    D = [0, 0, (R + z_H) / 2];

    A = [r_base * cos(210 * pi / 180), r_base * sin(210 * pi / 180), z_H];
    B = [r_base * cos(-30 * pi / 180), r_base * sin(-30 * pi / 180), z_H];
    C = [r_base * cos(90 * pi / 180), r_base * sin(90 * pi / 180), z_H];

    hold on;

    t = linspace(0, 2 * pi, 200);
    plot3(R * cos(t), R * sin(t), zeros(size(t)), 'k-', 'LineWidth', 1.0);

    plot3([A(1), B(1), C(1), A(1)], [A(2), B(2), C(2), A(2)], [A(3), B(3), C(3), A(3)], 'k--', 'LineWidth', 1.0);

    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k--');
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k--');
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k--');
    
    plot3([Q(1), A(1)], [Q(2), A(2)], [Q(3), A(3)], 'k--');
    plot3([Q(1), B(1)], [Q(2), B(2)], [Q(3), B(3)], 'k--');
    plot3([Q(1), C(1)], [Q(2), C(2)], [Q(3), C(3)], 'k--');

    plot3([P(1), Q(1)], [P(2), Q(2)], [P(3), Q(3)], 'k--');
    
    plot3([H(1), A(1)], [H(2), A(2)], [H(3), A(3)], 'k--');
    plot3([H(1), B(1)], [H(2), B(2)], [H(3), B(3)], 'k--');
    plot3([H(1), C(1)], [H(2), C(2)], [H(3), C(3)], 'k--');
    
    all_points = [P; Q; A; B; C; O; H; D];
    scatter3(all_points(:,1), all_points(:,2), all_points(:,3), 50, 'k', 'filled');
    
    text(P(1), P(2), P(3) + 0.3, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(Q(1), Q(2), Q(3) - 0.6, point_Q, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1) - 0.5, A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1) + 0.3, B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2) + 0.4, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(O(1) + 0.3, O(2), O(3), point_O, 'FontSize', 14, 'FontWeight', 'bold');
   

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
    