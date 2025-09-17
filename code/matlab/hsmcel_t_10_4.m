function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_G, point_M)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    B = [0, 0, 0];                     
    C = [1, 0, 0];                     
    D = [0.5, sqrt(3)/2, 0];          
    A = [0.5, sqrt(3)/6, sqrt(6)/3];  
    
    
    G = (B + C + D) / 3;               
    M = (A + G) / 2;                   
    
    
    solid_edges = {
        [A; B];  
        [A; C];  
        [A; D];
        [B; D];
        [B; C];  
        [C; D]   
    };
    
    
    dashed_edges = {
        [A; G];          
        [C; M];  
        [B; M];  
        [D; M]   
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
    
    text(A(1)+0.05, A(2)+0.05, A(3)+0.05, point_A, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(B(1)-0.1, B(2)-0.1, B(3), point_B, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)-0.1, C(3), point_C, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(D(1)+0.05, D(2)+0.05, D(3)-0.05, point_D, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(G(1)-0.1, G(2)+0.05, G(3)+0.05, point_G, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(M(1)+0.05, M(2)-0.05, M(3), point_M, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');



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
    