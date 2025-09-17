function visual(mode, azimuth, elevation, point_V, point_A, point_B, point_C, point_P)
    close all;
    fig = figure('Visible', 'off');

    a = 2; h_v = 3;
    O = [0, 0, 0]; V = [0, 0, h_v];
    r = a / sqrt(3);
    A = [r, 0, 0]; B = [r*cos(2*pi/3), r*sin(2*pi/3), 0]; C = [r*cos(4*pi/3), r*sin(4*pi/3), 0];
    D = (B+C)/2;
    
    P_ratio = 0.5; P = A + P_ratio * (V - A);
    
    hold on;

    plot3([V(1), A(1)], [V(2), A(2)], [V(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), B(1)], [V(2), B(2)], [V(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), C(1)], [V(2), C(2)], [V(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), O(1)], [V(2), O(2)], [V(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 1.5);
    plot3([V(1), D(1)], [V(2), D(2)], [V(3), D(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k--', 'LineWidth', 1.5);
    
    all_points = {V, A, B, C, O, D, P};
    point_coords = cell2mat(all_points');
    scatter3(point_coords(:,1), point_coords(:,2), point_coords(:,3), 50, 'ko', 'filled');

    text(V(1), V(2), V(3)+0.1, point_V, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1)+0.2, A(2), A(3)-0.2, point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)-0.1, B(2)+0.1, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2)-0.2, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    
    text(P(1)+0.2, P(2)+0.2, P(3), point_P, 'FontSize', 14, 'FontWeight', 'bold');
    
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
    