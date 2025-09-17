function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1)
    close all;
    fig = figure('Visible', 'off');

    AC_len = sqrt(2);
    A1C_len = sqrt(2);
    BC_len = 2;
    
    C = [0, 0, 0];
    B = [BC_len, 0, 0];
    A = [0, AC_len, 0];
    A1 = [0, 0, A1C_len];
    
    vec_AA1 = A1 - A;
    C1 = C + vec_AA1;
    B1 = B + vec_AA1;

    hold on;

    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), C1(1)], [A1(2), C1(2)], [A1(3), C1(3)], 'k-', 'LineWidth', 2);
    
    plot3([A1(1), C(1)], [A1(2), C(2)], [A1(3), C(3)], 'k--', 'LineWidth', 2);
    
    all_points = {A, B, C, A1, B1, C1};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
    end
    
    text(A(1), A(2)+0.2, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2), B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)-0.2, C(2)-0.2, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(A1(1), A1(2), A1(3)+0.2, point_A1, 'FontSize', 12, 'FontWeight', 'bold');
    text(B1(1)+0.2, B1(2), B1(3), point_B1, 'FontSize', 12, 'FontWeight', 'bold');
    text(C1(1), C1(2)-0.3, C1(3), point_C1, 'FontSize', 12, 'FontWeight', 'bold');

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
    