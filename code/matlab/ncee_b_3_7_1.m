function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_O)
    close all;
    fig = figure('Visible', 'off');

    AC_len = 4;
    BC_len = 2*sqrt(2);
    PC_len = 4;
    
    O = [0, 0, 0];
    A = [-AC_len/2, 0, 0];
    C = [AC_len/2, 0, 0];
    
    BO_len = sqrt(BC_len^2 - (AC_len/2)^2);
    PO_len = sqrt(PC_len^2 - (AC_len/2)^2);
    
    B = [0, BO_len, 0];
    P = [0, 0, PO_len];
    
    M = B + (1/3)*(C - B);

    hold on;

    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);

    plot3([P(1), O(1)], [P(2), O(2)], [P(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), M(1)], [O(2), M(2)], [O(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([P(1), M(1)], [P(2), M(2)], [P(3), M(3)], 'k-', 'LineWidth', 1.5);
    
    all_points = {A, B, C, P, O, M};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'ko', 'filled');
    end
    
    text(A(1)-0.3, A(2), A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1), B(2)+0.2, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2), C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(P(1), P(2), P(3)+0.2, point_P, 'FontSize', 12, 'FontWeight', 'bold');
    text(O(1)-0.2, O(2)-0.3, O(3), point_O, 'FontSize', 12, 'FontWeight', 'bold');
    
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
    