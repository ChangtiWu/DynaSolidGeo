function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_M, point_N)
    close all;
    fig = figure('Visible', 'off');

    ab_len = 5;
    dc_len = 3;
    ef_len = 1;
    angle_deg = 60;
    dihedral_deg = 60;

    h1 = (ab_len - dc_len) * tand(angle_deg);
    h2 = (dc_len - ef_len) * tand(angle_deg);

    A = [-2, h1, 0];
    B = [3, h1, 0];
    C = [3, 0, 0];
    D = [0, 0, 0];
    
    y_rot = cosd(dihedral_deg);
    z_rot = sind(dihedral_deg);

    E = [2, h2 * y_rot, h2 * z_rot];
    F = [3, h2 * y_rot, h2 * z_rot];

    M = (A + E) / 2;
    N = (B + C) / 2;

    hold on;

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 1.5);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 1.5);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 1.5);
    plot3([F(1), C(1)], [F(2), C(2)], [F(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([F(1), B(1)], [F(2), B(2)], [F(3), B(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k-', 'LineWidth', 1.5);
    plot3([D(1), M(1)], [D(2), M(2)], [D(3), M(3)], 'k--', 'LineWidth', 1);


    all_points_mat = [A; B; C; D; E; F; M; N];
    labels = {point_A, point_B, point_C, point_D, point_E, point_F, point_M, point_N};
    scatter3(all_points_mat(:,1), all_points_mat(:,2), all_points_mat(:,3), 30, 'k', 'filled');
    
    offset = 0.4;
    text(A(1) - offset, A(2), A(3), labels{1}, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1) + offset, B(2), B(3), labels{2}, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1) + offset, C(2) - offset, C(3), labels{3}, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1) - offset, D(2) - offset, D(3), labels{4}, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1) - offset, E(2) + offset, E(3), labels{5}, 'FontSize', 12, 'FontWeight', 'bold');
    text(F(1) + offset, F(2), F(3), labels{6}, 'FontSize', 12, 'FontWeight', 'bold');
    text(M(1) - offset*1.5, M(2), M(3), labels{7}, 'FontSize', 12, 'FontWeight', 'bold');
    text(N(1), N(2) - offset, N(3), labels{8}, 'FontSize', 12, 'FontWeight', 'bold');

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
            
            camzoom(0.7);

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
    