function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F)
    close all;
    fig = figure('Visible', 'off');
    hold on;

    a = 3; 
    b = 2; 
    c = 1.5;
    L = 1;

    A = [0, L*sqrt(3)/2, 0];
    B = [-L/2, 0, 0];
    C = [L/2, 0, 0];
    
    D = [A(1), A(2), a];
    E = [B(1), B(2), b];
    F = [C(1), C(2), c];
    
    
    plot3([A(1),B(1)], [A(2),B(2)], [A(3),B(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1),D(1)], [A(2),D(2)], [A(3),D(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1),E(1)], [B(2),E(2)], [B(3),E(3)], 'k-', 'LineWidth', 1.5);
    plot3([D(1),F(1)], [D(2),F(2)], [D(3),F(3)], 'k-', 'LineWidth', 1.5);
    plot3([E(1),F(1)], [E(2),F(2)], [E(3),F(3)], 'k-', 'LineWidth', 1.5);
    plot3([D(1),E(1)], [D(2),E(2)], [D(3),E(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1),E(1)], [A(2),E(2)], [A(3),E(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1),D(1)], [B(2),D(2)], [B(3),D(3)], 'k--', 'LineWidth', 1.5);

    plot3([A(1),C(1)], [A(2),C(2)], [A(3),C(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1),C(1)], [B(2),C(2)], [B(3),C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1),F(1)], [C(2),F(2)], [C(3),F(3)], 'k-', 'LineWidth', 1.5);
    
    all_points_coords = [A; B; C; D; E; F];
    all_points_labels = {point_A, point_B, point_C, point_D, point_E, point_F};
    scatter3(all_points_coords(:,1), all_points_coords(:,2), all_points_coords(:,3), 30, 'k', 'filled');

    text_offset = 0.1;
    text(A(1), A(2), A(3) + text_offset, all_points_labels{1}, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1) - text_offset, B(2), B(3), all_points_labels{2}, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1), C(2) - text_offset, C(3), all_points_labels{3}, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1), D(2), D(3) + text_offset, all_points_labels{4}, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1), E(2), E(3) + text_offset, all_points_labels{5}, 'FontSize', 12, 'FontWeight', 'bold');
    text(F(1), F(2) - text_offset, F(3), all_points_labels{6}, 'FontSize', 12, 'FontWeight', 'bold');
    
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

        camzoom(0.3);

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