function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_F, point_E, point_D)
    close all;
    fig = figure('Visible', 'off');
    
    C = [0, 0, 0];
    A = [3, 0, 0];
    B = [0, 2, 0];
    F = [0, 1/2, sqrt(3)/2];
    E = [0, 3/2, sqrt(3)/2];
    D = [3/2, 1/2, sqrt(3)/2];
    
    hold on;
    
    patch([A(1) C(1) F(1) D(1)], [A(2) C(2) F(2) D(2)], [A(3) C(3) F(3) D(3)], 'c', 'FaceAlpha', 0.3);
    
    plot3([A(1) B(1)], [A(2) B(2)], [A(3) B(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1) C(1)], [B(2) C(2)], [B(3) C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1) A(1)], [C(2) A(2)], [C(3) A(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([D(1) E(1)], [D(2) E(2)], [D(3) E(3)], 'k-', 'LineWidth', 1.5);
    plot3([E(1) F(1)], [E(2) F(2)], [E(3) F(3)], 'k-', 'LineWidth', 1.5);
    plot3([F(1) D(1)], [F(2) D(2)], [F(3) D(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([A(1) D(1)], [A(2) D(2)], [A(3) D(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1) E(1)], [B(2) E(2)], [B(3) E(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1) F(1)], [C(2) F(2)], [C(3) F(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([B(1), F(1)], [B(2), F(2)], [B(3), F(3)], 'r--', 'LineWidth', 2.5);
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'b--', 'LineWidth', 2.5);
    
    all_points = {A, B, C, D, E, F};
    labels = {point_A, point_B, point_C, point_D, point_E, point_F};
    offset = 0.15;
    
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
        text(pt(1)+offset, pt(2)+offset, pt(3)+offset, labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
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

            camzoom(0.8);

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
    