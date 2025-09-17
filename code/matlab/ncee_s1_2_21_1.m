function visual(mode, azimuth, elevation, point_O, point_E, point_F, point_G, point_H, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1)
    close all;
    fig = figure('Visible', 'off');

    AB_len = 6;
    BC_len = 6;
    AA1_len = 4;
    
    A = [0, BC_len, 0];
    B = [AB_len, BC_len, 0];
    C = [AB_len, 0, 0];
    D = [0, 0, 0];

    A1 = [0, BC_len, AA1_len];
    B1 = [AB_len, BC_len, AA1_len];
    C1 = [AB_len, 0, AA1_len];
    D1 = [0, 0, AA1_len];

    O = (B + D1) / 2;
    E = (B + C) / 2;
    F = (C + C1) / 2;
    G = (C1 + B1) / 2;
    H = (B1 + B) / 2;
    
    hold on;
    
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k-', 'LineWidth', 2);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    
    plot3([C(1), B(1)], [C(2), B(2)], [C(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);

    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), D1(1)], [A1(2), D1(2)], [A1(3), D1(3)], 'k-', 'LineWidth', 2);

    plot3([B1(1), B(1)], [B1(2), B(2)], [B1(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    
    plot3([D1(1), C1(1)], [D1(2), C1(2)], [D1(3), C1(3)], 'k-', 'LineWidth', 2);

    plot3([O(1), E(1)], [O(2), E(2)], [O(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), F(1)], [O(2), F(2)], [O(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), G(1)], [O(2), G(2)], [O(3), G(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), H(1)], [O(2), H(2)], [O(3), H(3)], 'k--', 'LineWidth', 1.5);

    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([F(1), G(1)], [F(2), G(2)], [F(3), G(3)], 'k--', 'LineWidth', 1.5);
    plot3([G(1), H(1)], [G(2), H(2)], [G(3), H(3)], 'k--', 'LineWidth', 1.5);
    plot3([H(1), E(1)], [H(2), E(2)], [H(3), E(3)], 'k--', 'LineWidth', 1.5);

    all_points = {A, B, C, D, A1, B1, C1, D1, O, E, F, G, H};
    all_labels = {point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_O, point_E, point_F, point_G, point_H};
    for i = 1:length(all_points)
        pt = all_points{i};
        text(pt(1)+0.2, pt(2)+0.2, pt(3)+0.2, all_labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
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

        camzoom(0.9);

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
    