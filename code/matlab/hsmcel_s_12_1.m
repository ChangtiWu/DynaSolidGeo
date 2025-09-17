function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q)
    close all;
    fig = figure('Visible', 'off');

    L = 1;
    D = [0,0,0]; A = [L,0,0]; B = [L,L,0]; C = [0,L,0];
    D1 = [0,0,L]; A1 = [L,0,L]; B1 = [L,L,L]; C1 = [0,L,L];
    
    O_p = (A1+C1)/2; r_p = L/2;
    O_q = (A+C1)/2; r_q = norm(A-O_q);

    hold on;
    
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([C1(1), D1(1)], [C1(2), D1(2)], [C1(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([D1(1), A1(1)], [D1(2), A1(2)], [D1(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), B(1)], [C(2), B(2)], [C(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k-', 'LineWidth', 2);

    t = linspace(0, 2*pi, 100);
    p_circle = O_p + r_p * [cos(t); sin(t); zeros(size(t))]';
    fill3(p_circle(:,1), p_circle(:,2), p_circle(:,3), 'b', 'FaceAlpha', 0.3, 'EdgeColor', 'k', 'LineStyle', '--', 'LineWidth', 1.5);
    
    normal_q = cross(B-A, C1-A);
    [u, ~] = qr([normal_q', randn(3,1), randn(3,1)]);
    q_circle = O_q + r_q * (u(:,2)*cos(t) + u(:,3)*sin(t))';
    fill3(q_circle(:,1), q_circle(:,2), q_circle(:,3), 'r', 'FaceAlpha', 0.3, 'EdgeColor', 'k', 'LineStyle', '--', 'LineWidth', 1.5);

    all_points = {A, B, C, D, A1, B1, C1, D1, O_p, O_q};
    point_coords = cell2mat(all_points');
    scatter3(point_coords(:,1), point_coords(:,2), point_coords(:,3), 50, 'ko', 'filled');
    
    text(A(1)+0.05, A(2)-0.1, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.05, B(2)+0.05, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)-0.1, C(2)+0.05, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)-0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1)+0.05, A1(2)-0.1, A1(3), point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B1(1)+0.05, B1(2)+0.05, B1(3), point_B1, 'FontSize', 14, 'FontWeight', 'bold');
    text(C1(1)-0.1, C1(2)+0.05, C1(3), point_C1, 'FontSize', 14, 'FontWeight', 'bold');
    text(D1(1)-0.1, D1(2)-0.1, D1(3), point_D1, 'FontSize', 14, 'FontWeight', 'bold');
    text(O_p(1), O_p(2)-0.15, O_p(3), point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(O_q(1)+0.05, O_q(2)-0.1, O_q(3), point_Q, 'FontSize', 14, 'FontWeight', 'bold');

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
    