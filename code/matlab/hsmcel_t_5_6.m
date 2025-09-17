function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];       
    B = [2, 0, 0];       
    C = [2, 2, 0];       
    D = [0, 2, 0];       
    A1 = [0, 0, 2];      
    B1 = [2, 0, 2];      
    C1 = [2, 2, 2];      
    D1 = [0, 2, 2];      
    E = [2, 1, 1];       
    F = [1, 1, 0];       
    
    
    
    solid_edges = [
        A1; B1; ...  
        B1; C1; ...  
        C1; C; ...   
        C; B; ...    
        B; A; ...    
        A; A1; ...   
        A1; D1; ...  
        D1; C1; ...  
        D; D1; ...   
        D; A; ...    
        B; B1; ...   
        C; D];       
    
    
    dashed_edges = [
        F; C; ...    
        F; E; ...    
        A; C; ...    
        B; C1; ...   
        B; D; ...
        B1; C; ...  
        A1; C1; ...  
        B; E];      
    
    
    hold on;
    
    
    
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
    
    
    point_labels = {point_A,point_B,point_C,point_D,point_A1,point_B1,point_C1,point_D1,point_E,point_F};
    points = [A; B; C; D; A1; B1; C1; D1; E; F];
    for i = 1:size(points, 1)
        
        dx = 0.1; dy = 0.1; dz = 0.1;
        if strcmp(point_labels{i}, point_F)
            dy = -0.2;  
        elseif strcmp(point_labels{i}, point_E)
            dx = -0.2;  
        end
        text(points(i,1)+dx, points(i,2)+dy, points(i,3)+dz, point_labels{i}, ...
            'FontSize', 10, 'HorizontalAlignment', 'left', 'FontWeight', 'bold');
    end
    
    
    xlim([-0.5, 2.5]);
    ylim([-0.5, 2.5]);
    zlim([-0.5, 2.5]);



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
    