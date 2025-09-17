function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    D = [0, 0, 0];
    C = [1, 0, 0];
    B = [1, 1, 0];
    A = [0, 1, 0];
    D1 = [0, 0, 1];
    C1 = [1, 0, 1];
    B1 = [1, 1, 1];
    A1 = [0, 1, 1];
    AE = 1 - sqrt(6)/3;  
    E = [0, 1, AE];      
    
    
    solid_edges = {
        [D1; D],      
        [D; A],       
        [D; C],       
        [A; B],       
        [B; C],       
        [B; B1],      
        [C; C1],      
        [C1; B1],     
        [B1; A1],     
        [A1; E],      
        [E; A],       
        [A1; D1],     
        [D1; C1]    
    };
    
    
    dashed_edges = {
        
        [D1; C],      
        [D1; E],
        [C; E], 
    };
    
    
    hold on;
    
    
    
    for i = 1:length(solid_edges)
        edge = solid_edges{i};
        x = edge(:, 1);
        y = edge(:, 2);
        z = edge(:, 3);
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(dashed_edges)
        edge = dashed_edges{i};
        x = edge(:, 1);
        y = edge(:, 2);
        z = edge(:, 3);
        plot3(x, y, z, 'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    text(A(1), A(2), A(3), point_A, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(B(1), B(2), B(3), point_B, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(D(1), D(2), D(3), point_D, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(A1(1), A1(2), A1(3), 'A1', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(B1(1), B1(2), B1(3), 'B1', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(C1(1), C1(2), C1(3), 'C1', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(D1(1), D1(2), D1(3), 'D1', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(E(1), E(2), E(3), point_E, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');



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
    