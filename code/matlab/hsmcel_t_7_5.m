function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_E, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    


    A = [0, 0, 0];        
    P = [0, 0, 2];        
    B = [2, 0, 0];        
    C = [1, 1, 0];        
    
    
    PB = B - P;           
    t = 0.5;              
    E = P + t * PB;       
    
    PC = C - P;           
    s = 2/3;              
    F = P + s * PC;       
    
    
    
    solid_edges = [
        P; A; ...  
        A; B; ...  
        B; C; ...  
        C; P; ...  
        P; B; ...  
        A; C];     
    
    
    dashed_edges = [
        A; F; ...  
        E; F;
        A; E];     
    
    
    hold on;
     
    
    for i = 1:size(solid_edges, 1)/2  
        start_idx = 2*i - 1;          
        end_idx = 2*i;                
        x = [solid_edges(start_idx, 1), solid_edges(end_idx, 1)];
        y = [solid_edges(start_idx, 2), solid_edges(end_idx, 2)];
        z = [solid_edges(start_idx, 3), solid_edges(end_idx, 3)];
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');  
    end
    
    
    for i = 1:size(dashed_edges, 1)/2
        start_idx = 2*i - 1;
        end_idx = 2*i;
        x = [dashed_edges(start_idx, 1), dashed_edges(end_idx, 1)];
        y = [dashed_edges(start_idx, 2), dashed_edges(end_idx, 2)];
        z = [dashed_edges(start_idx, 3), dashed_edges(end_idx, 3)];
        plot3(x, y, z, 'LineWidth', 1.5, 'LineStyle', '--', 'Color', 'k');  
    end
    
    
    point_labels = {point_P, point_A, point_B, point_C, point_E, point_F};
    points = [P; A; B; C; E; F];
    for i = 1:6
        px = points(i, 1); py = points(i, 2); pz = points(i, 3);
        
        if strcmp(point_labels{i}, point_P)
            pz = pz + 0.2;  
        elseif strcmp(point_labels{i}, point_C)
            py = py + 0.2;  px = px + 0.2;  
        elseif strcmp(point_labels{i}, point_E)
            pz = pz + 0.2;  
        elseif strcmp(point_labels{i}, point_F)
            pz = pz + 0.2;  
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
    