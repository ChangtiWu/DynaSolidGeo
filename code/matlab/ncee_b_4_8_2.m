function visual(mode, azimuth, elevation, point_D, point_O, point_P, point_A, point_B, point_C)
    close all;
    fig = figure('Visible', 'off');

    r = 1;
    h_cone = sqrt(2);
    h_pyramid = sqrt(2)/2;
    
    O = [0, 0, 0];
    D = [0, 0, h_cone];
    P = [0, 0, h_pyramid];
    
    A = [r*cosd(210), r*sind(210), 0];
    B = [r*cosd(-30), r*sind(-30), 0];
    C = [0, r, 0];
    
    hold on;

    [Xc,Yc,Zc] = cylinder([r 0], 50);
    cone_surf = surf(Xc, Yc, Zc*h_cone);
    set(cone_surf, 'FaceColor', [0.5 0.8 0.9], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), B(1)], [D(2), B(2)], [D(3), B(3)], 'k-', 'LineWidth', 2);
    
    theta = linspace(0, 2*pi, 100);
    x_circle = r * cos(theta);
    y_circle = r * sin(theta);
    z_circle = zeros(size(theta));
    plot3(x_circle, y_circle, z_circle, 'k--', 'LineWidth', 1.5);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([C(1), A(1)], [C(2), A(2)], [C(3), A(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([D(1), O(1)], [D(2), O(2)], [D(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 1.5);
    
    all_points = {A, B, C, D, O, P};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
    end
    
    text(A(1)-0.1, A(2)-0.1, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1), C(2)+0.1, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1), D(2), D(3)+0.1, point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(O(1)+0.05, O(2)-0.1, O(3), point_O, 'FontSize', 12, 'FontWeight', 'bold');
    text(P(1)+0.05, P(2), P(3)+0.05, point_P, 'FontSize', 12, 'FontWeight', 'bold');

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
    