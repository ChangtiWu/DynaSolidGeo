
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_G, point_M)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];          
    B = [3, 0, 0];          
    C = [3, 2, 0];          
    D = [0, 2, 0];          
    E = [1, 0, 0];          

    
    
    
    
    t1 = 0.6;  
    t2 = 0.4;  

    F = [1 + t1*2, 0, 0];   
    G = [3, t2*2, 0];       
    L = [2.5,1.5,0];
    P = [2,2,0];

    
    
    
    
    
    
    
    
    
    
    
    
    

    
    M = [2.6, 0.4, 1];    



    hold on;

    
    plot3([A(1), F(1)], [A(2), F(2)], [A(3),F(3)], 'k-', 'LineWidth', 2);   
    plot3([A(1), M(1)], [A(2), M(2)], [A(3),M(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), M(1)], [D(2), M(2)], [D(3),M(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), L(1)], [C(2), L(2)], [C(3), L(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), P(1)], [C(2), P(2)], [C(3), P(3)], 'k-', 'LineWidth', 2);

    
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), E(1)], [C(2), E(2)], [C(3), E(3)], 'k--', 'LineWidth', 2);  

    
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);   
    plot3([G(1), C(1)], [G(2), C(2)], [G(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([F(1), G(1)], [F(2), G(2)], [F(3), G(3)], 'k-', 'LineWidth', 2);   

    
    plot3([M(1), F(1)], [M(2), F(2)], [M(3), F(3)], 'k-', 'LineWidth', 2);   
    plot3([M(1), G(1)], [M(2), G(2)], [M(3), G(3)], 'k-', 'LineWidth', 2);   

    
    plot3([D(1), F(1)], [D(2), F(2)], [D(3), F(3)], 'k--', 'LineWidth', 2);  

    
    scatter3(A(1), A(2), A(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(E(1), E(2), E(3), 100, 'ko', 'filled');
    scatter3(F(1), F(2), F(3), 100, 'ko', 'filled');
    scatter3(G(1), G(2), G(3), 100, 'ko', 'filled');
    scatter3(M(1), M(2), M(3), 100, 'ko', 'filled');

    
    text(A(1)-0.1, A(2)-0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)+0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1), E(2)-0.2, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1), F(2)-0.2, F(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(G(1)+0.1, G(2), G(3), point_G, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)+0.1, M(2), M(3)+0.1, point_M, 'FontSize', 14, 'FontWeight', 'bold');



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
    