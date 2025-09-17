function visual(mode, azimuth, elevation, point_O)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 2;         
    h = 4;         
    l = sqrt(r^2 + h^2); 
    R = (r * h) / (r + l); 
    
    
    S = [0, 0, h];     
    O1 = [0, 0, 0];    
    A = [r, 0, 0];     
    B = [-r, 0, 0];    
    O = [0, 0, R];     
    
    
    t = (h^2 - h*R) / (r^2 + h^2);  
    C = [r*t, 0, h - h*t];          
    
    
    hold on;
    
    
    
    theta = linspace(0, 2*pi, 50);
    z = linspace(0, h, 20);
    [THETA, Z] = meshgrid(theta, z);
    R_z = r * (1 - Z/h);  
    X = R_z .* cos(THETA);
    Y = R_z .* sin(THETA);
    surf(X, Y, Z, 'FaceColor', [0.8 0.8 0.8], 'FaceAlpha', 0.3, 'EdgeAlpha', 0.1);
    
    
    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2); 
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2); 
    plot3([S(1), O1(1)], [S(2), O1(2)], [S(3), O1(3)], 'k-', 'LineWidth', 2); 
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5); 
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 1.5); 
    plot3([O(1), O1(1)], [O(2), O1(2)], [O(3), O1(3)], 'k--', 'LineWidth', 1.5); 
    
    
    
    theta = linspace(0, 2*pi, 100);
    circle_x = R * sin(theta);  
    circle_y = zeros(size(theta));  
    circle_z = R + R * cos(theta);  
    plot3(circle_x, circle_y, circle_z, 'k--', 'LineWidth', 2);
    
    
    base_theta = linspace(0, 2*pi, 100);
    base_x = r * cos(base_theta);
    base_y = r * sin(base_theta);
    base_z = zeros(size(base_theta));
    plot3(base_x, base_y, base_z, 'k-', 'LineWidth', 2);
    
    
   
    text(O(1)+0.1, O(2)+0.1, O(3)+0.1, point_O, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    

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
    