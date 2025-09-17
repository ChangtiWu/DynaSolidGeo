function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_F, point_E)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 1, 3];     
    B = [-1, 0, 3];    
    C = [1, 0, 3];     
    D = [0, 0, 3];     
    A1 = [0, 1, 0];    
    B1 = [-1, 0, 0];   
    C1 = [1, 0, 0];    
    F = [-1, 0, 1];    
    E = [0, 0.5, 3];   
    
    
    vertices = {A, B, C, D, A1, B1, C1, E, F};
    labels = {point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_E, point_F};
    
    
    edges_solid = {
        {A, B}, {B, C}, {C, A}, ...       
         {B1, C1}, {C1, A1}, ... 
        {A, A1}, {B, B1}, {C, C1} ,  {A1, B1}      
    };
    
    
    edges_dashed = {
       {F, C1} ,{D, A},{E, F}
    };
    
    
    hold on;
    
    
    for i = 1:length(edges_solid)
        edge = edges_solid{i};
        x = [edge{1}(1), edge{2}(1)];
        y = [edge{1}(2), edge{2}(2)];
        z = [edge{1}(3), edge{2}(3)];
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(edges_dashed)
        edge = edges_dashed{i};
        x = [edge{1}(1), edge{2}(1)];
        y = [edge{1}(2), edge{2}(2)];
        z = [edge{1}(3), edge{2}(3)];
        plot3(x, y, z, 'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    for i = 1:length(vertices)
        
        offset = 0.15;
        text(vertices{i}(1) + offset, vertices{i}(2) + offset, vertices{i}(3) + offset, ...
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
    