function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_M)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 6];    
    B = [4, 0, 0];    
    C = [-4, 0, 0];   
    M = [0, 0, 2];    
    
    
    solid_edges = {
        [A; B];  
        [A; C];  
        [B; C]  
    };
    
    
    dashed_edges = {
        [M; A];  
        [M; B];  
        [M; C]   
    };
    
    
    hold on;
    
    
    
    for i = 1:length(solid_edges)
        edge = solid_edges{i};
        x = edge(:, 1); y = edge(:, 2); z = edge(:, 3);
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(dashed_edges)
        edge = dashed_edges{i};
        x = edge(:, 1); y = edge(:, 2); z = edge(:, 3);
        plot3(x, y, z, 'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    text(A(1), A(2), A(3)+0.5, point_A, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(B(1)+0.5, B(2), B(3), point_B, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(C(1)-0.5, C(2), C(3), point_C, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(M(1), M(2), M(3)-0.5, point_M, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    


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
    