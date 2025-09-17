function visual(mode, azimuth, elevation, point_P, point_O, point_A, point_B, point_H, point_C)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 2;                
    PA_length = 4;        
    h = sqrt(PA_length^2 - r^2); 
    
    
    P = [0, 0, h];        
    O = [0, 0, 0];        
    A = [r, 0, 0];        
    D = [-r, 0, 0];       
    B = [1, 1, 0];        
    C = (P + A) / 2;      
    
    
    PB = B - P;           
    t = -dot(P, PB) / dot(PB, PB); 
    H = P + t * PB;       
    
    
    hold on;
    
    
    
    theta = linspace(0, 2*pi, 50);
    x_cone = [];
    y_cone = [];
    z_cone = [];
    
    for i = 1:length(theta)
        
        x_bottom = r * cos(theta(i));
        y_bottom = r * sin(theta(i));
        z_bottom = 0;
        
        
        x_line = [P(1), x_bottom];
        y_line = [P(2), y_bottom];
        z_line = [P(3), z_bottom];
    
        x_cone = [x_cone; x_line];
        y_cone = [y_cone; y_line];
        z_cone = [z_cone; z_line];
    end
    
    
    theta_surf = linspace(0, 2*pi, 30);
    r_surf = linspace(0, r, 20);
    [THETA, R] = meshgrid(theta_surf, r_surf);
    X_surf = R .* cos(THETA);
    Y_surf = R .* sin(THETA);
    Z_surf = h * (1 - R/r);  
    
    surf(X_surf, Y_surf, Z_surf, 'FaceColor', [0.8, 0.9, 1], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    theta_bottom = linspace(0, 2*pi, 50);
    x_bottom_fill = r * cos(theta_bottom);
    y_bottom_fill = r * sin(theta_bottom);
    z_bottom_fill = zeros(size(x_bottom_fill));
    
    fill3(x_bottom_fill, y_bottom_fill, z_bottom_fill, [0.8, 0.9, 1], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    
    solid_edges = {
        [P; A]; 
        [P; D]; 
        [A; B]; 
        [P; C]  
    };
    
    
    dashed_edges = {
        [P; O]; 
        [O; B]; 
        [P; B]; 
        [O; H];
        [H; C]; 
        [O; A]; 
        [O; D]  
    };
    
    
    theta = linspace(0, 2*pi, 100); 
    x_circle = r * cos(theta);      
    y_circle = r * sin(theta);      
    z_circle = zeros(size(x_circle)); 
    
    
    hold on;
    
    
    plot3(x_circle, y_circle, z_circle, '--', 'LineWidth', 1.5, 'Color', 'k');
    
    
    for i = 1:length(solid_edges)
        edge = solid_edges{i};
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(dashed_edges)
        edge = dashed_edges{i};
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    text(P(1), P(2), P(3)+0.5, point_P, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(O(1), O(2), O(3)-0.5, point_O, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(A(1)+0.5, A(2), A(3)-0.5, point_A, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    
    text(B(1)-0.5, B(2)+0.5, B(3)-0.5, point_B, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(C(1), C(2), C(3)+0.5, point_C, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(H(1)-0.5, H(2)-0.5, H(3), point_H, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    


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
    