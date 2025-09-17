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
    E = (A + B)/2;        
    F = (A + A1)/2;       
    
    
    
    solid_edges = [
        
        A; B; ...          
        B; C; ...          
        C; C1;
        D; C; ...          
        D; A; ...          
        D; D1;
        B; B1;
        A; A1;
        A1; B1;
        B1; C1;
        A1; D1;
        C1; D1;
        ];             
    
    
    dashed_edges = [
        B1; D1;
        E; C; ...          
        B1; F;
        B1; C;
        B1; E;
        F; D1];            
    
    
    hold on;
    
    
    
    for i = 1:size(solid_edges, 1)/2  
        row_start = 2*i - 1;          
        row_end = 2*i;                
        x = [solid_edges(row_start, 1), solid_edges(row_end, 1)];
        y = [solid_edges(row_start, 2), solid_edges(row_end, 2)];
        z = [solid_edges(row_start, 3), solid_edges(row_end, 3)];
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');  
    end
    
    
    for i = 1:size(dashed_edges, 1)/2
        row_start = 2*i - 1;
        row_end = 2*i;
        x = [dashed_edges(row_start, 1), dashed_edges(row_end, 1)];
        y = [dashed_edges(row_start, 2), dashed_edges(row_end, 2)];
        z = [dashed_edges(row_start, 3), dashed_edges(row_end, 3)];
        plot3(x, y, z, 'LineWidth', 1.5, 'LineStyle', '--', 'Color', 'k');  
    end
    
    
    point_labels = {point_A,point_B,point_C,point_D,point_A1,point_B1,point_C1,point_D1,point_E,point_F};
    points = [A; B; C; D; A1; B1; C1; D1; E; F];
    for i = 1:10
        px = points(i, 1); py = points(i, 2); pz = points(i, 3);
        
        if strcmp(point_labels{i}, point_E)
            py = py - 0.2;  
        elseif strcmp(point_labels{i}, point_F)
            pz = pz + 0.2;  
        elseif strcmp(point_labels{i}, point_D)
            py = py + 0.2;  
        end
        text(px, py, pz, point_labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
    end
    
    
    xlim([-1, 3]);
    ylim([-1, 3]);
    zlim([-1, 3]);
    



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
    