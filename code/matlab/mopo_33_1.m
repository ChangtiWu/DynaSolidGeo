function visual(mode, azimuth, elevation, point_P, point_E, point_F, point_B, point_C, point_A)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 1; 
    h = 5; 
    sphere_r = r; 
    
    
    theta = linspace(0, 2*pi, 50);
    z = linspace(-h/2, h/2, 50);
    [theta_grid, z_grid] = meshgrid(theta, z);
    x_cylinder = r * cos(theta_grid);
    y_cylinder = r * sin(theta_grid);
    
    
    surf(x_cylinder, y_cylinder, z_grid, 'EdgeColor', 'none', 'FaceColor', [0.3 0.6 0.9], 'FaceAlpha', 0.5);
    hold on;
    
    
    [x_sphere1, y_sphere1, z_sphere1] = sphere(30);
    x_sphere1 = sphere_r * x_sphere1;
    y_sphere1 = sphere_r * y_sphere1;
    z_sphere1 = sphere_r * z_sphere1 + h/2 - sphere_r; 
    surf(x_sphere1, y_sphere1, z_sphere1, 'EdgeColor', 'none', 'FaceColor', [0.9 0.4 0.4], 'FaceAlpha', 0.5);
    
    [x_sphere2, y_sphere2, z_sphere2] = sphere(30);
    x_sphere2 = sphere_r * x_sphere2;
    y_sphere2 = sphere_r * y_sphere2;
    z_sphere2 = sphere_r * z_sphere2 - h/2 + sphere_r; 
    surf(x_sphere2, y_sphere2, z_sphere2, 'EdgeColor', 'none', 'FaceColor', [0.9 0.4 0.4], 'FaceAlpha', 0.5);
    
    
    
    
    axis equal;
    grid on;
    
    [x_plane, y_plane] = meshgrid(linspace(-2, 2, 200));
    z_plane = zeros(size(x_plane)); 
    surf(x_plane, y_plane, z_plane, 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'FaceColor', [0.7, 0.7, 0.7]);



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
    