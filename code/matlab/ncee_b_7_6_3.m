function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_O)
    close all;
    fig = figure('Visible', 'off');

    A = [0, 2, 0];
    B = [0, 0, 0];
    C = [2*sqrt(2), 0, 0];
    P = [sqrt(2), -1, sqrt(3)];
    D = [sqrt(2)/2, -1/2, sqrt(3)/2];
    E = [sqrt(2)/2, 1/2, sqrt(3)/2];
    O = [sqrt(2), 0, 0];
    F = [sqrt(2), 1, 0];

    hold on;

    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), O(1)], [A(2), O(2)], [A(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([D(1), O(1)], [D(2), O(2)], [D(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1), F(1)], [B(2), F(2)], [B(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 1.5);

    all_points = {A, B, C, P, D, E, O, F};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 50, 'k', 'filled');
    end
    
    text(A(1)-0.2, A(2)+0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)-0.3, B(2)-0.3, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2)-0.2, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1), P(2), P(3)+0.2, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+0.2, D(2)-0.2, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');

    text(O(1)+0.2, O(2)-0.2, O(3), point_O, 'FontSize', 14, 'FontWeight', 'bold');


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
    