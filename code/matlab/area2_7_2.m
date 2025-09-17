function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    

    
    
    side_bottom = 2;     
    height = 4;          
    O = [0, 0, 0];       
    O_prime = [0, 0, height/2]; 
    P = [0, 0, height];  
    
    
    theta_bottom = linspace(0, 2*pi, 7); 
    x_bottom = side_bottom * cos(theta_bottom);
    y_bottom = side_bottom * sin(theta_bottom);
    z_bottom = zeros(size(theta_bottom));
    
    
    side_top = side_bottom / 2;
    theta_top = linspace(0, 2*pi, 7);
    x_top = side_top * cos(theta_top);
    y_top = side_top * sin(theta_top);
    z_top = height/2 * ones(size(theta_top));
    
    

    hold on;

    
    
    
    plot3(x_bottom(1:7), y_bottom(1:7), z_bottom(1:7), 'k-', 'LineWidth', 2);
    
    
    plot3(x_top(1:7), y_top(1:7), z_top(1:7), 'k-', 'LineWidth', 2);
    
    
    for i = 1:6
        plot3([P(1), x_bottom(i)], [P(2), y_bottom(i)], [P(3), z_bottom(i)], 'k-', 'LineWidth', 2);
    end
    
    
    for i = 1:7
        plot3([x_top(i), x_bottom(i)], [y_top(i), y_bottom(i)], [z_top(i), z_bottom(i)], 'k-', 'LineWidth', 2);
    end
    
    
    
    for i = 1:6
        plot3([P(1), x_top(i)], [P(2), y_top(i)], [P(3), z_top(i)], 'k--', 'LineWidth', 1.5);
    end
    
    
    plot3([P(1), O(1)], [P(2), O(2)], [P(3), O(3)], 'k--', 'LineWidth', 1.5);
    
    
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
    