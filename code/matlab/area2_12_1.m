function visual(mode, azimuth, elevation, point_P, point_O, point_A, point_B)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    R = 2;          
    h = 4;          
    O = [0, 0, 0];  
    O1 = [0, 0, h]; 
    A = [-R, 0, 0]; 
    B = [R, 0, 0];  
    A1 = [-R, 0, h];
    B1 = [R, 0, h]; 
    
    theta_P = pi/6;
    P = [R*cos(theta_P), R*sin(theta_P), 0];
    
    

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
    
    
    
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    
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
    
    
    
    plot3([A1(1), P(1)], [A1(2), P(2)], [A1(3), P(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([A(1), P(1)], [A(2), P(2)], [A(3), P(3)], 'k--', 'LineWidth', 1.5);
    
    theta_base_hid = linspace(pi, 3*pi, 50);
    x_base_hid = R*cos(theta_base_hid);
    y_base_hid = R*sin(theta_base_hid);
    z_base_hid = zeros(size(theta_base_hid));
    plot3(x_base_hid, y_base_hid, z_base_hid, 'k-', 'LineWidth', 1.5);
    
    theta_top_hid = linspace(pi, 3*pi, 50);
    x_top_hid = R*cos(theta_top_hid);
    y_top_hid = R*sin(theta_top_hid);
    z_top_hid = ones(size(theta_top_hid))*h;
    plot3(x_top_hid, y_top_hid, z_top_hid, 'k-', 'LineWidth', 1.5);
    
    plot3([O(1), A(1)], [O(2), A(2)], [O(3), A(3)], 'k--', 'LineWidth', 1.5);
    plot3([O(1), B(1)], [O(2), B(2)], [O(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([O1(1), A1(1)], [O1(2), A1(2)], [O1(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([O1(1), B1(1)], [O1(2), B1(2)], [O1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([O(1), P(1)], [O(2), P(2)], [O(3), P(3)], 'k--', 'LineWidth', 1.5);
    scatter3(O1(1), O1(2), O1(3), 15, 'k', 'filled');
    plot3([A1(1), B(1)], [A1(2), B(2)], [A1(3), B(3)], 'k--', 'LineWidth', 1.5);
    
    text(A(1)-0.1, A(2), A(3), point_A, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(B(1)+0.1, B(2), B(3), point_B, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(O(1), O(2)-0.1, O(3), point_O, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(P(1), P(2)+0.1, P(3), point_P, 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');


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
    