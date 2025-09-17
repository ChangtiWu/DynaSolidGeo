function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_M)
    close all;
    fig = figure('Visible', 'off');
    
    AD = 2;
    AB = 1;
    BC = 1;
    
    A = [0, 0, 0];
    B = [AB, 0, 0];
    D = [0, AD, 0];
    C = [AB, AD - BC, 0];
    
    h = sqrt(AD^2 - (AD/2)^2);
    P_proj = [0, AD/2, 0];
    P = [P_proj(1), P_proj(2), h];
    
    E = (P + D) / 2;
    
    k = 1 - 1/sqrt(2);
    M = (1-k)*P + k*C;
    
    hold on;
    
    patch([P(1), A(1), B(1)], [P(2), A(2), B(2)], [P(3), A(3), B(3)], 'c', 'FaceAlpha', 0.2);
    patch([M(1), A(1), B(1)], [M(2), A(2), B(2)], [M(3), A(3), B(3)], 'm', 'FaceAlpha', 0.3);
    patch([A(1), B(1), C(1), D(1)], [A(2), B(2), C(2), D(2)], [A(3), B(3), C(3), D(3)], 'y', 'FaceAlpha', 0.1);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2);
    
    plot3([C(1), E(1)], [C(2), E(2)], [C(3), E(3)], 'b-', 'LineWidth', 2.5);
    plot3([B(1), M(1)], [B(2), M(2)], [B(3), M(3)], 'r-', 'LineWidth', 2.5);
    
    all_points = {A, B, C, D, P, E, M};

    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    
    text(A(1)-0.1, A(2)-0.1, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)+0.1, D(3), point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(P(1), P(2), P(3)+0.1, point_P, 'FontSize', 12, 'FontWeight', 'bold');

    text(M(1), M(2)+0.1, M(3), point_M, 'FontSize', 12, 'FontWeight', 'bold');
    
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
    