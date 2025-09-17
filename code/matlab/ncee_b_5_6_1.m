function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_E, point_O)
    close all;
    fig = figure('Visible', 'off');
    
    r = 1;
    h = 2;
    
    O = [0, 0, 0];
    P = [0, 0, h];
    A = [-r, 0, 0];
    B = [r, 0, 0];
    
    C = [0, -r, 0];
    theta_E = -pi / 4;
    E = [r*cos(theta_E), r*sin(theta_E), 0];

    hold on;
    
    [X_cone, Y_cone, Z_cone] = cylinder([r, 0], 100);
    Z_cone = Z_cone * h;
    surf(X_cone, Y_cone, Z_cone, 'FaceColor', [0.3, 0.7, 0.9], 'EdgeColor', 'none', 'FaceAlpha', 0.3);

    theta_circle = linspace(0, 2*pi, 200);
    x_circle = r * cos(theta_circle);
    y_circle = r * sin(theta_circle);
    z_circle = zeros(size(theta_circle));
    
    front_indices = find(y_circle <= 0);
    back_indices = find(y_circle >= 0);
    
    plot3(x_circle(front_indices), y_circle(front_indices), z_circle(front_indices), 'k-', 'LineWidth', 1.5);
    plot3(x_circle(back_indices), y_circle(back_indices), z_circle(back_indices), 'k--', 'LineWidth', 1);

    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'r-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 1.5);

    plot3([P(1), O(1)], [P(2), O(2)], [P(3), O(3)], 'k--', 'LineWidth', 1);
    plot3([O(1), A(1)], [O(2), A(2)], [O(3), A(3)], 'k--', 'LineWidth', 1);
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 1);
    plot3([O(1), E(1)], [O(2), E(2)], [O(3), E(3)], 'r--', 'LineWidth', 2);
    
    all_points = {P, O, A, B, C, E};
    labels = {point_P, point_O, point_A, point_B, point_C, point_E};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
        text_offset = [0.1, -0.1, 0.1];
        if pt == C
            text_offset = [0, -0.2, -0.1];
        end
        text(pt(1)+text_offset(1), pt(2)+text_offset(2), pt(3)+text_offset(3), labels{i}, 'FontSize', 14, 'FontWeight', 'bold');
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
    