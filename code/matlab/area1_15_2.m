function visual(mode, azimuth, elevation, point_O, point_P, point_A, point_B, point_C)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 2;          
    h = r;          
    P = [0, 0, h];  
    A = [r, 0, 0];  
    B = [-r, 0, 0]; 
    O = [0, 0, 0];  
    
    
    theta_C = pi/2; 
    C = [r*cos(theta_C), r*sin(theta_C), 0]; 
    
    
    theta_D = (pi + theta_C) / 2; 
    D = [r*cos(theta_D), r*sin(theta_D), 0]; 
    
    

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
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2); 
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 2); 
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k--', 'LineWidth', 2); 
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k--', 'LineWidth', 2); 
    
    
    theta_vis = linspace(0, pi, 100);
    x_vis = r * cos(theta_vis);
    y_vis = r * sin(theta_vis);
    z_vis = zeros(size(theta_vis));
    plot3(x_vis, y_vis, z_vis, 'k--', 'LineWidth', 1.5);
    
    
    theta_hid = linspace(pi, 2*pi, 100);
    x_hid = r * cos(theta_hid);
    y_hid = r * sin(theta_hid);
    z_hid = zeros(size(theta_hid));
    plot3(x_hid, y_hid, z_hid, 'k--', 'LineWidth', 1.5);
    
    
    plot3([P(1), O(1)], [P(2), O(2)], [P(3), O(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([O(1), D(1)], [O(2), D(2)], [O(3), D(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 1.5);
    
    
    text(P(1)+0.05, P(2)+0.05, P(3)+0.2, point_P, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(A(1)+0.05, A(2)+0.05, A(3)+0.2, point_A, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(B(1)+0.05, B(2)+0.05, B(3)+0.2, point_B, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(O(1)+0.05, O(2)+0.05, O(3)+0.2, point_O, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(C(1)+0.05, C(2)+0.05, C(3)+0.2, point_C, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    

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
    