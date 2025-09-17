
function visual(mode, azimuth, elevation, point_P, point_B, point_C, point_A)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    radius = 1;         
    height = 2;         
    
    
    
    A = [-radius, 0, 0];     
    B = [radius, 0, 0];      
    
    C = [radius, 0, height]; 
    D = [-radius, 0, height]; 
    
    
    P = [radius, 0, height/2]; 
    
    
    target_point = [0, -1, 2]; 


    hold on;
    
    
    theta = linspace(0, 2*pi, 100);
    z_cylinder = linspace(0, height, 50);
    [THETA, Z] = meshgrid(theta, z_cylinder);
    
    
    X = radius * cos(THETA);
    Y = radius * sin(THETA);
    
    
    surf(X, Y, Z, 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'FaceColor', [0.8, 0.8, 0.8]);
    
    
    theta_circle = linspace(0, 2*pi, 100);
    bottom_x = radius * cos(theta_circle);
    bottom_y = radius * sin(theta_circle);
    bottom_z = zeros(size(theta_circle));
    
    
    top_x = radius * cos(theta_circle);
    top_y = radius * sin(theta_circle);
    top_z = height * ones(size(theta_circle));
    
    
    fill3(bottom_x, bottom_y, bottom_z, [0.8, 0.8, 0.8], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    plot3(bottom_x, bottom_y, bottom_z, 'k-', 'LineWidth', 2);
    
    
    plot3(top_x, top_y, top_z, 'k-', 'LineWidth', 2);
    
    
    
    left_bottom = [-radius, 0, 0];
    left_top = [-radius, 0, height];
    right_bottom = [radius, 0, 0];
    right_top = [radius, 0, height];
    
    plot3([left_bottom(1), left_top(1)], [left_bottom(2), left_top(2)], [left_bottom(3), left_top(3)], 'k-', 'LineWidth', 2);
    plot3([right_bottom(1), right_top(1)], [right_bottom(2), right_top(2)], [right_bottom(3), right_top(3)], 'k-', 'LineWidth', 2);
    
   
    
    x_wave = linspace(A(1), target_point(1), 50);
    y_wave = linspace(A(2), target_point(2), 50);
    z_wave = linspace(A(3), target_point(3), 50);
    
    
    wave_amplitude = 0.05;
    for i = 1:length(x_wave)-1
        
        wave_offset = wave_amplitude * sin(i * pi / 5);
        x_start = x_wave(i);
        y_start = y_wave(i) + wave_offset;
        z_start = z_wave(i);
        x_end = x_wave(i+1);
        y_end = y_wave(i+1) + wave_offset;
        z_end = z_wave(i+1);
        
        
        if mod(i, 2) == 0
            plot3([x_start, x_end], [y_start, y_end], [z_start, z_end], 'k:', 'LineWidth', 2);
        end
    end
    
    
    plot3([target_point(1), P(1)], [target_point(2), P(2)], [target_point(3), P(3)], 'k-', 'LineWidth', 2);
    
    
    scatter3(A(1), A(2), A(3), 120, 'ko', 'filled'); 
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(P(1), P(2), P(3), 120, 'ks', 'filled'); 
    scatter3(target_point(1), target_point(2), target_point(3), 100, 'ko', 'filled'); 
    
    
    text(A(1)+0.1, A(2)-0.2, A(3)+0.1, point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2)+0.1, B(3)+0.1, point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2)-0.1, C(3)+0.1, point_C, 'FontSize', 14, 'FontWeight', 'bold');
    
    text(P(1)+0.2, P(2)+0.1, P(3)+0.1, point_P, 'FontSize', 14, 'FontWeight', 'bold');


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
    