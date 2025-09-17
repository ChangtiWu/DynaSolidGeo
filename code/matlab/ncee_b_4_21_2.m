function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_M, point_N)
    close all;
    fig = figure('Visible', 'off');

    A = [0, 0, 0];
    D = [3, 0, 0];
    B = [-2, sqrt(5), 0];
    C = [2, sqrt(5), 0];
    P = [0, 0, 4];
    M = [2, 0, 0];
    N = (P + C) / 2;

    hold on;

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k--', 'LineWidth', 1.5);
    plot3([N(1), B(1)], [N(2), B(2)], [N(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([N(1), C(1)], [N(2), C(2)], [N(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), B(1)], [M(2), B(2)], [M(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), C(1)], [M(2), C(2)], [M(3), C(3)], 'k--', 'LineWidth', 1.5);

    all_points = {P, A, B, C, D, M, N};
    labels = {point_P, point_A, point_B, point_C, point_D, point_M, point_N};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
        text(pt(1)+0.5, pt(2)+0.5, pt(3)+0.5, labels{i}, 'FontSize', 14, 'FontWeight', 'bold');
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
    