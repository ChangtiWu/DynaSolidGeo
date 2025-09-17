
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    B = [0, 0, 0];          
    C = [3, 0, 0];          
    D = [3, 3, 0];          
    A_original = [0, 2, 0]; 

    
    AB_dist = sqrt((A_original(1)-B(1))^2 + (A_original(2)-B(2))^2 + (A_original(3)-B(3))^2);
    AD_dist = sqrt((A_original(1)-D(1))^2 + (A_original(2)-D(2))^2 + (A_original(3)-D(3))^2);

    
    
    
    
    A_original = [0, 3-sqrt(7), 0]; 

    
    
    A_original = [0, 2, 0];  
    B = [0, 0, 0];           
    
    
    
    D = [2*sqrt(3), 4, 0];   
    C = [3, 0, 0];           

    
    A_original = [0, 3, 0];  
    B = [0, 0, 0];           
    C = [4, 0, 0];           
    D = [4, 3, 0];           

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    AD_original = sqrt((A_original(1)-D(1))^2 + (A_original(2)-D(2))^2);

    
    A_prime = [1.5, 1, 1.2]; 
    H = [A_prime(1), A_prime(2), 0]; 



    hold on;

    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([D(1), B(1)], [D(2), B(2)], [D(3), B(3)], 'k--', 'LineWidth', 2);  

    
    plot3([A_original(1), B(1)], [A_original(2), B(2)], [A_original(3), B(3)], 'k--', 'LineWidth', 1);  
    plot3([A_original(1), D(1)], [A_original(2), D(2)], [A_original(3), D(3)], 'k--', 'LineWidth', 1);  

    
    plot3([A_prime(1), B(1)], [A_prime(2), B(2)], [A_prime(3), B(3)], 'k-', 'LineWidth', 2);   
    plot3([A_prime(1), D(1)], [A_prime(2), D(2)], [A_prime(3), D(3)], 'k-', 'LineWidth', 2);   

    
    plot3([A_prime(1), C(1)], [A_prime(2), C(2)], [A_prime(3), C(3)], 'k-', 'LineWidth', 2);  

    
    plot3([A_prime(1), H(1)], [A_prime(2), H(2)], [A_prime(3), H(3)], 'k:', 'LineWidth', 2);  

    
    scatter3(A_original(1), A_original(2), A_original(3), 50, 'ko');  
    scatter3(A_prime(1), A_prime(2), A_prime(3), 100, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(H(1), H(2), H(3), 50, 'ko', 'filled');  

    
    text(A_original(1)-0.1, A_original(2)+0.1, A_original(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(A_prime(1)-0.1, A_prime(2), A_prime(3)+0.2, point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)-0.1, B(2)-0.3, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)-0.3, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+0.1, D(2)+0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');



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
    