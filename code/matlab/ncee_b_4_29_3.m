function visual(mode, azimuth, elevation, point_V, point_A, point_B, point_C, point_O, point_M)
    close all;
    fig = figure('Visible', 'off');

    s = sqrt(2);
    C = [0, 0, 0];
    A = [s, 0, 0];
    B = [0, s, 0];
    
    O = (A + B) / 2;
    V_height = sqrt( (2*s/sqrt(2))^2 - (s/sqrt(2))^2 );
    V = [O(1), O(2), V_height];
    M = (V + A) / 2;

    hold on;
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([M(1), O(1)], [M(2), O(2)], [M(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), C(1)], [M(2), C(2)], [M(3), C(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([V(1), A(1)], [V(2), A(2)], [V(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), B(1)], [V(2), B(2)], [V(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), C(1)], [V(2), C(2)], [V(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    all_points = {V, A, B, C, O, M};
    labels = {point_V, point_A, point_B, point_C, point_O, point_M};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
        text(pt(1)+0.2, pt(2)+0.2, pt(3)+0.2, labels{i}, 'FontSize', 14, 'FontWeight', 'bold');
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
    