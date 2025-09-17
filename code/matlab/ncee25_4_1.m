function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    R = 4;
    H = 9;
    
    
    r = 5 / 2;  

    
    
    
    
    
    C1 = [-(R - r), 0, r];        
    C2 = [(R - r), 0, H - r];     

    
    [X, Y, Z] = cylinder(R, 50);
    Z = Z * H; 

    
    [x1, y1, z1] = sphere(30);
    x1 = r * x1 + C1(1);
    y1 = r * y1 + C1(2);
    z1 = r * z1 + C1(3);

    [x2, y2, z2] = sphere(30);
    x2 = r * x2 + C2(1);
    y2 = r * y2 + C2(2);
    z2 = r * z2 + C2(3);

    
    
    theta = linspace(0, 2*pi, 50);
    
    x_ball1 = r * cos(theta);
    y_ball1 = r * sin(theta);
    z_ball1 = r * ones(size(theta));
    
    x_ball2 = r * cos(theta);
    y_ball2 = r * sin(theta);
    z_ball2 = (H - r) * ones(size(theta));


    hold on;

    
    surf(X, Y, Z, 'FaceColor', 'blue', 'FaceAlpha', 0.2, 'EdgeColor', 'none');
    

    
    
    plot3(X(1,:), Y(1,:), Z(1,:), 'k-', 'LineWidth', 2); 
    plot3(X(2,:), Y(2,:), Z(2,:), 'k-', 'LineWidth', 2); 

    
    angles = [0, pi/2, pi, 3*pi/2];
    for i = 1:4
        x_line = [R * cos(angles(i)), R * cos(angles(i))];
        y_line = [R * sin(angles(i)), R * sin(angles(i))];
        z_line = [0, H];
        if i == 1 || i == 2
            
            plot3(x_line, y_line, z_line, 'k-', 'LineWidth', 2);
        else
            
            plot3(x_line, y_line, z_line, 'k--', 'LineWidth', 1);
        end
    end

    
    plot3(x_ball1, y_ball1, z_ball1, 'k--', 'LineWidth', 1.5);
    plot3(x_ball2, y_ball2, z_ball2, 'k--', 'LineWidth', 1.5);

    
    scatter3(C1(1), C1(2), C1(3), 100, 'ko', 'filled');
    
    scatter3(C2(1), C2(2), C2(3), 100, 'ko', 'filled');
    

    
    plot3([C1(1), C2(1)], [C1(2), C2(2)], [C1(3), C2(3)], 'k-', 'LineWidth', 2);
    


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
        
        camzoom(0.8);

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
    