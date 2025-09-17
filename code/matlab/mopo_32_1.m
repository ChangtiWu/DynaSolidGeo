function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_B_prime, point_K)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    B = [0, 0, 0];
    C = [4, 0, 0];         
    A = [1, 2, 0];         
    D = [5, 2, 0];         
    E = [3, 0, 0];         
    
    
    K = [0.5, 0.5, 0];     
    B_prime = [K(1), K(2), 2];  
    
    

    hold on;

    
    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);  
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);  
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);  
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5);  
    
    
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k-', 'LineWidth', 2);  
    plot3([A(1), B_prime(1)], [A(2), B_prime(2)], [A(3), B_prime(3)], 'k-', 'LineWidth', 2);  
    
    
    plot3([E(1), B_prime(1)], [E(2), B_prime(2)], [E(3), B_prime(3)], 'k-', 'LineWidth', 2);  
    
    
    plot3([B_prime(1), K(1)], [B_prime(2), K(2)], [B_prime(3), K(3)], 'k--', 'LineWidth', 1.5);  
    
    
    text(B(1), B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1), E(2), E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1), A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1), D(2), D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(B_prime(1), B_prime(2), B_prime(3), point_B_prime, 'FontSize', 14, 'FontWeight', 'bold');
    text(K(1), K(2), K(3), point_K, 'FontSize', 14, 'FontWeight', 'bold');
    
    hold off;  

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
    