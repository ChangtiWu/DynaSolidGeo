function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_A2, point_B2, point_D2, point_C2, point_P)
    close all;
    fig = figure('Visible', 'off');
    
    AB = 2;
    AA1 = 4;
    
    D = [0, 0, 0];
    A = [AB, 0, 0];
    C = [0, AB, 0];
    B = [AB, AB, 0];
    
    D1 = D + [0, 0, AA1];
    A1 = A + [0, 0, AA1];
    C1 = C + [0, 0, AA1];
    B1 = B + [0, 0, AA1];
    
    AA2 = 1;
    BB2 = 2;
    CC2 = 3;
    DD2 = 2;
    
    A2 = A + [0, 0, AA2];
    B2 = B + [0, 0, BB2];
    C2 = C + [0, 0, CC2];
    D2 = D + [0, 0, DD2];
    
    p_z = 3.5;
    P = [B(1), B(2), p_z];
    
    hold on;
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), D1(1)], [A1(2), D1(2)], [A1(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([C1(1), D1(1)], [C1(2), D1(2)], [C1(3), D1(3)], 'k-', 'LineWidth', 2);
    
    patch([P(1), A2(1), C2(1)], [P(2), A2(2), C2(2)], [P(3), A2(3), C2(3)], [0.7 0.7 1.0], 'FaceAlpha', 0.2);
    patch([D2(1), A2(1), C2(1)], [D2(2), A2(2), C2(2)], [D2(3), A2(3), C2(3)], [0.7 1.0 0.7], 'FaceAlpha', 0.2);
    
    plot3([A2(1), B2(1)], [A2(2), B2(2)], [A2(3), B2(3)], 'r--', 'LineWidth', 1);
    plot3([B2(1), C2(1)], [B2(2), C2(2)], [B2(3), C2(3)], 'r--', 'LineWidth', 1);
    plot3([C2(1), D2(1)], [C2(2), D2(2)], [C2(3), D2(3)], 'r--', 'LineWidth', 1);
    plot3([D2(1), A2(1)], [D2(2), A2(2)], [D2(3), A2(3)], 'r--', 'LineWidth', 1);
    plot3([A2(1), C2(1)], [A2(2), C2(2)], [A2(3), C2(3)], 'r--', 'LineWidth', 1.5);
    
    all_points = {A, B, C, D, A1, B1, C1, D1, A2, B2, C2, D2, P};
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter3(pt(1), pt(2), pt(3), 40, 'k', 'filled');
    end
    
    text(A(1)+0.1, A(2)-0.25, A(3), point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)+0.1, B(3), point_B, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1)-0.3, C(2)+0.1, C(3), point_C, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1)-0.2, D(2)-0.25, D(3), point_D, 'FontSize', 12, 'FontWeight', 'bold');
    text(A1(1)+0.1, A1(2)-0.25, A1(3), point_A1, 'FontSize', 12, 'FontWeight', 'bold');
    text(B1(1)+0.1, B1(2)+0.1, B1(3), point_B1, 'FontSize', 12, 'FontWeight', 'bold');
    text(C1(1)-0.3, C1(2)+0.1, C1(3), point_C1, 'FontSize', 12, 'FontWeight', 'bold');
    text(D1(1)-0.2, D1(2)-0.25, D1(3), point_D1, 'FontSize', 12, 'FontWeight', 'bold');
    text(A2(1)+0.15, A2(2)-0.25, A2(3), point_A2, 'FontSize', 12, 'FontWeight', 'bold');
    text(B2(1)+0.15, B2(2)+0.15, B2(3), point_B2, 'FontSize', 12, 'FontWeight', 'bold');
    text(C2(1)-0.35, C2(2)+0.15, C2(3), point_C2, 'FontSize', 12, 'FontWeight', 'bold');
    text(D2(1)-0.3, D2(2)-0.2, D2(3), point_D2, 'FontSize', 12, 'FontWeight', 'bold');
    text(P(1)+0.15, P(2)+0.15, P(3), point_P, 'FontSize', 12, 'FontWeight', 'bold');

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
    