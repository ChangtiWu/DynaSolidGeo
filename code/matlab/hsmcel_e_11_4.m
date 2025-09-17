function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D)
    close all;
    fig = figure('Visible', 'off');

    w = 3; l = 4;
    d = sqrt(w^2 + l^2);
    
    C = [0, 0, 0];
    A = [d, 0, 0];
    
    cosA_D = (d^2 + w^2 - l^2) / (2 * d * w);
    proj_D_on_AC = w * cosA_D;
    h_D = sqrt(w^2 - proj_D_on_AC^2);
    D = [proj_D_on_AC, -h_D, 0];

    cosA_B = (d^2 + l^2 - w^2) / (2 * d * l);
    proj_B_on_AC = l * cosA_B;
    h_B = sqrt(l^2 - proj_B_on_AC^2);
    B = [proj_B_on_AC, 0, h_B];
    
    F = [proj_D_on_AC, 0, 0];
    E = [proj_B_on_AC, 0, 0];
    
    hold on;
    
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k--', 'LineWidth', 2);
    plot3([D(1), F(1)], [D(2), F(2)], [D(3), F(3)], 'k--', 'LineWidth', 2);
    
    all_points_labels = {point_A, point_B, point_C, point_D};
    all_points_coords = {A, B, C, D};
    offsets = {[-0.3, 0.1, 0], [0, 0.2, 0.2], [0.3, 0.1, 0], [0, -0.2, -0.1]};

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
    