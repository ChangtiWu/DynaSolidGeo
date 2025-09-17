
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_O)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    O = [0, 0, 1.5];        
    D = [-1, -0.5, 0];      
    E = [-0.5, 1, 0];          
    F = [1, -0.5, 0];       



    hold on;

    
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 2);   
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);   
    plot3([F(1), D(1)], [F(2), D(2)], [F(3), D(3)], 'k-', 'LineWidth', 2);  

    
    plot3([O(1), D(1)], [O(2), D(2)], [O(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([O(1), E(1)], [O(2), E(2)], [O(3), E(3)], 'k-', 'LineWidth', 2);   
    plot3([O(1), F(1)], [O(2), F(2)], [O(3), F(3)], 'k-', 'LineWidth', 2);   

    
    scatter3(O(1), O(2), O(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(E(1), E(2), E(3), 100, 'ko', 'filled');
    scatter3(F(1), F(2), F(3), 100, 'ko', 'filled');

    
    text(O(1)-0.1, O(2), O(3)+0.1, point_O, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)-0.1, D(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1)-0.1, E(2)+0.1, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1)+0.1, F(2)+0.1, F(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');



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
    