function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_G)
    close all;
    fig = figure('Visible', 'off');
    
    AB = 3;
    AD = 2;
    rot_angle_deg = 120;
    rot_angle_rad = rot_angle_deg * pi / 180;
    
    A = [0, 0, 0];
    B = [0, 0, AB];
    D = [AD, 0, 0];
    C = [AD, 0, AB];
    
    Rxz = @(theta) [cos(theta), -sin(theta); sin(theta), cos(theta)];
    D_rot = Rxz(rot_angle_rad) * [D(1); D(2)];
    C_rot = Rxz(rot_angle_rad) * [C(1); C(2)];
    
    F = [D_rot(1), D_rot(2), 0];
    E = [C_rot(1), C_rot(2), AB];
    
    G_rot = Rxz(rot_angle_rad/2) * [D(1); D(2)];
    G = [G_rot(1), G_rot(2), 0];
    
    P_vis_rot = Rxz(90 * pi / 180) * [C(1); C(2)];
    P = [P_vis_rot(1), P_vis_rot(2), AB];
    
    hold on;
    
    patch([E(1), A(1), G(1)], [E(2), A(2), G(2)], [E(3), A(3), G(3)], 'm', 'FaceAlpha', 0.3);
    patch([C(1), A(1), G(1)], [C(2), A(2), G(2)], [C(3), A(3), G(3)], 'g', 'FaceAlpha', 0.2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), F(1)], [A(2), F(2)], [A(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([F(1), E(1)], [F(2), E(2)], [F(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k-', 'LineWidth', 2);
    
    theta = linspace(0, rot_angle_rad, 50);
    x_arc_bottom = AD * cos(theta);
    y_arc_bottom = AD * sin(theta);
    plot3(x_arc_bottom, y_arc_bottom, zeros(size(theta)), 'k-', 'LineWidth', 2);
    plot3(x_arc_bottom, y_arc_bottom, AB*ones(size(theta)), 'k-', 'LineWidth', 2);
    
    plot3([A(1), G(1)], [A(2), G(2)], [A(3), G(3)], 'r--', 'LineWidth', 1.5);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'r--', 'LineWidth', 1.5);
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'r--', 'LineWidth', 1.5);
    plot3([A(1), P(1)], [A(2), P(2)], [A(3), P(3)], 'b--', 'LineWidth', 1);
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'b--', 'LineWidth', 1);
    
    all_points = {A, B, C, D, E, F, G, P};

    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    
    text(A(1), A(2)-0.2, A(3)-0.2, point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1), B(2)-0.2, B(3)+0.1, point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2), C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1)+0.1, D(2), D(3), point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1)-0.1, E(2)+0.1, E(3), point_E, 'FontSize', 12, 'FontWeight', 'bold');
    text(F(1)-0.1, F(2)+0.1, F(3), point_F, 'FontSize', 12, 'FontWeight', 'bold');
    text(G(1), G(2)+0.1, G(3), point_G, 'FontSize', 12, 'FontWeight', 'bold');
    
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

            camzoom(0.6);

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
    