function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_E, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];   
    B = [1, 0, 0];   
    D = [0, 2, 0];   
    C = [2, 2, 0];   
    P = [0, 0, 2];   
    E = [(0+2)/2, (0+2)/2, (2+0)/2]; 
    F = [(2+0)/2, 2, 0];              
    
    
    edges_solid = {
        {P, A}, {A, B}, {B, C},...  
        {P, B}, {P, C}, ...                          
        {D, P}, {D, A}, {D, C}                            
    };
    
    
    edges_dashed = {
        {D, E}, {D, F},   {D, B},  {E, F}, {B, F}, {B, E}
    };
    
    
    hold on; 
    
    
    for i = 1:length(edges_solid)
        p1 = edges_solid{i}{1}; p2 = edges_solid{i}{2};
        plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], ...
              'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(edges_dashed)
        p1 = edges_dashed{i}{1}; p2 = edges_dashed{i}{2};
        plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], ...
              'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    vertices = {A,B,C,D,P,E,F}; labels = {point_A,point_B,point_C,point_D,point_P,point_E,point_F};
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
    