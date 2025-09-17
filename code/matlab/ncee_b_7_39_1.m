function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_O, point_A1)
    close all;
    fig = figure('Visible', 'off');
    
    A_orig = [0, 0, 0];
    B = [1, 0, 0];
    C = [1, 1, 0];
    D = [0, 2, 0];
    E = [0, 1, 0];
    O = [0.5, 0.5, 0];
    A1 = [0.5, 0.5, 1/sqrt(2)];
    
    hold on;
    
    patch([A1(1), B(1), C(1)], [A1(2), B(2), C(2)], [A1(3), B(3), C(3)], 'm', 'FaceAlpha', 0.3);
    patch([A1(1), C(1), D(1)], [A1(2), C(2), D(2)], [A1(3), C(3), D(3)], 'g', 'FaceAlpha', 0.2);
    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), B(1)], [E(2), B(2)], [E(3), B(3)], 'k-', 'LineWidth', 2);
    
    plot3([A1(1), B(1)], [A1(2), B(2)], [A1(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), E(1)], [A1(2), E(2)], [A1(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), C(1)], [A1(2), C(2)], [A1(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), D(1)], [A1(2), D(2)], [A1(3), D(3)], 'k-', 'LineWidth', 2);
    
    plot3([A1(1), O(1)], [A1(2), O(2)], [A1(3), O(3)], 'r--', 'LineWidth', 1);
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'r--', 'LineWidth', 1);
    
    all_points = {A1, B, C, D, E, O};

    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    
    text(A1(1), A1(2), A1(3)+0.1, point_A1, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)+0.1, D(3), point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1)-0.1, E(2)+0.1, E(3), point_E, 'FontSize', 12, 'FontWeight', 'bold');
    text(O(1), O(2), O(3)-0.1, point_O, 'FontSize', 12, 'FontWeight', 'bold');
    
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
    