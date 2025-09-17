function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    x = 1;
    r_top = 2 * x;       
    r_bottom = 3 * x;    
    height = sqrt(5) * x;
    
    
    O1 = [0, 0, height]; 
    B = [r_top, 0, height];
    O = [0, 0, 0];       
    A = [r_bottom, 0, 0];
    C = [r_top, 0, 0];   
    E=2*O-A;
    F=2*O1-B;
    
    

    hold on;

    
    
    
    theta = linspace(0, 2*pi, 100);
    
    
    x_top_fill = [0; r_top * cos(theta')];
    y_top_fill = [0; r_top * sin(theta')];
    z_top_fill = height * ones(size(x_top_fill));
    fill3(x_top_fill, y_top_fill, z_top_fill, [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    x_bottom_fill = [0; r_bottom * cos(theta')];
    y_bottom_fill = [0; r_bottom * sin(theta')];
    z_bottom_fill = zeros(size(x_bottom_fill));
    fill3(x_bottom_fill, y_bottom_fill, z_bottom_fill, [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    [THETA, Z] = meshgrid(theta, [0, height]);
    R = r_bottom - (r_bottom - r_top) * Z / height;
    X = R .* cos(THETA);
    Y = R .* sin(THETA);
    surf(X, Y, Z, 'FaceColor', [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    
    theta_top = linspace(-pi, pi, 50);
    x_top = r_top * cos(theta_top) + O1(1);
    y_top = r_top * sin(theta_top) + O1(2);
    z_top = ones(size(theta_top)) * height;
    plot3(x_top, y_top, z_top, 'k-', 'LineWidth', 2);
    
    
    theta_bottom = linspace(-pi, pi, 50);
    x_bottom = r_bottom * cos(theta_bottom) + O(1);
    y_bottom = r_bottom * sin(theta_bottom) + O(2);
    z_bottom = zeros(size(theta_bottom));
    plot3(x_bottom, y_bottom, z_bottom, 'k-', 'LineWidth', 2);
    
    
    plot3([B(1), A(1)], [B(2), A(2)], [B(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);
    
    plot3([O1(1), B(1)], [O1(2), B(2)], [O1(3), B(3)], 'k-', 'LineWidth', 2);
    
    
    
    plot3([O1(1), O(1)], [O1(2), O(2)], [O1(3), O(3)], 'k--', 'LineWidth', 1.5);
    
    
    
    plot3([O(1), A(1)], [O(2), A(2)], [O(3), A(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([C(1), B(1)], [C(2), B(2)], [C(3), B(3)], 'k--', 'LineWidth', 1.5);
    
    


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
    