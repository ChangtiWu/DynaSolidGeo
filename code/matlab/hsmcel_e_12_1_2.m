function visual(mode, azimuth, elevation, point_S, point_A, point_B, point_P, point_Q, point_O, point_E, point_F)
    close all;
    fig = figure('Visible', 'off');

    r = 2;
    h = r; 
    
    O = [0, 0, 0];
    S = [0, 0, h];
    A = [-r, 0, 0];
    B = [r, 0, 0];
    P = [r * cosd(150), r * sind(150), 0];
    Q = [r * cosd(60), r * sind(60), 0];
    E = (S + P) / 2;

    v_SQ = Q - S;
    F = S + dot(O - S, v_SQ) / dot(v_SQ, v_SQ) * v_SQ;

    hold on;

    [X, Y, Z] = cylinder([r, 0], 50);
    Z = Z * h;
    surf(X, Y, Z, 'FaceAlpha', 0.1, 'EdgeColor', 'none', 'FaceColor', [0.8 0.8 0.8]);

    t = linspace(0, 2*pi, 100);
    plot3(r*cos(t), r*sin(t), zeros(size(t)), 'k-', 'LineWidth', 2);
    
    plot3([A(1) S(1) B(1)], [A(2) S(2) B(2)], [A(3) S(3) B(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([O(1) P(1)], [O(2) P(2)], [O(3) P(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1) Q(1)], [O(2) Q(2)], [O(3) Q(3)], 'k--', 'LineWidth', 1.5);
    plot3([S(1) P(1)], [S(2) P(2)], [S(3) P(3)], 'k--', 'LineWidth', 1.5);
    plot3([S(1) Q(1)], [S(2) Q(2)], [S(3) Q(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), O(1)], [E(2), O(2)], [E(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), F(1)], [O(2), F(2)], [O(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 1.5);
    
    all_points = {S, O, A, B, P, Q, E, F};
    point_coords = cell2mat(all_points');
    scatter3(point_coords(:,1), point_coords(:,2), point_coords(:,3), 50, 'ko', 'filled');

    text(S(1), S(2), S(3) + 0.1, point_S, 'FontSize', 14, 'FontWeight', 'bold');
    text(O(1), O(2)-0.1, O(3), point_O, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1) - 0.3, A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1) + 0.1, B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1) - 0.2, P(2) + 0.2, P(3), point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(Q(1) + 0.2, Q(2) + 0.1, Q(3), point_Q, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1) - 0.3, E(2), E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1) + 0.2, F(2), F(3) - 0.2, point_F, 'FontSize', 14, 'FontWeight', 'bold');
    
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
    