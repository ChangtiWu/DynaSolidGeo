function visual(mode, azimuth, elevation, point_A, point_B, point_P)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 2;          
    h_cyl = 4;      
    h_cone = 3;     
    
    
    O1 = [0, 0, 0];       
    O2 = [0, 0, h_cyl];   
    P = [0, 0, h_cyl + h_cone];  
    
    
    theta_visible = linspace(-pi/2, pi/2, 50);  
    theta_hidden = linspace(pi/2, 3*pi/2, 50);   
    
    
    hold on;
    
    
    
    theta = linspace(0, 2*pi, 50);
    z_cyl = linspace(0, h_cyl, 20);
    [THETA, Z_CYL] = meshgrid(theta, z_cyl);
    X_CYL = r * cos(THETA);
    Y_CYL = r * sin(THETA);
    surf(X_CYL, Y_CYL, Z_CYL, 'FaceColor', [0.8 0.8 0.8], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    z_cone = linspace(h_cyl, h_cyl + h_cone, 20);
    [THETA, Z_CONE] = meshgrid(theta, z_cone);
    R_z = r * (1 - (Z_CONE - h_cyl)/h_cone);  
    X_CONE = R_z .* cos(THETA);
    Y_CONE = R_z .* sin(THETA);
    surf(X_CONE, Y_CONE, Z_CONE, 'FaceColor', [0.8 0.8 0.8], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    
    x_bot_vis = r * cos(theta_visible);
    y_bot_vis = r * sin(theta_visible);
    z_bot_vis = zeros(size(theta_visible));
    plot3(x_bot_vis, y_bot_vis, z_bot_vis, 'k-', 'LineWidth', 2);
    
    
    x_top_vis = r * cos(theta_visible);
    y_top_vis = r * sin(theta_visible);
    z_top_vis = h_cyl * ones(size(theta_visible));
    plot3(x_top_vis, y_top_vis, z_top_vis, 'k-', 'LineWidth', 2);
    
    
    for i = 0:2:4
        theta_m = 2*pi*(i-1)/4;
        x_m = r * cos(theta_m);
        y_m = r * sin(theta_m);
        plot3([x_m, x_m], [y_m, y_m], [0, h_cyl], 'k-', 'LineWidth', 2);
    end
    
    
    x_cone = r * cos(theta_visible);
    y_cone = r * sin(theta_visible);
    z_cone = h_cyl * ones(size(theta_visible));
    
    plot3([P(1), x_cone(length(theta_visible))], [P(2), y_cone(length(theta_visible))] ...
            , [P(3), z_cone(length(theta_visible))], 'k-', 'LineWidth', 2);
    
    plot3([P(1), x_cone(1)], [P(2), y_cone(1)] ...
            , [P(3), z_cone(1)], 'k-', 'LineWidth', 2);
    
    
    x_bot_hid = r * cos(theta_hidden);
    y_bot_hid = r * sin(theta_hidden);
    z_bot_hid = zeros(size(theta_hidden));
    plot3(x_bot_hid, y_bot_hid, z_bot_hid, 'k--', 'LineWidth', 1.5);
    
    
    x_top_hid = r * cos(theta_hidden);
    y_top_hid = r * sin(theta_hidden);
    z_top_hid = h_cyl * ones(size(theta_hidden));
    plot3(x_top_hid, y_top_hid, z_top_hid, 'k--', 'LineWidth', 1.5);
    
    
    plot3(x_top_hid, y_top_hid, z_top_hid, 'k--', 'LineWidth', 1.5);
    
    
    plot3([P(1), O1(1)], [P(2), O1(2)], [P(3), O1(3)], 'k--', 'LineWidth', 1.5);
    
    
    text(O1(1), O1(2), O1(3), point_B, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(O2(1), O2(2), O2(3), point_A, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(P(1), P(2), P(3), point_P, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');


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
    