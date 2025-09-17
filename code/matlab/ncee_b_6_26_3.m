function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_O, point_E, point_F, point_G, point_H)
    close all;
    fig = figure('Visible', 'off');

    s2 = sqrt(2);

    O = [0, 0, 0];
    A = [0, s2, 0];
    B = [s2, 0, 0];
    C = [0, -s2, 0];
    D = [-s2, 0, 0];
    
    E = [0, 0, s2];
    F = [s2, 0, s2];
    
    G = (A + B) / 2;

    hold on;

    plot3([A(1), B(1), C(1), D(1), A(1)], [A(2), B(2), C(2), D(2), A(2)], [A(3), B(3), C(3), D(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([O(1), B(1), F(1), E(1), O(1)], [O(2), B(2), F(2), E(2), O(2)], [O(3), B(3), F(3), E(3), O(3)], 'b-', 'LineWidth', 2);

    plot3([C(1), E(1)], [C(2), E(2)], [C(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), F(1)], [A(2), F(2)], [A(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k-', 'LineWidth', 2);
    
    all_points_labels = {point_A, point_B, point_C, point_D, point_O, point_E, point_F, point_G};
    all_points_coords = {A, B, C, D, O, E, F, G};
    offsets = {[0, 0.2, 0.1], [0.2, 0, 0], [0, -0.2, -0.1], [-0.2, 0, 0], ...
               [0.1, -0.2, 0], [0, 0.1, 0.2], [0.2, 0.1, 0.2], [0.2, 0.2, 0]};

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
    