function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_O, point_E, point_F, point_D_prime)
    close all;
    fig = figure('Visible', 'off');

    O = [0, 0, 0];
    A = [0, -3, 0];
    B = [-4, 0, 0];
    C = [0, 3, 0];
    D = [4, 0, 0];
    E = [1, -9/4, 0];
    F = [1, 9/4, 0];
    H = [1, 0, 0];
    D_prime = [1, 0, sqrt(7)];

    hold on;
    
    base_vertices_x = [A(1), B(1), C(1), F(1), E(1)];
    base_vertices_y = [A(2), B(2), C(2), F(2), E(2)];
    base_vertices_z = [A(3), B(3), C(3), F(3), E(3)];
    patch(base_vertices_x, base_vertices_y, base_vertices_z, [0.5 0.7 0.9], 'FaceAlpha', 0.2);
    
    patch([D_prime(1), A(1), B(1)], [D_prime(2), A(2), B(2)], [D_prime(3), A(3), B(3)], [0.9 0.5 0.5], 'FaceAlpha', 0.4);
    patch([D_prime(1), B(1), C(1)], [D_prime(2), B(2), C(2)], [D_prime(3), B(3), C(3)], [0.5 0.9 0.5], 'FaceAlpha', 0.4);
    patch([D_prime(1), C(1), F(1)], [D_prime(2), C(2), F(2)], [D_prime(3), C(3), F(3)], [0.5 0.5 0.9], 'FaceAlpha', 0.4);
    patch([D_prime(1), F(1), E(1)], [D_prime(2), F(2), E(2)], [D_prime(3), F(3), E(3)], [0.9 0.9 0.5], 'FaceAlpha', 0.6);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), F(1)], [C(2), F(2)], [C(3), F(3)], 'k-', 'LineWidth', 1.5);
    plot3([E(1), A(1)], [E(2), A(2)], [E(3), A(3)], 'k-', 'LineWidth', 1.5);
    plot3([F(1), E(1)], [F(2), E(2)], [F(3), E(3)], 'k-', 'LineWidth', 1.5);

    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k--', 'LineWidth', 1);
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k--', 'LineWidth', 1);
    plot3([D(1), F(1)], [D(2), F(2)], [D(3), F(3)], 'k--', 'LineWidth', 1);
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k--', 'LineWidth', 1);

    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k--', 'LineWidth', 1);
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'k--', 'LineWidth', 1);

    plot3([D_prime(1), A(1)], [D_prime(2), A(2)], [D_prime(3), A(3)], 'k-', 'LineWidth', 1.5);
    plot3([D_prime(1), B(1)], [D_prime(2), B(2)], [D_prime(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([D_prime(1), C(1)], [D_prime(2), C(2)], [D_prime(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([D_prime(1), E(1)], [D_prime(2), E(2)], [D_prime(3), E(3)], 'k-', 'LineWidth', 1.5);
    plot3([D_prime(1), F(1)], [D_prime(2), F(2)], [D_prime(3), F(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([D_prime(1), H(1)], [D_prime(2), H(2)], [D_prime(3), H(3)], 'r--', 'LineWidth', 1.5);
    
    points_to_plot = {A, B, C, D, E, F, O, D_prime};
    labels = {point_A, point_B, point_C, point_D, point_E, point_F, point_O, point_D_prime};
    
    for i = 1:length(points_to_plot)
        pt = points_to_plot{i};
        scatter3(pt(1), pt(2), pt(3), 30, 'k', 'filled');
        text_offset = 0.2;
        text(pt(1) + text_offset, pt(2) + text_offset, pt(3), labels{i}, 'FontSize', 12, 'FontWeight', 'bold', 'Interpreter', 'tex');
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
    