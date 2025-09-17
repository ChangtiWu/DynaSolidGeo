function visual(mode, azimuth, elevation, point_E, point_A, point_B, point_C, point_D, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    v1 = [1, 1, 1];   
    v2 = [-1, 1, 1];  
    v3 = [1, -1, 1];  
    v4 = [-1, -1, 1]; 
    v5 = [1, 1, -1];  
    v6 = [-1, 1, -1]; 
    v7 = [1, -1, -1]; 
    v8 = [-1, -1, -1];
    
    
    B = [-1, 0, 0];   
    D = [1, 0, 0];    
    A = [0, -1, 0];   
    E = [0, 0, 1];    
    C = [0, 1, 0];    
    F = [0, 0, -1];   
    
    

    hold on;

    
    
    
    plot3([v1(1), v2(1)], [v1(2), v2(2)], [v1(3), v2(3)], 'k--', 'LineWidth', 1.5);
    plot3([v2(1), v4(1)], [v2(2), v4(2)], [v2(3), v4(3)], 'k--', 'LineWidth', 1.5);
    plot3([v4(1), v3(1)], [v4(2), v3(2)], [v4(3), v3(3)], 'k--', 'LineWidth', 1.5);
    plot3([v3(1), v1(1)], [v3(2), v1(2)], [v3(3), v1(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([v5(1), v6(1)], [v5(2), v6(2)], [v5(3), v6(3)], 'k--', 'LineWidth', 1.5);
    plot3([v6(1), v8(1)], [v6(2), v8(2)], [v6(3), v8(3)], 'k--', 'LineWidth', 1.5);
    plot3([v8(1), v7(1)], [v8(2), v7(2)], [v8(3), v7(3)], 'k--', 'LineWidth', 1.5);
    plot3([v7(1), v5(1)], [v7(2), v5(2)], [v7(3), v5(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([v1(1), v5(1)], [v1(2), v5(2)], [v1(3), v5(3)], 'k--', 'LineWidth', 1.5);
    plot3([v2(1), v6(1)], [v2(2), v6(2)], [v2(3), v6(3)], 'k--', 'LineWidth', 1.5);
    plot3([v3(1), v7(1)], [v3(2), v7(2)], [v3(3), v7(3)], 'k--', 'LineWidth', 1.5);
    plot3([v4(1), v8(1)], [v4(2), v8(2)], [v4(3), v8(3)], 'k--', 'LineWidth', 1.5);
    
    
    
    plot3([E(1), A(1)], [E(2), A(2)], [E(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), B(1)], [E(2), B(2)], [E(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), C(1)], [E(2), C(2)], [E(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), D(1)], [E(2), D(2)], [E(3), D(3)], 'k--', 'LineWidth', 2);
    
    
    plot3([F(1), A(1)], [F(2), A(2)], [F(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([F(1), B(1)], [F(2), B(2)], [F(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([F(1), C(1)], [F(2), C(2)], [F(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([F(1), D(1)], [F(2), D(2)], [F(3), D(3)], 'k--', 'LineWidth', 2);
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k--', 'LineWidth', 2);
    
    
    text(E(1)+0.05, E(2)+0.05, E(3)+0.05, point_E, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(F(1)+0.05, F(2)+0.05, F(3)+0.05, point_F, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(A(1)+0.05, A(2)+0.05, A(3)+0.05, point_A, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(B(1)+0.05, B(2)+0.05, B(3)+0.05, point_B, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(C(1)+0.05, C(2)+0.05, C(3)+0.05, point_C, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(D(1)+0.05, D(2)+0.05, D(3)+0.05, point_D, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');




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
    