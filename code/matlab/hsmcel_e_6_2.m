function visual(mode, azimuth, elevation, point_O, point_A, point_B, point_C, point_E, point_F, point_A1, point_B1, point_C1)
    close all;
    fig = figure('Visible', 'off');

    L = 2;
    O = [0, 0, 0];
    A = [L, 0, 0];
    B = [0, L, 0];
    C = [0, 0, L];

    E = (A + B) / 2;
    F = (A + C) / 2;
    
    A1 = [3/2, 0, 0];

    vec1 = E - A1;
    vec2 = F - A1;
    plane_normal = cross(vec1, vec2);
    
    plane_d = dot(plane_normal, A1);

    t_B1 = plane_d / dot(plane_normal, B);
    B1 = t_B1 * B;
    
    t_C1 = plane_d / dot(plane_normal, C);
    C1 = t_C1 * C;

    n1 = [0, 0, 1];
    n2 = plane_normal;
    
    cos_theta = abs(dot(n1, n2)) / (norm(n1) * norm(n2));
    
    tan_theta = sqrt(1 / cos_theta^2 - 1);

    hold on;

    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'b-', 'LineWidth', 2);
    fill3([A1(1), B1(1), C1(1)], [A1(2), B1(2), C1(2)], [A1(3), B1(3), C1(3)], 'b', 'FaceAlpha', 0.1);

    plot3([O(1), B1(1)], [O(2), B1(2)], [O(3), B1(3)], 'k-', 'LineWidth', 1.5);
    plot3([O(1), C1(1)], [O(2), C1(2)], [O(3), C1(3)], 'k-', 'LineWidth', 1.5);
    plot3([A1(1), C1(1)], [A1(2), C1(2)], [A1(3), C1(3)], 'k-', 'LineWidth', 1.5);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([O(1), A(1)], [O(2), A(2)], [O(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([O(1), B(1)], [O(2), B(2)], [O(3), B(3)], 'k--', 'LineWidth', 1);
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 1);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k--', 'LineWidth', 1);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k--', 'LineWidth', 1);

    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'r--', 'LineWidth', 1.2);

    all_points_coords = {O, A, B, C, A1, B1, C1, E, F};
    all_points_labels = {point_O, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_E, point_F};
    offsets = {[-0.3, -0.2, -0.2], [0.2, 0, 0], [0, 0.2, 0], [-0.2, -0.2, 0.2], ...
               [0.2, 0, 0], [0, 0.3, 0], [0, -0.3, 0.3], [0.2, 0.2, 0], [0.2, -0.2, 0]};

    for i = 1:length(all_points_coords)
        pt = all_points_coords{i};
        scatter3(pt(1), pt(2), pt(3), 30, 'k', 'filled');
        text(pt(1) + offsets{i}(1), pt(2) + offsets{i}(2), pt(3) + offsets{i}(3), ...
             all_points_labels{i}, 'FontSize', 12, 'FontWeight', 'bold', 'Interpreter', 'tex');
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
    