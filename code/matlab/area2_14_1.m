function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    R = 2;          
    h = 4;          
    O = [0, 0, 0];  
    O1 = [0, 0, h]; 
    
    
    circle_center = [0, 0, h/2];  
    circle_radius = R;            
    
    
    sphere_center = [0, 0, h/2];  
    sphere_radius = R;            
    
    

    hold on;

    
    
    
    theta = linspace(0, 2*pi, 100);
    
    
    x_bottom_fill = [0; R * cos(theta')];
    y_bottom_fill = [0; R * sin(theta')];
    z_bottom_fill = zeros(size(x_bottom_fill));
    fill3(x_bottom_fill, y_bottom_fill, z_bottom_fill, [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    x_top_fill = [0; R * cos(theta')];
    y_top_fill = [0; R * sin(theta')];
    z_top_fill = h * ones(size(x_top_fill));
    fill3(x_top_fill, y_top_fill, z_top_fill, [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    [THETA, Z] = meshgrid(theta, [0, h]);
    X = R * cos(THETA);
    Y = R * sin(THETA);
    surf(X, Y, Z, 'FaceColor', [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    [x_sphere, y_sphere, z_sphere] = sphere(50);
    x_sphere = sphere_radius * x_sphere + sphere_center(1);
    y_sphere = sphere_radius * y_sphere + sphere_center(2);
    z_sphere = sphere_radius * z_sphere + sphere_center(3);
    surf(x_sphere, y_sphere, z_sphere, 'FaceColor', [0.9, 0.7, 0.8], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    
    plot3([-R, -R], [0, 0], [0, h], 'k-', 'LineWidth', 2);
    
    plot3([R, R], [0, 0], [0, h], 'k-', 'LineWidth', 2);
    
    
    
    
    
    
    theta_top_vis = linspace(-pi/2, pi/2, 50);
    x_top_vis = R*cos(theta_top_vis);
    y_top_vis = R*sin(theta_top_vis);
    z_top_vis = ones(size(theta_top_vis))*h;
    plot3(x_top_vis, y_top_vis, z_top_vis, 'k-', 'LineWidth', 2);
    
    
    theta_base_vis = linspace(-pi/2, pi/2, 50);
    x_base_vis = R*cos(theta_base_vis);
    y_base_vis = R*sin(theta_base_vis);
    z_base_vis = zeros(size(theta_base_vis));
    plot3(x_base_vis, y_base_vis, z_base_vis, 'k-', 'LineWidth', 2);
    
    
    
    theta_top_hid = linspace(pi, 3*pi, 50);
    x_top_hid = R*cos(theta_top_hid);
    y_top_hid = R*sin(theta_top_hid);
    z_top_hid = ones(size(theta_top_hid))*h;
    plot3(x_top_hid, y_top_hid, z_top_hid, 'k-', 'LineWidth', 1.5);
    
    
    theta_base_hid = linspace(pi, 3*pi, 50);
    x_base_hid = R*cos(theta_base_hid);
    y_base_hid = R*sin(theta_base_hid);
    z_base_hid = zeros(size(theta_base_hid));
    plot3(x_base_hid, y_base_hid, z_base_hid, 'k-', 'LineWidth', 1.5);
    
    
    
    
    
    
    theta_circle = linspace(0, 2*pi, 100);
    x_circle = circle_center(1) + circle_radius*cos(theta_circle);
    z_circle = circle_center(3) + circle_radius*sin(theta_circle);
    y_circle = zeros(size(theta_circle)) + circle_center(2);  
    plot3(x_circle, y_circle, z_circle, 'k--', 'LineWidth', 1.5);





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
    