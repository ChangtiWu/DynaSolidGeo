function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C)
    close all;
    fig = figure('Visible', 'off');

    s = 4;
    
    V0 = [0, 0, 0];
    V1 = [s, 0, 0];
    V2 = [0, s, 0];
    V3 = [0, 0, s];
    V4 = [s, s, 0];
    V5 = [s, 0, s];
    V6 = [0, s, s];
    V7 = [s, s, s];
    
    P = V0;
    A = V4;
    B = V5;
    C = V6;
    

    hold on;

    plot3([V0(1), V1(1)], [V0(2), V1(2)], [V0(3), V1(3)], 'k--', 'LineWidth', 2);
    plot3([V0(1), V2(1)], [V0(2), V2(2)], [V0(3), V2(3)], 'k--', 'LineWidth', 2);
    plot3([V0(1), V3(1)], [V0(2), V3(2)], [V0(3), V3(3)], 'k--', 'LineWidth', 2);

    plot3([V1(1), V4(1)], [V1(2), V4(2)], [V1(3), V4(3)], 'k--', 'LineWidth', 2);
    plot3([V1(1), V5(1)], [V1(2), V5(2)], [V1(3), V5(3)], 'k--', 'LineWidth', 2);
    plot3([V2(1), V4(1)], [V2(2), V4(2)], [V2(3), V4(3)], 'k--', 'LineWidth', 2);
    plot3([V2(1), V6(1)], [V2(2), V6(2)], [V2(3), V6(3)], 'k--', 'LineWidth', 2);
    plot3([V3(1), V5(1)], [V3(2), V5(2)], [V3(3), V5(3)], 'k--', 'LineWidth', 2);
    plot3([V3(1), V6(1)], [V3(2), V6(2)], [V3(3), V6(3)], 'k--', 'LineWidth', 2);
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k--', 'LineWidth', 1.5);


    all_points_labels = {point_P, point_A, point_B, point_C};
    all_points_coords = {P, V4, V5, V6};
    offsets = {[-0.3, -0.3, 0], [0.2, 0.2, 0], [0.2, -0.3, 0], [-0.3, 0.2, 0]};

    for i = 1:length(all_points_coords)
        pt = all_points_coords{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
        text(pt(1)+offsets{i}(1), pt(2)+offsets{i}(2), pt(3)+offsets{i}(3), ...
             all_points_labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
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
    