function visual(mode, azimuth, elevation, point_S, point_A, point_B, point_C, point_D, point_P)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [-1, -1, 0];
    B = [1, -1, 0];
    C = [1, 1, 0];
    D = [-1, 1, 0];
    O = [0, 0, 0];    
    S = [0, 0, 2];    
    
    
    hold on;

    
    
    outer_edges = {
        [S; D], [S; A], [S; B], [S; C], ...  
        [A; B], [B; C], [C; D], [D; A]  
    };
    
    for i = 1:length(outer_edges)
        edge = outer_edges{i};  
        p1 = edge(1,:);         
        p2 = edge(2,:);         
        plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], ...
              'k-', 'LineWidth', 2);  
    end
    
    
    aux_edges = {
        [S; O], ...  
        [A; C], [B; D]       
    };
    
    for i = 1:length(aux_edges)
        edge = aux_edges{i};  
        p1 = edge(1,:);       
        p2 = edge(2,:);       
        plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], ...
              'k--', 'LineWidth', 1.5);  
    end
    
    
    points = {S, A, B, C, D};
    labels = {point_S, point_A, point_B, point_C, point_D};
    
    for i = 1:length(points)
        p = points{i};  
        
        plot3(p(1), p(2), p(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'k');
        
        text(p(1)+0.1, p(2)+0.1, p(3)+0.1, labels{i}, 'FontSize', 14, 'FontWeight', 'bold');
    end
    
    
    xlim([-1.5, 1.5]);  
    ylim([-1.5, 1.5]);  
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
    