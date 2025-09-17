function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_P)
    close all;
    fig = figure('Visible', 'off');
    
    D = [0, 0, 0];
    C = [3, 0, 0];
    A = [0, 5*sqrt(3), 0];
    B = [4, sqrt(3), 0];
    E = [0, 3*sqrt(3), 0];
    F = [2, 3*sqrt(3), 0];
    P = [0, 3*sqrt(3), 2*sqrt(3)];
    
    hold on;
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'b-', 'LineWidth', 2);
    
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k--', 'LineWidth', 1);
    plot3([A(1), F(1)], [A(2), F(2)], [A(3), F(3)], 'k--', 'LineWidth', 1);
    
    plot3([P(1), E(1)], [P(2), E(2)], [P(3), E(3)], 'r-', 'LineWidth', 2);
    plot3([P(1), F(1)], [P(2), F(2)], [P(3), F(3)], 'r-', 'LineWidth', 2);
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'r-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'r-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'r-', 'LineWidth', 2);
    
    patch([P(1), C(1), D(1)], [P(2), C(2), D(2)], [P(3), C(3), D(3)], 'm', 'FaceAlpha', 0.2);
    patch([P(1), B(1), F(1)], [P(2), B(2), F(2)], [P(3), B(3), F(3)], 'g', 'FaceAlpha', 0.2);
    
    all_points = {A, B, C, D, E, F, P};
    labels = {point_A, point_B, point_C, point_D, point_E, point_F, point_P};
    for i = 1:length(all_points)
        pt = all_points{i};
        if i == 1
            scatter3(pt(1), pt(2), pt(3), 30, 'o', 'MarkerEdgeColor', [0.5 0.5 0.5]);
        else
            scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
        end
    end
    
    text(A(1), A(2)+0.5, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold', 'Color', [0.5 0.5 0.5]);
    text(B(1)+0.2, B(2), B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2)-0.2, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1)-0.3, D(2)-0.2, D(3), point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1)-0.3, E(2)+0.2, E(3), point_E, 'FontSize', 12, 'FontWeight', 'bold');
    text(F(1)+0.2, F(2)+0.2, F(3), point_F, 'FontSize', 12, 'FontWeight', 'bold');
    text(P(1), P(2), P(3)+0.3, point_P, 'FontSize', 12, 'FontWeight', 'bold');
    
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
    