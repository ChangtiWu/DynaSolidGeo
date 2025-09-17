function visual(mode, azimuth, elevation, point_A, point_C, point_B, point_P)
    close all;
    fig = figure('Visible', 'off');

    ac_len = 2;
    bc_len = 3;
    ab_sq_final = 7;
    
    ab_len_orig = sqrt(ac_len^2 + bc_len^2);
    
    ap_len = ac_len^2 / ab_len_orig;
    bp_len = bc_len^2 / ab_len_orig;
    cp_len = (ac_len * bc_len) / ab_len_orig;
    
    cos_theta = (ab_sq_final - ap_len^2 - bp_len^2) / (2 * ap_len * bp_len);
    theta = acos(cos_theta);

    D = [0, 0, 0];
    C = [0, cp_len, 0];
    A = [ap_len, 0, 0];
    B = [-bp_len * cos(theta), 0, bp_len * sin(theta)];

    hold on;

    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'r--', 'LineWidth', 1.5);

    all_points_labels = {point_A, point_B, point_C};
    all_points_coords = {A, B, C};
    offsets = {[0.1, 0, 0.1], [-0.1, 0, 0.1], [0, 0.1, 0]};

    for i = 1:length(all_points_coords)
        pt = all_points_coords{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
        text(pt(1)+offsets{i}(1), pt(2)+offsets{i}(2), pt(3)+offsets{i}(3), ...
             all_points_labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
    end

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
    