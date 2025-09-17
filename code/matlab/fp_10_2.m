
function visual(mode, azimuth, elevation, point_M, point_A)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    top_radius = 5;      
    bottom_radius = 10;  
    slant_height = 20;   
    
    
    height = sqrt(slant_height^2 - (bottom_radius - top_radius)^2);
    
    
    
    A = [bottom_radius, 0, 0];  
    
    B = [top_radius, 0, height]; 
    
    
    M = (A + B) / 2;
    
    
    opposite_bottom = [-bottom_radius, 0, 0];
    opposite_top = [-top_radius, 0, height];
    
    
    
    
    
    
    h_total = height * bottom_radius / (bottom_radius - top_radius);
    O = [0, 0, h_total]; 


    hold on;
    
    
    theta = linspace(0, 2*pi, 100);
    bottom_x = bottom_radius * cos(theta);
    bottom_y = bottom_radius * sin(theta);
    bottom_z = zeros(size(theta));
    
    
    top_x = top_radius * cos(theta);
    top_y = top_radius * sin(theta);
    top_z = height * ones(size(theta));
    
    
    n_segments = 50;
    theta_surf = linspace(0, 2*pi, n_segments);
    
    
    for i = 1:n_segments-1
        
        x_bot = [bottom_radius * cos(theta_surf(i)), bottom_radius * cos(theta_surf(i+1))];
        y_bot = [bottom_radius * sin(theta_surf(i)), bottom_radius * sin(theta_surf(i+1))];
        z_bot = [0, 0];
        
        
        x_top = [top_radius * cos(theta_surf(i)), top_radius * cos(theta_surf(i+1))];
        y_top = [top_radius * sin(theta_surf(i)), top_radius * sin(theta_surf(i+1))];
        z_top = [height, height];
        
        
        X = [x_bot(1), x_bot(2), x_top(2), x_top(1), x_bot(1)];
        Y = [y_bot(1), y_bot(2), y_top(2), y_top(1), y_bot(1)];
        Z = [z_bot(1), z_bot(2), z_top(2), z_top(1), z_bot(1)];
        
        patch(X, Y, Z, [0.8, 0.8, 0.9], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    end
    
    
    patch(bottom_x, bottom_y, bottom_z, [0.8, 0.8, 0.9], 'FaceAlpha', 0.2, 'EdgeColor', 'none');
    
    
    patch(top_x, top_y, top_z, [0.8, 0.8, 0.9], 'FaceAlpha', 0.2, 'EdgeColor', 'none');
    
    
    plot3(bottom_x, bottom_y, bottom_z, 'k-', 'LineWidth', 2);
    
    
    plot3(top_x, top_y, top_z, 'k-', 'LineWidth', 2);
    
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([opposite_bottom(1), opposite_top(1)], [opposite_bottom(2), opposite_top(2)], [opposite_bottom(3), opposite_top(3)], 'k--', 'LineWidth', 2);
    
    
    plot3([B(1), O(1)], [B(2), O(2)], [B(3), O(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([opposite_top(1), O(1)], [opposite_top(2), O(2)], [opposite_top(3), O(3)], 'k--', 'LineWidth', 1.5);
    
    
    left_bottom = [0, -bottom_radius, 0];
    left_top = [0, -top_radius, height];
    right_bottom = [0, bottom_radius, 0];
    right_top = [0, top_radius, height];
    
    
    rope_points = [];
    num_segments = 30;
    
    
    
    if ~isempty(rope_points)
        plot3([rope_points(end,1), M(1)], [rope_points(end,2), M(2)], [rope_points(end,3), M(3)], 'k:', 'LineWidth', 2);
    end
    
    
    text(A(1)+0.5, A(2)-0.5, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');

    text(M(1)+0.5, M(2)+0.5, M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    
    
    
    text(bottom_radius+1, 0, -1, '', 'FontSize', 12, 'FontWeight', 'bold');
    text(top_radius+1, 0, height+1, '', 'FontSize', 12, 'FontWeight', 'bold');
    text(A(1)+1, A(2), (A(3)+B(3))/2, '', 'FontSize', 12, 'FontWeight', 'bold');
    
    
    plot3(A(1), A(2), A(3), 'ko', 'MarkerSize', 8, 'MarkerFaceColor', 'black');
    plot3(B(1), B(2), B(3), 'ko', 'MarkerSize', 8, 'MarkerFaceColor', 'black');
    plot3(M(1), M(2), M(3), 'ko', 'MarkerSize', 8, 'MarkerFaceColor', 'black');
    plot3(O(1), O(2), O(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');


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

        camzoom(0.6);

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