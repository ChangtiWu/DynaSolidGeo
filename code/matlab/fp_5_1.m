
function visual(mode, azimuth, elevation, point_A, point_B)
    
    
    
    close all;
    fig = figure('Visible', 'off');



    radius = 2;         
    height = 3;         
    
    
    O1 = [0, 0, 0];       
    O2 = [0, 0, height];  
    
    
    A = [radius, 0, 0];   
    B = [-2, 0, height]; 


    hold on;
    
    
    theta = linspace(0, 2*pi, 100);
    bottom_x = radius * cos(theta);
    bottom_y = radius * sin(theta);
    bottom_z = zeros(size(theta));
    
    
    top_x = radius * cos(theta);
    top_y = radius * sin(theta);
    top_z = height * ones(size(theta));
    
    
    [THETA, Z] = meshgrid(theta, [0, height]);
    X = radius * cos(THETA);
    Y = radius * sin(THETA);
    
    
    surf(X, Y, Z, 'FaceColor', [0.8, 0.9, 1], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    [R, T] = meshgrid(linspace(0, radius, 20), theta);
    X_bottom = R .* cos(T);
    Y_bottom = R .* sin(T);
    Z_bottom = zeros(size(X_bottom));
    surf(X_bottom, Y_bottom, Z_bottom, 'FaceColor', [0.8, 0.9, 1], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    Z_top = height * ones(size(X_bottom));
    surf(X_bottom, Y_bottom, Z_top, 'FaceColor', [0.8, 0.9, 1], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    plot3(bottom_x, bottom_y, bottom_z, 'k-', 'LineWidth', 2);
    
    
    plot3(top_x, top_y, top_z, 'k-', 'LineWidth', 2);
    
    
    
    left_bottom = [-radius, 0, 0];
    left_top = [-radius, 0, height];
    right_bottom = [radius, 0, 0];
    right_top = [radius, 0, height];
    
    plot3([left_bottom(1), left_top(1)], [left_bottom(2), left_top(2)], [left_bottom(3), left_top(3)], 'k-', 'LineWidth', 2);
    plot3([right_bottom(1), right_top(1)], [right_bottom(2), right_top(2)], [right_bottom(3), right_top(3)], 'k-', 'LineWidth', 2);
    
    
    
    
    scatter3(A(1), A(2), A(3), 100, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    
    
    text(A(1)+0.2, A(2)-0.2, A(3)+0.1, point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2)-0.2, B(3)+0.1, point_B, 'FontSize', 14, 'FontWeight', 'bold');


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
    