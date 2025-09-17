function visual(mode, azimuth, elevation, point_A, point_B, point_C)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 2.8;          
    h = 5.5;          
    s = 1.5;          
    
    
    B = [-s, s*sqrt(3)-1.3, 2.6];  
    A = [-s, -1.3, 1.3];           
    C = [-s, -1.3, 3.8];           
    
    
    hold on;
    
    
    [X,Y,Z] = cylinder(r, 50);  
    Z = Z * h;  
    surf(X, Y, Z, 'FaceColor', [0.8 0.8 0.8], 'FaceAlpha', 0.3, 'EdgeAlpha', 0.1);
    
    
    
    theta_front = linspace(-pi/2, pi/2, 50);  
    x_bottom_front = r * cos(theta_front);
    y_bottom_front = r * sin(theta_front);
    z_bottom_front = zeros(size(theta_front));
    plot3(x_bottom_front, y_bottom_front, z_bottom_front, 'k-', 'LineWidth', 2);
    
    theta_back = linspace(pi/2, 3*pi/2, 50);   
    x_bottom_back = r * cos(theta_back);
    y_bottom_back = r * sin(theta_back);
    z_bottom_back = zeros(size(theta_back));
    plot3(x_bottom_back, y_bottom_back, z_bottom_back, 'k--', 'LineWidth', 2);
    
    
    z_top = h * ones(size(theta_front));
    plot3(x_bottom_front, y_bottom_front, z_top, 'k-', 'LineWidth', 2);
    plot3(x_bottom_back, y_bottom_back, z_top, 'k-', 'LineWidth', 2);
    
    
    for i = 0:2:4
        theta_m = 2*pi*(i-1)/4;
        x_m = r * cos(theta_m);
        y_m = r * sin(theta_m);
        plot3([x_m, x_m], [y_m, y_m], [0, h], 'k-', 'LineWidth', 2);
    end
    
    
    
    
    
    
    
    
    theta_inner = linspace(0, 2*pi, 100);  
    
    
    x_A = A(1) + s * sin(theta_inner);
    y_A = A(2) + s * cos(theta_inner);
    z_A = A(3) + s * sin(theta_inner);
    plot3(x_A, y_A, z_A, 'k--', 'LineWidth', 1.5);
    
    
    x_B = B(1) + s * sin(theta_inner);
    y_B = B(2) + s * cos(theta_inner);
    z_B = B(3) + s * sin(theta_inner);
    plot3(x_B, y_B, z_B, 'k--', 'LineWidth', 1.5);
    
    
    x_C = C(1) + s * sin(theta_inner);
    y_C = C(2) + s * cos(theta_inner);
    z_C = C(3) + s * sin(theta_inner);
    plot3(x_C, y_C, z_C, 'k--', 'LineWidth', 1.5);
    
    
    text(A(1), A(2), A(3), point_A, 'FontSize', 12, 'Color', 'black');
    text(B(1), B(2), B(3), point_B, 'FontSize', 12, 'Color', 'black');
    text(C(1), C(2), C(3), point_C, 'FontSize', 12, 'Color', 'black');


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
    