function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_P, point_Q)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];       
    D = [4, 0, 0];       
    Q = [0, 0, 2];       
    P = [0, 0, 4];       
    B = [1, 3, 0];       
    C = B + D - A;       
    
    dashed_edges = [];
    solid_edges = [
        P; Q; ...  
        Q; B; ...  
        B; D; ...  
        B; C; ...  
        C; D; ...  
        Q; D; ...
        Q; A; ...  
        A; D; ...
        A; B];     
    
    
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
    
    
    point_labels = {point_A,point_B,point_C,point_D,point_Q,point_P};
    points = [A; B; C; D; Q; P];
    for i = 1:size(points, 1)
        dx = 0.2; dy = 0.2; dz = 0.2;
        if strcmp(point_labels{i}, point_A)
            dy = -0.3;  
        elseif strcmp(point_labels{i}, point_D)
            dx = 0.3;   
        elseif strcmp(point_labels{i}, point_P)
            dz = 0.3;   
        end
        text(points(i,1)+dx, points(i,2)+dy, points(i,3)+dz, point_labels{i}, ...
            'FontSize', 12, 'HorizontalAlignment', 'left', 'FontWeight', 'bold');
    end
    
    
    xlim([-1, 6]);
    ylim([-1, 4]);
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
    