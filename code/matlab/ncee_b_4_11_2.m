function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E)
    close all;
    fig = figure('Visible', 'off');

    a = 3;
    h = 6;

    A = [0, 0, 0];
    B = [a, 0, 0];
    D = [0, a, 0];
    C = [a, a, 0];
    
    A1 = [0, 0, h];
    B1 = [a, 0, h];
    D1 = [0, a, h];
    C1 = [a, a, h];

    E = [0, 0, h/2];

    hold on;

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C1(1), B1(1)], [C1(2), B1(2)], [C1(3), B1(3)], 'k-', 'LineWidth', 2);

    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), D1(1)], [A1(2), D1(2)], [A1(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([D1(1), C1(1)], [D1(2), C1(2)], [D1(3), C1(3)], 'k-', 'LineWidth', 2);
    
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), C1(1)], [E(2), C1(2)], [E(3), C1(3)], 'k--', 'LineWidth', 1.5);
    plot3([B1(1), E(1)], [B1(2), E(2)], [B1(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), C(1)], [E(2), C(2)], [E(3), C(3)], 'k--', 'LineWidth', 1.5);

    scatter3([A(1) B(1) C(1) D(1) A1(1) B1(1) C1(1) D1(1) E(1)], [A(2) B(2) C(2) D(2) A1(2) B1(2) C1(2) D1(2) E(2)], [A(3) B(3) C(3) D(3) A1(3) B1(3) C1(3) D1(3) E(3)], 40, 'ko', 'filled');

    text(A(1)-0.3, A(2)-0.3, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2)-0.3, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2)+0.2, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1)-0.3, D(2)+0.2, D(3), point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(A1(1)-0.15, A1(2)-0.5, A1(3), point_A1, 'FontSize', 12, 'FontWeight', 'bold');
    text(B1(1)+0.2, B1(2)-0.3, B1(3), point_B1, 'FontSize', 12, 'FontWeight', 'bold');
    text(C1(1)+0.2, C1(2)+0.2, C1(3), point_C1, 'FontSize', 12, 'FontWeight', 'bold');
    text(D1(1)-0.4, D1(2)+0.3, D1(3), point_D1, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1)-0.4, E(2), E(3), point_E, 'FontSize', 12, 'FontWeight', 'bold');

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

            camzoom(0.5);

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
    