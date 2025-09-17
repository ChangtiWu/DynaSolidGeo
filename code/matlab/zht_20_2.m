
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_A1)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    A = [0, 0, 0];          
    B = [4, 0, 0];          
    C = [5, 3, 0];          
    D = [1, 3, 0];          

    
    E = [2, 0, 0];

  
    
    
    A_prime = [2, 2, 1.2];  

    
    F = [3.5, 2.5, 0.6];


    hold on;

    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);  
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);  
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);  
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2); 

    
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 2);  

    
    plot3([A_prime(1), D(1)], [A_prime(2), D(2)], [A_prime(3), D(3)], 'k-', 'LineWidth', 2);  
    plot3([A_prime(1), E(1)], [A_prime(2), E(2)], [A_prime(3), E(3)], 'k-', 'LineWidth', 2);  

    
    plot3([A_prime(1), C(1)], [A_prime(2), C(2)], [A_prime(3), C(3)], 'k-', 'LineWidth', 2);  

    
    plot3([F(1), B(1)], [F(2), B(2)], [F(3), B(3)], 'k--', 'LineWidth', 2); 

    
    text(A(1)-0.2, A(2)-0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.2, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.2, D(2)+0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1), E(2)-0.2, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(A_prime(1)-0.2, A_prime(2), A_prime(3)+0.1, point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    

    
    scatter3(A(1), A(2), A(3), 50, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 50, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 50, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 50, 'ko', 'filled');
    scatter3(E(1), E(2), E(3), 50, 'ko', 'filled');
    scatter3(A_prime(1), A_prime(2), A_prime(3), 50, 'ko', 'filled');
    scatter3(F(1), F(2), F(3), 50, 'ko', 'filled');


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
    