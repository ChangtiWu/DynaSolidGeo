
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_M, point_N, point_E, point_F, point_P)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];          
    B = [0, 3, 0];          
    C = [4, 3, 0];          
    D = [3, 1, 0];          
    M = [2, 1, 0];          
    N = [2, 3, 0];          

    
    
    
    
    
    
    h = 1.5;  

    
    
    E = [2, 1, h];          
    F = [2, 3, h];          

    
    t = 0.4;  
    P = [F(1) + t*(C(1)-F(1)), F(2) + t*(C(2)-F(2)), F(3) + t*(C(3)-F(3))];
    P = [3, 3, 0.75];        



    hold on;

    
    plot3([M(1), D(1)], [M(2), D(2)], [M(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), N(1)], [C(2), N(2)], [C(3), N(3)], 'k-', 'LineWidth', 2);   
    plot3([F(1), D(1)], [F(2), D(2)], [F(3), D(3)], 'k--', 'LineWidth', 2);   

    
    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k-', 'LineWidth', 2);  

    
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);   
    plot3([E(1), M(1)], [E(2), M(2)], [E(3), M(3)], 'k-', 'LineWidth', 2);   
    plot3([F(1), N(1)], [F(2), N(2)], [F(3), N(3)], 'k-', 'LineWidth', 2);   
    plot3([F(1), C(1)], [F(2), C(2)], [F(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([N(1), D(1)], [N(2), D(2)], [N(3), D(3)], 'k--', 'LineWidth', 2);   
    
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k--', 'LineWidth', 2);  
    plot3([P(1), N(1)], [P(2), N(2)], [P(3), N(3)], 'k--', 'LineWidth', 2);  

    
    plot3([E(1), D(1)], [E(2), D(2)], [E(3), D(3)], 'k-', 'LineWidth', 2);  

    
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(E(1), E(2), E(3), 100, 'ko', 'filled');
    scatter3(F(1), F(2), F(3), 100, 'ko', 'filled');
    scatter3(M(1), M(2), M(3), 100, 'ko', 'filled');
    scatter3(N(1), N(2), N(3), 100, 'ko', 'filled');
    scatter3(P(1), P(2), P(3), 100, 'ko', 'filled');

    
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)-0.3, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1)-0.1, E(2), E(3)+0.1, point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1)+0.1, F(2), F(3)+0.1, point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)-0.1, M(2)-0.3, M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    text(N(1)+0.1, N(2), N(3), point_N, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1)+0.1, P(2)+0.1, P(3), point_P, 'FontSize', 14, 'FontWeight', 'bold');



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

        camzoom(0.7);

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
    