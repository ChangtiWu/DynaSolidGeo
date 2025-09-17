function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    

    hold on;         
    
    
    R_bottom = 6;    
    R_mid = 8;      
    R_top = 4;       
    H_total = 14;    
    h_bottom = 8;    
    h_top = 6;       
    
    
    O_bottom = [0, 0, 0];   
    O_mid = [0, 0, h_bottom]; 
    O_top = [0, 0, H_total]; 
    
    
    theta = linspace(0, 2*pi, 100);  
    
    
    
    
    x_bottom = R_bottom * cos(theta);
    y_bottom = R_bottom * sin(theta);
    z_bottom = zeros(size(theta));
    plot3(x_bottom, y_bottom, z_bottom, 'k', 'LineWidth', 1.5);
    
    
    x_mid = R_mid * cos(theta);
    y_mid = R_mid * sin(theta);
    z_mid = ones(size(theta)) * h_bottom;
    plot3(x_mid, y_mid, z_mid, 'k', 'LineWidth', 1.5);
    
    
    x_top = R_top * cos(theta);
    y_top = R_top * sin(theta);
    z_top = ones(size(theta)) * H_total;
    plot3(x_top, y_top, z_top, 'k', 'LineWidth', 1.5);
    
    
    plot3([0, 0], [0, 0], [0, H_total], 'k--', 'LineWidth', 1.5);
    
    
    
    
    theta_outline = [0,  pi];  
    
    
    for i = 1:length(theta_outline)
        x_b = R_bottom * cos(theta_outline(i));
        y_b = R_bottom * sin(theta_outline(i));
        x_m = R_mid * cos(theta_outline(i));
        y_m = R_mid * sin(theta_outline(i));
        plot3([x_b, x_m], [y_b, y_m], [0, h_bottom], 'k', 'LineWidth', 2);
    end
    
    
    for i = 1:length(theta_outline)
        x_m = R_mid * cos(theta_outline(i));
        y_m = R_mid * sin(theta_outline(i));
        x_t = R_top * cos(theta_outline(i));
        y_t = R_top * sin(theta_outline(i));
        plot3([x_m, x_t], [y_m, y_t], [h_bottom, H_total], 'k', 'LineWidth', 2);
    end

    
    
    [theta_grid, r_grid] = meshgrid(theta, linspace(R_bottom, R_mid, 20));
    X_lower = r_grid .* cos(theta_grid);
    Y_lower = r_grid .* sin(theta_grid);
    Z_lower = (h_bottom/(R_mid-R_bottom)) * (r_grid - R_bottom);
    surf(X_lower, Y_lower, Z_lower, 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'FaceColor', 'blue');

    
    [theta_grid, r_grid] = meshgrid(theta, linspace(R_mid, R_top, 20));
    X_upper = r_grid .* cos(theta_grid);
    Y_upper = r_grid .* sin(theta_grid);
    Z_upper = h_bottom + (h_top/(R_mid-R_top)) * (R_mid - r_grid);
    surf(X_upper, Y_upper, Z_upper, 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'FaceColor', 'red');

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
    