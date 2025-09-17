
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_M, point_N, point_A1, point_H)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 2, 0];          
    B = [-2, 0, 0];         
    C = [2, 0, 0];          
    M = [(A(1)+C(1))/2, (A(2)+C(2))/2, (A(3)+C(3))/2];  
    M = [1, 1, 0];          

    
    
    t = 0.4;  
    N = [A(1) + t*(B(1)-A(1)), A(2) + t*(B(2)-A(2)), A(3) + t*(B(3)-A(3))];
    N = [-1.5,0.5 , 0];     

    
    
    
    
    
    h_x = 0.5;  
    H = [h_x, 0, 0];        

    
    
    
    
    
    
    AM_dist = sqrt((A(1)-M(1))^2 + (A(2)-M(2))^2 + (A(3)-M(3))^2);
    AN_dist = sqrt((A(1)-N(1))^2 + (A(2)-N(2))^2 + (A(3)-N(3))^2);

    
    
    

    
    A1 = [h_x, 0, 1.2];     



    hold on;

    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 2);  
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k--', 'LineWidth', 2);  

    
    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k-', 'LineWidth', 2);   

    
    plot3([N(1), B(1)], [N(2), B(2)], [N(3), B(3)], 'k-', 'LineWidth', 2);   
    plot3([M(1), C(1)], [M(2), C(2)], [M(3), C(3)], 'k-', 'LineWidth', 2);   

    
    plot3([A1(1), M(1)], [A1(2), M(2)], [A1(3), M(3)], 'k-', 'LineWidth', 2); 
    plot3([A1(1), N(1)], [A1(2), N(2)], [A1(3), N(3)], 'k-', 'LineWidth', 2); 

    
    plot3([A1(1), H(1)], [A1(2), H(2)], [A1(3), H(3)], 'k-', 'LineWidth', 2); 

    
    scatter3(A(1), A(2), A(3), 100, 'ko', 'filled');
    scatter3(A1(1), A1(2), A1(3), 100, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(M(1), M(2), M(3), 100, 'ko', 'filled');
    scatter3(N(1), N(2), N(3), 100, 'ko', 'filled');
    scatter3(H(1), H(2), H(3), 100, 'ko', 'filled');

    
    text(A(1)-0.1, A(2)+0.1, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1)-0.1, A1(2), A1(3)+0.1, point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)-0.1, B(2)-0.3, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)-0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)+0.1, M(2), M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    text(N(1)-0.1, N(2)+0.1, N(3), point_N, 'FontSize', 14, 'FontWeight', 'bold');
    text(H(1), H(2)-0.3, H(3), point_H, 'FontSize', 14, 'FontWeight', 'bold');



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
    