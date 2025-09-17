function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_M)
    close all;
    fig = figure('Visible', 'off');

    PD = 1;
    DC = 1;
    BC = sqrt(2);
    
    D = [0, 0, 0];
    P = [0, 0, PD];
    C = [DC, 0, 0];
    A = [0, BC, 0];
    B = [DC, BC, 0];
    
    M = (B + C) / 2;

    hold on;

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);

    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), M(1)], [A(2), M(2)], [A(3), M(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), M(1)], [P(2), M(2)], [P(3), M(3)], 'k-', 'LineWidth', 1.5);
    
    points = {A, B, C, D, M, P};
    for i = 1:length(points)
        pt = points{i};
        scatter3(pt(1), pt(2), pt(3), 50, 'ko', 'filled');
    end
    
    text(A(1)-0.1, A(2), A(3)+0.05, point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.15, B(2)+0.15, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.15, C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)-0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)+0.15, M(2), M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1), P(2), P(3)+0.1, point_P, 'FontSize', 14, 'FontWeight', 'bold');

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
    