
function visual(mode, azimuth, elevation, point_V, point_A, point_B, point_C, point_E, point_F)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    edge_length = 4;    

    
    
    triangle_side = 3;  
    height_2d = triangle_side * sqrt(3) / 2;  

    A = [-triangle_side/2, -height_2d/3, 0];
    B = [triangle_side/2, -height_2d/3, 0];
    C = [0, 2*height_2d/3, 0];

    
    
    
    
    center_to_vertex = sqrt((A(1))^2 + (A(2))^2);  
    V_height = sqrt(edge_length^2 - center_to_vertex^2);  
    V = [0, 0, V_height];

    
    
    t_E = 0.4;  
    t_F = 0.6;  
    E = V + t_E * (C - V);
    F = V + t_F * (B - V);


    hold on;

    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), A(1)], [C(2), A(2)], [C(3), A(3)], 'k-', 'LineWidth', 2);  

    
    plot3([V(1), A(1)], [V(2), A(2)], [V(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), B(1)], [V(2), B(2)], [V(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), C(1)], [V(2), C(2)], [V(3), C(3)], 'k-', 'LineWidth', 2);

    
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k--', 'LineWidth', 2);  
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 2);  
    plot3([F(1), A(1)], [F(2), A(2)], [F(3), A(3)], 'k--', 'LineWidth', 2); 

    
    text(A(1)-0.3, A(2)-0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2)-0.2, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.2, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(V(1), V(2), V(3)+0.3, point_V, 'FontSize', 14, 'FontWeight', 'bold');

    
    text(E(1)+0.2, E(2), E(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1)-0.2, F(2)+0.2, F(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');

    
    scatter3(A(1), A(2), A(3), 50, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 50, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 50, 'ko', 'filled');
    scatter3(V(1), V(2), V(3), 50, 'ko', 'filled');

    
    scatter3(E(1), E(2), E(3), 50, 'ko', 'filled');
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
    