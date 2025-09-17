
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_O, point_P, point_E)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    O = [0, 0, 0];          
    A_original = [0, 1, 0]; 
    C = [0, -2, 0];         
    B = [-1, 0, 0];         
    D = [2, 0, 0];          

    
    
    
    
    
    
    
    
    
    
    
    
    
    P = [0, 0, 1];          

    
    
    t = 0.2;  
    E = [B(1) + t*(D(1)-B(1)), B(2) + t*(D(2)-B(2)), B(3) + t*(D(3)-B(3))];
    E = [-1 + t*3, 0, 0];   



    hold on;

    
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'k-', 'LineWidth', 2);  

    
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2);   

    
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);  
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 2);   
    plot3([P(1), O(1)], [P(2), O(2)], [P(3), O(3)], 'k--', 'LineWidth', 2);   

    
    scatter3(P(1), P(2), P(3), 100, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(O(1), O(2), O(3), 100, 'ko', 'filled');
    scatter3(E(1), E(2), E(3), 100, 'ko', 'filled');

    
    text(P(1)-0.05, P(2), P(3)+0.05, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.05, B(2)-0.05, B(3)+0.05, point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)-0.05, C(2)-0.05, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+0.05, D(2)-0.05, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(O(1)-0.05, O(2)+0.05, O(3), point_O, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1)-0.05, E(2)-0.05, E(3)-0.05, point_E, 'FontSize', 14, 'FontWeight', 'bold');



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
    