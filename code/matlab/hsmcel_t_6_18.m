function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_M, point_N)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];        
    B = [0, 2, 0];        
    C = [2, 2, 0];        
    D = [2, 0, 0];        
    P = [0, 0, 2];        
    
    
    M = (P + D) / 2;      
    PC = C - P;           
    
    s = 1/3;             
    N = P + s*(C - P);    
    
    
    
    solid_edges = [
        B; C; ...  
        C; D; ...  
        P; B; ...  
        P; C; ...  
        P; D; ...  
        A; P;
        A; D; ...  
        A; B];     
    
    
    dashed_edges = [
        A; N;
        M; N;
        A; M];     
    
    
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
    
    
    point_labels = {point_P, point_A, point_B, point_C, point_D, point_M, point_N};
    points = [P; A; B; C; D; M; N];
    for i = 1:7
        px = points(i, 1); py = points(i, 2); pz = points(i, 3);
        
        if strcmp(point_labels{i}, point_P)
            pz = pz + 0.2;  
        elseif strcmp(point_labels{i}, point_D)
            px = px + 0.2;  
        elseif strcmp(point_labels{i}, point_N)
            py = py + 0.2;  
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
    