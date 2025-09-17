function visual(mode, azimuth, elevation, point_P, point_A)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    r = 1;
    
    
    
    h = sqrt(3);

    
    O = [0, 0, 0];      
    P = [0, 0, h];      
    A = [-r, 0, 0];     
    B = [r, 0, 0];      
    Q = (P + A) / 2;    

    
    theta_AC = pi/3;
    C = [r*cos(pi - theta_AC), r*sin(pi - theta_AC), 0]; 
    C = [r*cosd(120), r*sind(120), 0]; 
    
    
    D = [r*cosd(60), r*sind(60), 0];

    
    M = 0.6 * C;  

    
    
    n = 50; 
    [theta, z_cone] = meshgrid(linspace(0, 2*pi, n), linspace(0, h, n));
    x_cone = (r/h) * (h - z_cone) .* cos(theta); 
    y_cone = (r/h) * (h - z_cone) .* sin(theta);
    


    hold on;

    
    surf(x_cone, y_cone, z_cone, 'FaceColor', 'blue', 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    

    
    t = linspace(0, 2*pi, 50);
    x = r * cos(t);
    y = r * sin(t);
    z = zeros(size(t));
    plot3(x, y, z, 'b-', 'LineWidth', 2); 

    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k--', 'LineWidth', 1);
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k--', 'LineWidth', 1);

    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);

    
    plot3([O(1), C(1)], [O(2), C(2)], [O(3), C(3)], 'k--', 'LineWidth', 1);
    plot3([Q(1), M(1)], [Q(2), M(2)], [Q(3), M(3)], 'r-', 'LineWidth', 2);

    
    points = {A, C, D, P, Q, O, M};
    
    for i = 1:length(points)
        pt = points{i};
        scatter3(pt(1), pt(2), pt(3), 100, 'ko', 'filled');  
    end
    text(A(1)+0.05, A(2)+0.05, A(3)+0.05, point_A, 'FontSize', 12, 'FontWeight', 'bold');
    text(P(1)+0.05, P(2)+0.05, P(3)+0.05, point_P, 'FontSize', 12, 'FontWeight', 'bold');

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
    