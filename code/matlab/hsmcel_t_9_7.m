function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 2];    
    B = [2, 0, 2];    
    C = [2, 2, 2];    
    D = [0, 2, 2];    
    A1 = [0, 0, 0];   
    B1 = [2, 0, 0];   
    C1 = [2, 2, 0];   
    D1 = [0, 2, 0];   
    M = [0, 0, 1];    
    
    
    vertices = {A, B, C, D, A1, B1, C1, D1, M};
    labels = {point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M};
    
    
    edges_solid = {
        {A, B}, {B, C}, {C, D}, {D, A}, ...  
        {A1, B1}, {B1, C1}, ...  
        {D1, A1}, {D1, D}, {D1, C1},{A, A1}, {B, B1}, {C, C1}   
    };
    
    
    edges_dashed = {
         {B1, M}, {B1, C}  
    };
    
    
    hold on;
    
    
    for i = 1:length(edges_solid)
        p1 = edges_solid{i}{1};
        p2 = edges_solid{i}{2};
        plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], ...
              'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(edges_dashed)
        p1 = edges_dashed{i}{1};
        p2 = edges_dashed{i}{2};
        plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], ...
              'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    for i = 1:length(vertices)
       
        
        text(vertices{i}(1)+0.1, vertices{i}(2)+0.1, vertices{i}(3)+0.1, ...
             labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
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
    