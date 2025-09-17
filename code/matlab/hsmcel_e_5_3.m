function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_P, point_D, point_E)
    close all;
    fig = figure('Visible', 'off');

    s = 4 * sqrt(2);
    h = 2;
    
    A = [0, 0, 0]; P = [0, 0, h]; B = [s, 0, 0]; C = [s/2, s*sqrt(3)/2, 0];
    
    D = (B + C) / 2; E = (A + C) / 2; F = (C + D) / 2;

    hold on;

    plot3([A(1), F(1)], [A(2), F(2)], [A(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), F(1)], [P(2), F(2)], [P(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 2);
    plot3([P(1), E(1)], [P(2), E(2)], [P(3), E(3)], 'k--', 'LineWidth', 2);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 2);
    
    all_points = [P, A, B, C, D, E, F];
    scatter3(all_points(:,1), all_points(:,2), all_points(:,3), 'filled', 'k');
    
    text(P(1)-0.2, P(2), P(3)+0.2, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1)-0.3, A(2)-0.3, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2)-0.2, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2)+0.3, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+0.2, D(2)+0.2, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1)-0.4, E(2)+0.1, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    

    axis equal; axis off; view(azimuth, elevation);
    set(gca, 'Color', 'white'); set(gcf, 'Color', 'white');
    set(gcf, 'ToolBar', 'none'); set(gcf, 'MenuBar', 'none');
    
    
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
    