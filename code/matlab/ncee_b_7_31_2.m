function visual(mode, azimuth, elevation, point_A, point_C, point_O, point_E, point_F, point_O_prime, point_B)
    close all;
    fig = figure('Visible', 'off');
    R1 = 2;
    R2 = 1;
    h = 3;
    O = [0, 0, 0];
    O_prime = [0, 0, h];
    A = [-R1, 0, 0];
    C = [R1, 0, 0];
    E = [-R2, 0, h];
    F = [R2, 0, h];
    theta_B = pi/6;
    B = [R1*cos(theta_B), R1*sin(theta_B), 0];
    G = (E + C) / 2;
    H = (F + B) / 2;
    theta = linspace(0, 2*pi, 100);
    x_bottom = R1 * cos(theta);
    y_bottom = R1 * sin(theta);
    z_bottom = zeros(size(theta));
    x_top = R2 * cos(theta);
    y_top = R2 * sin(theta);
    z_top = h * ones(size(theta));
    hold on;
    plot3(x_bottom, y_bottom, z_bottom, 'k-', 'LineWidth', 2);
    plot3(x_top, y_top, z_top, 'k-', 'LineWidth', 2);
    
    % 创建圆台侧面的网格点
    n = length(theta);
    X = zeros(2, n);
    Y = zeros(2, n);
    Z = zeros(2, n);
    X(1,:) = x_bottom;
    X(2,:) = x_top;
    Y(1,:) = y_bottom;
    Y(2,:) = y_top;
    Z(1,:) = z_bottom;
    Z(2,:) = z_top;
    surf(X, Y, Z, 'FaceColor', [0.8 0.8 0.8], 'EdgeColor', 'none', 'FaceAlpha', 0.3);
    
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'r-', 'LineWidth', 2);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'r-', 'LineWidth', 2);
    plot3([F(1), B(1)], [F(2), B(2)], [F(3), B(3)], 'b-', 'LineWidth', 2);
    plot3([E(1), C(1)], [E(2), C(2)], [E(3), C(3)], 'b-', 'LineWidth', 2);
    plot3([G(1), H(1)], [G(2), H(2)], [G(3), H(3)], 'g-', 'LineWidth', 2);
    % 绘制底面和顶面的半透明填充
    patch(x_bottom, y_bottom, z_bottom, [0.8, 0.8, 0.8], 'FaceAlpha', 0.3);
    patch(x_top, y_top, z_top, [0.8, 0.8, 0.8], 'FaceAlpha', 0.3);
    all_points = {A, B, C, O, E, F, O_prime};
    labels = {point_A, point_B, point_C, point_O, point_E, point_F, point_O_prime};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
        if i <= 4
            if i == 1
                text(pt(1)-0.3, pt(2)-0.3, pt(3), labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            elseif i == 2
                text(pt(1)+0.2, pt(2)+0.1, pt(3), labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            elseif i == 3
                text(pt(1)+0.2, pt(2)-0.3, pt(3), labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            else
                text(pt(1)+0.2, pt(2)-0.3, pt(3), labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            end
        elseif i <= 7
            if i == 5
                text(pt(1)-0.3, pt(2)-0.3, pt(3)+0.1, labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            elseif i == 6
                text(pt(1)+0.2, pt(2)-0.3, pt(3)+0.1, labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            else
                text(pt(1)+0.2, pt(2)-0.3, pt(3)+0.1, labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            end
        else
            if i == 8
                text(pt(1)-0.2, pt(2)-0.2, pt(3), labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            else
                text(pt(1)+0.2, pt(2)+0.1, pt(3), labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
            end
        end
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