function visual(mode, azimuth, elevation, point_O, point_O1, point_A, point_C, point_A1, point_B1)
    close all;
    fig = figure('Visible', 'off');
    
    r = 1;
    h = 1;
    n_pts = 100;

    O = [0, 0, 0];
    O1 = [0, 0, h];
    A = [r, 0, 0];
    A1 = [r, 0, h];
    
    theta_C = 2*pi/3;
    C = [r*cos(theta_C), r*sin(theta_C), 0];
    
    theta_B1 = pi/3;
    B1 = [r*cos(theta_B1), r*sin(theta_B1), h];
    B = [r*cos(theta_B1), r*sin(theta_B1), 0];

    hold on;
    
    [X,Y,Z] = cylinder(r, n_pts-1);
    Z = Z * h;
    surf(X, Y, Z, 'FaceColor', [0.3 0.7 0.9], 'EdgeColor', 'none', 'FaceAlpha', 0.4);

    theta = linspace(0, 2*pi, n_pts);
    x_circle = r * cos(theta);
    y_circle = r * sin(theta);
    patch(x_circle, y_circle, zeros(1, n_pts), [0.3 0.7 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'k', 'LineWidth', 1);
    patch(x_circle, y_circle, h*ones(1, n_pts), [0.3 0.7 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'k', 'LineWidth', 1);
    
    plot3([O(1), A(1)], [O(2), A(2)], [O(3), A(3)], 'k--', 'LineWidth', 1);
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([O1(1), A1(1)], [O1(2), A1(2)], [O1(3), A1(3)], 'k-', 'LineWidth', 1.5);
    plot3([O1(1), B1(1)], [O1(2), B1(2)], [O1(3), B1(3)], 'k-', 'LineWidth', 1.5);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([B1(1), C(1)], [B1(2), C(2)], [B1(3), C(3)], 'r-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'r-', 'LineWidth', 2);
    
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k--', 'LineWidth', 1);
    plot3([C(1), O1(1)],[C(2), O1(2)], [C(3),O1(3)],'k--', 'LineWidth', 1);
    plot3([C(1), A1(1)],[C(2), A1(2)], [C(3),A1(3)],'k--', 'LineWidth', 1);

    all_points = {O, O1, A, A1, B1, C};
    labels = {point_O, point_O1, point_A, point_A1, point_B1, point_C};
    
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 50, 'k', 'filled');
        text_pos = pt * 1.1;
        if all(pt == O)
            text_pos = [-0.15, -0.15, -0.05];
        end
        text(text_pos(1), text_pos(2), text_pos(3) + 0.05, labels{i}, 'FontSize', 14, 'FontWeight', 'bold', 'Interpreter', 'tex');
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
    