function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F)
    close all;
    fig = figure('Visible', 'off');
    
    a = 2; 
    b = 3; 
    k = 0.5;
    
    C = [0, 0, 0];
    B = [a*sqrt(2)/2, a*sqrt(2)/2, 0];
    A = [0, b, 0];
    D = [0, a*sqrt(2), a*sqrt(2)];
    
    E = D + k * (C - A);
    F = E + k * (C - B);
    
    hold on;
    
    patch([D(1) B(1) C(1)], [D(2) B(2) C(2)], [D(3) B(3) C(3)], [0.5 0.9 0.9], 'FaceAlpha', 0.4);
    
    patch([A(1) B(1) C(1)], [A(2) B(2) C(2)], [A(3) B(3) C(3)], [0.8 0.8 0.8], 'FaceAlpha', 0.2);
    patch([D(1) E(1) F(1)], [D(2) E(2) F(2)], [D(3) E(3) F(3)], [0.8 0.8 0.8], 'FaceAlpha', 0.3);
    patch([A(1) C(1) F(1) D(1)], [A(2) C(2) F(2) D(2)], [A(3) C(3) F(3) D(3)], [0.9 0.7 0.7], 'FaceAlpha', 0.2);
    patch([C(1) B(1) E(1) F(1)], [C(2) B(2) E(2) F(2)], [C(3) B(3) E(3) F(3)], [0.7 0.9 0.7], 'FaceAlpha', 0.2);
    patch([A(1) B(1) E(1) D(1)], [A(2) B(2) E(2) D(2)], [A(3) B(3) E(3) D(3)], [0.9 0.9 0.7], 'FaceAlpha', 0.2);
    
    plot3([A(1) B(1)], [A(2) B(2)], [A(3) B(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1) C(1)], [B(2) C(2)], [B(3) C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1) A(1)], [C(2) A(2)], [C(3) A(3)], 'k-', 'LineWidth', 1.5);
    plot3([D(1) E(1)], [D(2) E(2)], [D(3) E(3)], 'k-', 'LineWidth', 1.5);
    plot3([E(1) F(1)], [E(2) F(2)], [E(3) F(3)], 'k-', 'LineWidth', 1.5);
    plot3([F(1) D(1)], [F(2) D(2)], [F(3) F(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1) D(1)], [A(2) D(2)], [A(3) D(3)], 'k-', 'LineWidth', 1.5);
    plot3([B(1) E(1)], [B(2) E(2)], [B(3) E(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1) F(1)], [C(2) F(2)], [C(3) F(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([E(1) F(1)], [E(2) F(2)], [E(3) F(3)], 'r-', 'LineWidth', 2.5);
    plot3([D(1) B(1)], [D(2) B(2)], [D(3) B(3)], 'b--', 'LineWidth', 2.5);
    plot3([D(1) F(1)], [D(2) F(2)], [D(3) F(3)], 'm-', 'LineWidth', 2.5);
    
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
    