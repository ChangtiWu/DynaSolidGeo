
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_M, point_N, point_P, point_T)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];          
    B = [2, 0, 0];          
    C = [2, 2, 0];          
    D = [0, 2, 0];          
    M = [2, 1, 0];          
    N = [1, 2, 0];          

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    T = [1,1,0.5];
    P = [4/3, 4/3, 2/3];    



    hold on;

    
  
    plot3([M(1), C(1)], [M(2), C(2)], [M(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), N(1)], [C(2), N(2)], [C(3), N(3)], 'k-', 'LineWidth', 2);   
    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k--', 'LineWidth', 2);   

    
    plot3([A(1), M(1)], [A(2), M(2)], [A(3), M(3)], 'k-', 'LineWidth', 2);  
    plot3([A(1), N(1)], [A(2), N(2)], [A(3), N(3)], 'k-', 'LineWidth', 2);  

    
    plot3([A(1), P(1)], [A(2), P(2)], [A(3), P(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), M(1)], [P(2), M(2)], [P(3), M(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), N(1)], [P(2), N(2)], [P(3), N(3)], 'k-', 'LineWidth', 2);   
    plot3([T(1), N(1)], [T(2), N(2)], [T(3), N(3)], 'k--', 'LineWidth', 2);   
    plot3([T(1), M(1)], [T(2), M(2)], [T(3), M(3)], 'k--', 'LineWidth', 2);   

    
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);  

    
    scatter3(A(1), A(2), A(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(T(1), T(2), T(3), 100, 'ko', 'filled');
    scatter3(M(1), M(2), M(3), 100, 'ko', 'filled');
    scatter3(N(1), N(2), N(3), 100, 'ko', 'filled');
    scatter3(P(1), P(2), P(3), 100, 'ko', 'filled');

    
    text(A(1)-0.3, A(2)-0.1, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)+0.1, M(2), M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    text(N(1), N(2)+0.1, N(3), point_N, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1)+0.1, P(2), P(3)+0.1, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(T(1)+0.1, T(2), T(3)+0.2, point_T, 'FontSize', 14, 'FontWeight', 'bold');



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
    