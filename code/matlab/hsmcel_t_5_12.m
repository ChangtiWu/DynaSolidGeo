function visual(mode, azimuth, elevation, point_V, point_A, point_B, point_C, point_E, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    side_len = 2*sqrt(3);  
    angle = 40;            
    
    
    cos20 = cosd(20);
    sin20 = sind(20);
    V = [0, 0, side_len * cos20];       
    a = side_len * sin20;               
    A = [-a, 0, 0];                     
    B = [a, 0, 0];                      
    C = [0, a*sqrt(3), 0];              
    
    
    E = (V + B)/2;                      
    F = (V + C)/2;                      
    
    
    solid_edges = [
        V; A; ...  
        V; E; ...  
        E; B; ...  
        V; F; ...  
        F; C; ...  
        A; B; ...  
        B; C; ...  
        A; C; ...  
        ];    
    
    dashed_edges = [
        A; E; ...  
        E; F; ...
        A; F];     
    
    
    hold on;
    
    set(gca, 'FontSize', 10);
    
    
    for i = 1:size(solid_edges, 1)/2
        start = solid_edges(2*i-1, :);
        end_p = solid_edges(2*i, :);
        plot3([start(1), end_p(1)], [start(2), end_p(2)], [start(3), end_p(3)], ...
            'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:size(dashed_edges, 1)/2
        start = dashed_edges(2*i-1, :);
        end_p = dashed_edges(2*i, :);
        plot3([start(1), end_p(1)], [start(2), end_p(2)], [start(3), end_p(3)], ...
            'LineWidth', 1.5, 'LineStyle', '--', 'Color', 'k');
    end
    
    
    point_labels = {point_V,point_A,point_B,point_C,point_E,point_F};
    points = [V; A; B; C; E; F];
    for i = 1:size(points, 1)
        dx = 0.1; dy = 0.1; dz = 0.1;
        if strcmp(point_labels{i}, point_V)
            dz = 0.3;  
        elseif strcmp(point_labels{i}, point_A)
            dx = -0.3; 
        elseif strcmp(point_labels{i}, point_C)
            dy = 0.3;  
        end
        text(points(i,1)+dx, points(i,2)+dy, points(i,3)+dz, point_labels{i}, ...
            'HorizontalAlignment', 'left', 'FontWeight', 'bold');
    end
    
    
    xlim([-2, 2]);
    ylim([-1, 3]);
    zlim([-1, 5]);



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

        camzoom(0.8);

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
    