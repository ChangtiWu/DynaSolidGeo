
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_P)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    
    A = [-1, 0, 0];         
    B = [0, -sqrt(3), 0];   
    C = [1, 0, 0];          
    D = [0, sqrt(3), 0];    

    
    
    
    t1 = 0.5;  
    t2 = 0.5;  

    E = [A(1) + t1*(D(1)-A(1)), A(2) + t1*(D(2)-A(2)), A(3) + t1*(D(3)-A(3))];
    E = [-0.5, sqrt(3)/2, 0];  

    F = [A(1) + t2*(B(1)-A(1)), A(2) + t2*(B(2)-A(2)), A(3) + t2*(B(3)-A(3))];
    F = [-0.5, -sqrt(3)/2, 0]; 

    
    
    
    
    
    
    
    
    P = [-1, 0, 1.2];        



    hold on;

    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 2);   
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);  
    plot3([F(1), B(1)], [F(2), B(2)], [F(3), B(3)], 'k-', 'LineWidth', 2);   

    
    plot3([D(1), B(1)], [D(2), B(2)], [D(3), B(3)], 'k--', 'LineWidth', 2);   

    
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);  
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), E(1)], [P(2), E(2)], [P(3), E(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), F(1)], [P(2), F(2)], [P(3), F(3)], 'k-', 'LineWidth', 2);   

    
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(E(1), E(2), E(3), 100, 'ko', 'filled');
    scatter3(F(1), F(2), F(3), 100, 'ko', 'filled');
    scatter3(P(1), P(2), P(3), 100, 'ko', 'filled');

    
    text(B(1)-0.1, B(2)-0.3, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)-0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+0.1, D(2)+0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1)-0.1, E(2)+0.2, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1)-0.1, F(2)-0.2, F(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1)+0.1, P(2), P(3)+0.1, point_P, 'FontSize', 14, 'FontWeight', 'bold');



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
    