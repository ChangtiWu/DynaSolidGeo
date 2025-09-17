function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    D = [0, 0, 0];     A = [1, 0, 0];     B = [1, 1, 0];     C = [0, 1, 0];
    D1 = [0, 0, 1];    A1 = [1, 0, 1];    B1 = [1, 1, 1];    C1 = [0, 1, 1];
    
    
    P = B + (C1 - B)/3;  
    Q = (B + D)/2;       
    
    
    solid_edges = {
        [D; A];   
        [D; D1];  
        [D; C];
        [A; B];  
        [B; C];   
        [C; C1];  
        [C1; B1]; 
        [B1; A1]; 
        [A1; A];  
        [B; B1];
        
        [C1; D1];
        [A1;D1]
    };
    
    
    dashed_edges = {
        [B; C1];
        [P; Q];   
        [P; D1]   
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
    
    
    text(A(1)+0.1, A(2)-0.1, A(3), point_A, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)+0.1, B(3), point_B, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(C(1)-0.1, C(2)+0.1, C(3), point_C, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)-0.1, D(3), point_D, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(A1(1)+0.1, A1(2)-0.1, A1(3), point_A1, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(B1(1)+0.1, B1(2)+0.1, B1(3), point_B1, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(C1(1)-0.1, C1(2)+0.1, C1(3), point_C1, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(D1(1)-0.1, D1(2)-0.1, D1(3), point_D1, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(P(1), P(2)+0.1, P(3), point_P, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    text(Q(1), Q(2), Q(3)-0.1, point_Q, 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');


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
    