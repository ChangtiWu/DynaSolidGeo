function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_E, point_F, point_T)





    close all;
    fig = figure('Visible', 'off');
    
    
    A = [0, 0, 0];
    B = [2, 0, 0];
    C = [2, 2, 0];
    D = [0, 2, 0];
    
    
    P = [0, 0, 2];

    hold on;
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2);
    
    
    E = [1, 2, 0];      
    F = [1, 1, 1];      
    T = [1.5, 0, 0.2];      
    
    
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([T(1), C(1)], [T(2), C(2)], [T(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1), F(1)], [B(2), F(2)], [B(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), A(1)], [E(2), A(2)], [E(3), A(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2); 
    
    
    
    offset = 0.1;
    text(A(1), A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+offset, B(2)+offset, B(3)+offset, point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+offset, C(2)+offset, C(3)+offset, point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+offset, D(2)+offset, D(3)+offset, point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1)+offset, P(2)+offset, P(3)+offset, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1)+offset, E(2)+offset, E(3)+offset, point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1)+offset, F(2)+offset, F(3)+offset, point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(T(1), T(2), T(3), point_T, 'FontSize', 14, 'FontWeight', 'bold');
    
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
    