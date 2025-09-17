function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_O, point_BC, point_M, point_P)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    AB_len = 1;                
    AC_len = AB_len;           
    AA1_len = 2 * AB_len;      
    
    
    A = [0, 0, 0];
    B = [AB_len, 0, 0];
    C = [0, AC_len, 0];
    O = (B + C) / 2;           
    
    
    
    A1 = [O(1), O(2), AA1_len];
    
    B1 = [A1(1) + (B(1) - A(1)), A1(2) + (B(2) - A(2)), A1(3)];
    C1 = [A1(1) + (C(1) - A(1)), A1(2) + (C(2) - A(2)), A1(3)];
    
    
    M = (B1 + C1) / 2;
    
    

    hold on;
    
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([A1(1), C1(1)], [A1(2), C1(2)], [A1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A1(1), M(1)], [A1(2), M(2)], [A1(3), M(3)], 'k-', 'LineWidth', 2);
    
    
    
    plot3([A1(1), B(1)], [A1(2), B(2)], [A1(3), B(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), O(1)], [A(2), O(2)], [A(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([A1(1), C(1)], [A1(2), C(2)], [A1(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([M(1), C(1)], [M(2), C(2)], [M(3), C(3)], 'k--', 'LineWidth', 1.5);
    
    text(A(1)-0.1, A(2)-0.1, A(3), point_A, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(C(1)-0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(O(1), O(2)+0.1, O(3), point_O, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(A1(1)-0.1, A1(2)-0.1, A1(3)+0.1, point_A1, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(B1(1)+0.1, B1(2)-0.1, B1(3)+0.1, point_B1, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(C1(1)-0.1, C1(2)+0.1, C1(3)+0.1, point_C1, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(M(1), M(2)+0.1, M(3)+0.1, point_M, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');


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
    