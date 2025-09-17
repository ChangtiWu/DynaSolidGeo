
function visual(mode, azimuth, elevation, point_S)
    
    
    
    close all;
    fig = figure('Visible', 'off');



    radius = 1;        
    height = 4;         
    
    
    S = [0, 0, 0];      
    A = [height, 0, -1];    
    B = [height, 0, radius];    
    

    center = [height, 0, 0];


    hold on;
    

    theta = linspace(0, 2*pi, 100);
    circle_x = height * ones(size(theta));  
    circle_y = radius * cos(theta);
    circle_z = radius * sin(theta);
    

    front_idx = (theta >= -pi/2) & (theta <= pi/2);
    plot3(circle_x(front_idx), circle_y(front_idx), circle_z(front_idx), 'k-', 'LineWidth', 2);
    

    back_idx = (theta < -pi/2) | (theta > pi/2);
    plot3(circle_x(back_idx), circle_y(back_idx), circle_z(back_idx), 'k-', 'LineWidth', 2);
    

    [R, H] = meshgrid(linspace(0, radius, 50), linspace(0, height, 50));
    PHI = linspace(0, 2*pi, 50);
    X = H;
    Y = R .* cos(PHI);
    Z = R .* sin(PHI);
    

    key_angles = [0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4];
    for i = 1:length(key_angles)
        angle = key_angles(i);
        end_point = [height, radius*cos(angle), radius*sin(angle)];
        plot3([S(1), end_point(1)], [S(2), end_point(2)], [S(3), end_point(3)], 'k-', 'LineWidth', 1);
    end
    

    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([height, height], [0, 0], [-radius, radius], 'k-', 'LineWidth', 1);
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    

    ground_x = [-1, height+1, height+1, -1, -1];
    ground_y = [-radius-1, -radius-1, radius+1, radius+1, -radius-1];
    ground_z = [0, 0, 0, 0, 0];
    plot3(ground_x, ground_y, ground_z, 'k:', 'LineWidth', 1);
    

    scatter3(S(1), S(2), S(3), 100, 'ko', 'filled');
    scatter3(A(1), A(2), A(3), 100, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    

    text(S(1)-0.2, S(2)-0.2, S(3)+0.1, point_S, 'FontSize', 14, 'FontWeight', 'bold');
    


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
    