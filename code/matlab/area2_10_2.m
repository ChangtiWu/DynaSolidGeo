function visual(mode, azimuth, elevation, point_S, point_O)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    r = 2;          
    h = 3;          
    O = [0, 0, 0];  
    S = [0, 0, h];  
    A = [r, 0, 0];  
    B = [-r, 0, 0]; 
    D = [0, r, 0];  
    C = -D; 
    
    
    t = 0.4;
    P = S + t*(B - S);  
    
    

    hold on;

    
    
    
    theta = linspace(0, 2*pi, 100);
    
    
    x_bottom_fill = [0; r * cos(theta')];
    y_bottom_fill = [0; r * sin(theta')];
    z_bottom_fill = zeros(size(x_bottom_fill));
    fill3(x_bottom_fill, y_bottom_fill, z_bottom_fill, [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    [THETA, Z] = meshgrid(theta, linspace(0, h, 50));
    R = r * (h - Z) / h;  
    X = R .* cos(THETA);
    Y = R .* sin(THETA);
    surf(X, Y, Z, 'FaceColor', [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    
    theta_vis = linspace(0, pi, 50);
    x_vis = r * cos(theta_vis);
    y_vis = r * sin(theta_vis);
    z_vis = zeros(size(theta_vis));
    plot3(x_vis, y_vis, z_vis, 'k-', 'LineWidth', 2);
    
    
    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2);
    
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    
    plot3([O(1), D(1)], [O(2), D(2)], [O(3), D(3)], 'k--', 'LineWidth', 1.5);
    
    
    
    plot3([S(1), O(1)], [S(2), O(2)], [S(3), O(3)], 'k--', 'LineWidth', 1.5);
    
    theta_hid = linspace(pi/2, 2*pi, 100);
    x_hid = r * cos(theta_hid);
    y_hid = r * sin(theta_hid);
    z_hid = zeros(size(theta_hid));
    plot3(x_hid, y_hid, z_hid, 'k--', 'LineWidth', 1.5);
    
    plot3([C(1), P(1)], [C(2), P(2)], [C(3), P(3)], 'k--', 'LineWidth', 1.5);
    plot3([D(1), P(1)], [D(2), P(2)], [D(3), P(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([O(1), P(1)], [O(2), P(2)], [O(3), P(3)], 'k--', 'LineWidth', 1.5);
    
    
    text(S(1), S(2), S(3) + 0.1, point_S, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(O(1), O(2), O(3) - 0.1, point_O, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    
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
    