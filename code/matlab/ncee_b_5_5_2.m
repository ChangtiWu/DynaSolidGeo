function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F)
    close all;
    fig = figure('Visible', 'off');

    a = 2; 
    
    hE = a * sqrt(2) / 2;
    hF = hE / 2;

    B = [0, 0, 0];
    A = [a, 0, 0];
    C = [a*cosd(120), a*sind(120), 0];
    D = A + C;

    E = [B(1), B(2), hE];
    F = [D(1), D(2), hF];

    hold on;

    patch([A(1),B(1),C(1)], [A(2),B(2),C(2)], [A(3),B(3),C(3)], [0.5 0.7 0.9], 'FaceAlpha', 0.2);
    patch([A(1),E(1),C(1)], [A(2),E(2),C(2)], [A(3),E(3),C(3)], [0.8 0.5 0.5], 'FaceAlpha', 0.3);
    patch([A(1),F(1),C(1)], [A(2),F(2),C(2)], [A(3),F(3),C(3)], [0.5 0.8 0.5], 'FaceAlpha', 0.3);
    patch([C(1),D(1),F(1)], [C(2),D(2),F(2)], [C(3),D(3),F(3)], [0.9 0.9 0.5], 'FaceAlpha', 0.3);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), E(1)], [C(2), E(2)], [C(3), E(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), F(1)], [C(2), F(2)], [C(3), F(3)], 'k-', 'LineWidth', 1.5);
  
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 1);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k--', 'LineWidth', 1);
    plot3([A(1), F(1)], [A(2), F(2)], [A(3), F(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k--', 'LineWidth', 1);
    
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'b--', 'LineWidth', 1);
    plot3([D(1), F(1)], [D(2), F(2)], [D(3), F(3)], 'b--', 'LineWidth', 1);
    
    all_points = {A, B, C, D, E, F};
    labels = {point_A, point_B, point_C, point_D, point_E, point_F};
    
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 30, 'k', 'filled');
        text_offset = 0.15;
        text(pt(1) + text_offset, pt(2), pt(3), labels{i}, 'FontSize', 14, 'FontWeight', 'bold');
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
    