function visual(mode, azimuth, elevation, point_D, point_E, point_F, point_A, point_B, point_C, point_G, point_H)
    close all;
    fig = figure('Visible', 'off');
    
    side = 2;
    B = [0, 0, 0];
    A = [side, 0, 0];
    C = [0, side, 0];
    h = 1;
    E = [0, side/2, h];
    D = [side/2, side/2, h];
    F = [0, side, h];
    G = (A + C) / 2;
    H = (B + C) / 2;
    
    hold on;
    
    patch([F(1), G(1), H(1)], [F(2), G(2), H(2)], [F(3), G(3), H(3)], 'm', 'FaceAlpha', 0.3);
    patch([A(1), C(1), F(1), D(1)], [A(2), C(2), F(2), D(2)], [A(3), C(3), F(3), D(3)], 'g', 'FaceAlpha', 0.2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), A(1)], [C(2), A(2)], [C(3), A(3)], 'k-', 'LineWidth', 2);
    
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([F(1), D(1)], [F(2), D(2)], [F(3), D(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), F(1)], [C(2), F(2)], [C(3), F(3)], 'k-', 'LineWidth', 2);
    
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'b-', 'LineWidth', 2.5);
    
    all_points = {A, B, C, D, E, F, G, H};

    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    
    text(A(1)+0.1, A(2)-0.1, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)-0.1, B(2)-0.1, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)-0.1, C(2)+0.1, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1)+0.1, D(2), D(3)+0.1, point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1)-0.1, E(2), E(3)+0.1, point_E, 'FontSize', 12, 'FontWeight', 'bold');
    text(F(1)-0.1, F(2), F(3)+0.1, point_F, 'FontSize', 12, 'FontWeight', 'bold');
    text(G(1), G(2), G(3)-0.1, point_G, 'FontSize', 12, 'FontWeight', 'bold');
    text(H(1), H(2), H(3)-0.1, point_H, 'FontSize', 12, 'FontWeight', 'bold');
    
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
    