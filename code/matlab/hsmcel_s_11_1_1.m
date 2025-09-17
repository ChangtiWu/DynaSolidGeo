function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C)
    close all;
    fig = figure('Visible', 'off');

    alpha = 70; 
    beta = 60; 
    gamma = 80;
    len = 4;
    
    P = [0,0,0];
    A = [len, 0, 0];
    B = [len*cosd(alpha), len*sind(alpha), 0];
    
    x = len*cosd(gamma);
    y = len*(cosd(beta) - cosd(gamma)*cosd(alpha))/sind(alpha);
    z = sqrt(len^2 - x^2 - y^2);
    C = [x, y, z];
    
    M_ratio = 0.6;
    M = M_ratio * C;
    
    E_proj_vec = dot(M, B) / dot(B, B) * B;
    E = E_proj_vec;
    
    D_proj_vec = dot(M, A) / dot(A, A) * A;
    D = D_proj_vec;

    hold on;
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([M(1), A(1)], [M(2), A(2)], [M(3), A(3)], 'k-', 'LineWidth', 1.5);
    plot3([M(1), B(1)], [M(2), B(2)], [M(3), B(3)], 'k-', 'LineWidth', 1.5);

    plot3([M(1), D(1)], [M(2), D(2)], [M(3), D(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), E(1)], [M(2), E(2)], [M(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), E(1)], [P(2), E(2)], [P(3), E(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k--', 'LineWidth', 1.5);

    all_points_labels = {point_P, point_A, point_B, point_C};
    all_points_coords = {P, A, B, C};
    offsets = {[-0.3, -0.3, 0], [0.2, -0.1, 0], [0.1, 0.3, 0], [-0.1, 0.2, 0.2]};

    for i = 1:length(all_points_coords)
        pt = all_points_coords{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
        text(pt(1)+offsets{i}(1), pt(2)+offsets{i}(2), pt(3)+offsets{i}(3), ...
             all_points_labels{i}, 'FontSize', 12, 'FontWeight', 'bold', 'Interpreter', 'tex');
    end

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
    