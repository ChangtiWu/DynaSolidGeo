function visual(mode, azimuth, elevation, point_S, point_A, point_B, point_C, point_O)
    close all;
    fig = figure('Visible', 'off');

    D = [0, 0, 0];
    A = [0, -1, 0];
    B = [0, 1, 0];
    C = [1, 0, 0];
    S = [0, 0, sqrt(3)];
    O = [0, 0, 1/sqrt(3)];

    hold on;

    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), C(1)], [S(2), C(2)], [S(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k--', 'LineWidth', 1.5);
    plot3([S(1), D(1)], [S(2), D(2)], [S(3), D(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), O(1)], [A(2), O(2)], [A(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([C(1), O(1)], [C(2), O(2)], [C(3), O(3)], 'k--', 'LineWidth', 1.5);

    all_points = {S, A, B, C, D, O};
    point_coords = cell2mat(all_points');
    scatter3(point_coords(:,1), point_coords(:,2), point_coords(:,3), 50, 'ko', 'filled');
    
    text(S(1), S(2), S(3) + 0.1, point_S, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1) - 0.1, A(2) - 0.1, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1), B(2) + 0.1, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1) + 0.1, C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    
    text(O(1) + 0.1, O(2) - 0.1, O(3), point_O, 'FontSize', 14, 'FontWeight', 'bold');

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
    