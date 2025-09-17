function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 2;         
    h = 3 * r / 2; 
    theta_A = -pi/6;   
    theta_B = pi/2;
    theta_C = -pi/2;  
    
    
    O = [0, 0, 0];     
    A = [r*cos(theta_A), r*sin(theta_A), 0]; 
    B = [r*cos(theta_B), r*sin(theta_B), 0]; 
    C = [r*cos(theta_C), r*sin(theta_C), 0]; 
    P = [0, 0, h];     
    M = (P + A) / 2;   
    N = (P + B) / 2;   
    Q = (P + C) / 2;   
    
    
    hold on;

    
    
    theta = linspace(0, 2*pi, 50);
    z = linspace(0, h, 20);
    [THETA, Z] = meshgrid(theta, z);
    R_z = r * (1 - Z/h);  
    X = R_z .* cos(THETA);
    Y = R_z .* sin(THETA);
    surf(X, Y, Z, 'FaceColor', [0.8 0.8 0.8], 'FaceAlpha', 0.3, 'EdgeColor', 'none');

    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2); 
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2); 
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2); 
    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k--', 'LineWidth', 2); 
    
    
    
    
    theta_vis = linspace(theta_A, theta_B, 50);
    x_vis = r * cos(theta_vis);
    y_vis = r * sin(theta_vis);
    z_vis = zeros(size(theta_vis));
    plot3(x_vis, y_vis, z_vis, 'k--', 'LineWidth', 1.5);
    
    
    theta_hid1 = linspace(theta_B, theta_C, 50);
    theta_hid2 = linspace(theta_C, theta_A + 2*pi, 50);
    x_hid1 = r * cos(theta_hid1);
    y_hid1 = r * sin(theta_hid1);
    z_hid1 = zeros(size(theta_hid1));
    x_hid2 = r * cos(theta_hid2);
    y_hid2 = r * sin(theta_hid2);
    z_hid2 = zeros(size(theta_hid2));
    plot3(x_hid1, y_hid1, z_hid1, 'k--', 'LineWidth', 1.5);
    plot3(x_hid2, y_hid2, z_hid2, 'k-', 'LineWidth', 1.5);
    
    
    plot3([M(1), A(1)], [M(2), A(2)], [M(3), 0], 'k--', 'LineWidth', 1.5);
    plot3([N(1), B(1)], [N(2), B(2)], [N(3), 0], 'k--', 'LineWidth', 1.5);
    
    
    


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
    