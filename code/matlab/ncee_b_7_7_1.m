function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C)
    close all;
    fig = figure('Visible', 'off');
    
    PA = 1;
    AB = 1;
    BC = 1;
    PC_val = sqrt(3);
    
    A = [0, 0, 0];
    P = [0, 0, PA];
    B = [AB, 0, 0];
    AC_val = sqrt(PC_val^2 - PA^2);
    y_C = sqrt(BC^2 - (sqrt(AC_val^2 - AB^2)-AB)^2); 
    C = [AB, BC, 0];
    
    hold on;
    
    patch([A(1), P(1), C(1)], [A(2), P(2), C(2)], [A(3), P(3), C(3)], 'm', 'FaceAlpha', 0.3);
    patch([B(1), P(1), C(1)], [B(2), P(2), C(2)], [B(3), P(3), C(3)], 'g', 'FaceAlpha', 0.3);
    patch([P(1), A(1), B(1)], [P(2), A(2), B(2)], [P(3), A(3), B(3)], 'c', 'FaceAlpha', 0.2);
    patch([A(1), B(1), C(1)], [A(2), B(2), C(2)], [A(3), B(3), C(3)], 'y', 'FaceAlpha', 0.2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), A(1)], [C(2), A(2)], [C(3), A(3)], 'k-', 'LineWidth', 2);
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    
    all_points = {A, B, C, P};
    labels = {point_A, point_B, point_C, point_P};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    
    text(A(1)-0.1, A(2)-0.1, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(P(1)-0.1, P(2)-0.1, P(3)+0.1, point_P, 'FontSize', 12, 'FontWeight', 'bold');
    
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
    