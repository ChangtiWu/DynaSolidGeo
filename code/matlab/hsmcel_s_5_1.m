function visual(mode, azimuth, elevation, point_A, point_C, point_B, point_D)
    close all;
    fig = figure('Visible', 'off');
    hold on;

    a = 5;
    theta_deg = 30;
    phi_deg = 45;

    A = [0, 0, 0];
    C = [a, 0, 0];
    
    B_dir = [-cosd(theta_deg), sind(theta_deg), 0];
    D_dir = [-cosd(phi_deg), 0, sind(phi_deg)];
    
    B = A + 2.5 * B_dir;
    D = C + 3 * D_dir;
    
    t_P = 0.5;
    P = C + t_P * (D - C);
    
    R = [P(1), 0, 0];
    
    s_Q = dot(R - A, B_dir);
    Q = A + s_Q * B_dir;
    
    plane_size_x = [ -1, 6 ];
    plane_size_y = [ -1, 4 ];
    plane_size_z = [ -1, 4 ];
    
    plot3([plane_size_x(1), plane_size_x(2), plane_size_x(2), plane_size_x(1), plane_size_x(1)], ...
          [plane_size_y(1), plane_size_y(1), plane_size_y(2), plane_size_y(2), plane_size_y(1)], ...
          [0, 0, 0, 0, 0], 'k-', 'LineWidth', 1.0);
          
    plot3([plane_size_x(1), plane_size_x(2), plane_size_x(2), plane_size_x(1), plane_size_x(1)], ...
          [0, 0, 0, 0, 0], ...
          [plane_size_z(1), plane_size_z(1), plane_size_z(2), plane_size_z(2), plane_size_z(1)], 'k-', 'LineWidth', 1.0);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([A(1), Q(1)], [A(2), Q(2)], [A(3), Q(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([P(1), Q(1)], [P(2), Q(2)], [P(3), Q(3)], 'k-', 'LineWidth', 1.5);
    plot3([P(1), R(1)], [P(2), R(2)], [P(3), R(3)], 'k--', 'LineWidth', 1);
    plot3([R(1), Q(1)], [R(2), Q(2)], [R(3), Q(3)], 'k--', 'LineWidth', 1);
    
    all_points = [A; B; C; D];
    labels = {point_A, point_B, point_C, point_D};
    scatter3(all_points(:,1), all_points(:,2), all_points(:,3), 30, 'k', 'filled');

    offset = 0.2;
    text(A(1)-offset, A(2), A(3)-offset, labels{1}, 'FontSize', 12);
    text(B(1), B(2)+offset, B(3), labels{2}, 'FontSize', 12);
    text(C(1)+offset, C(2)-offset, C(3), labels{3}, 'FontSize', 12);
    text(D(1), D(2), D(3)+offset, labels{4}, 'FontSize', 12);
    


    axis equal;
    axis off;
    view(azimuth, elevation);
    
    set(gcf, 'Color', 'white');
    
    
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

        camzoom(0.7);

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
    