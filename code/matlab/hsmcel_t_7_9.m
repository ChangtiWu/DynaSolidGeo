function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    
    
    a = 6;                  
    h_base = a / sqrt(3);   
    h = sqrt(a^2 - h_base^2); 
    
    
    A = [0, 0, h];                  
    B = [-a/2, -h_base/2, 0];       
    C = [a/2, -h_base/2, 0];        
    D = [0, h_base, 0];             
    
    
    t = 1/a;                     
    E = A + t*(B - A);           
    
    s = 2/a;                     
    F = C + s*(D - C);           
    
    
    
    solid_edges = [
        A; B; ...  
        A; C; ...  
        A; D; ...  
        B; C; ...  
        B; D;
        C; D];     
    
    
    dashed_edges = [
        E; F;
        ];     
    
    
    hold on;
    
    
    
    for i = 1:size(solid_edges, 1)/2
        
        start_pt = solid_edges(2*i - 1, :);  
        end_pt = solid_edges(2*i, :);        
        
        
        x = [start_pt(1), end_pt(1)];
        y = [start_pt(2), end_pt(2)];
        z = [start_pt(3), end_pt(3)];
        
        
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:size(dashed_edges, 1)/2
        start_pt = dashed_edges(2*i - 1, :);
        end_pt = dashed_edges(2*i, :);
        
        x = [start_pt(1), end_pt(1)];
        y = [start_pt(2), end_pt(2)];
        z = [start_pt(3), end_pt(3)];
        
        
        plot3(x, y, z, 'LineWidth', 1.5, 'LineStyle', '--', 'Color', 'k');
    end
    
    
    point_labels = {point_A, point_B, point_C, point_D, point_E, point_F};
    points = [A; B; C; D; E; F];
    for i = 1:6
        px = points(i, 1);
        py = points(i, 2);
        pz = points(i, 3);
        
        
        if strcmp(point_labels{i}, point_A)
            pz = pz + 0.3;  
        elseif strcmp(point_labels{i}, point_B)
            px = px - 0.3;  
        elseif strcmp(point_labels{i}, point_C)
            px = px + 0.3;  
        elseif strcmp(point_labels{i}, point_E)
            py = py - 0.3;  
        elseif strcmp(point_labels{i}, point_F)
            py = py + 0.3;  
        end
        
        text(px, py, pz, point_labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
    end
   



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
    