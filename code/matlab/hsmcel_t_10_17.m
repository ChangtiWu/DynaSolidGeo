function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_M, point_N)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    D = [0, 0, 0];
    A = [4, 0, 0];
    C = [0, 4, 0];
    B = [4, 4, 0];
    P = [0, 0, 6];
    
    
    M = (P + B) / 2;  
    N = (A + B) / 2;  
    
    
    solid_edges = {
        [C; D];   
        [C; P];   
        [C; B];
        [P; A];   
        [P; B];   
        [P; D];   
        [A; B];   
        [D; A];   
        [P; M];           
    };
    
    
    dashed_edges = {          
        [D; M];   
        [D; N];
        [M; N];
        [P; N];
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
    
    
    text(P(1)-0.6, P(2), P(3)+0.6, point_P, 'FontSize', 12, 'Color', 'k');
    text(D(1)-0.6, D(2)-0.6, D(3), point_D, 'FontSize', 12, 'Color', 'k');
    text(A(1)+0.6, A(2)-0.6, A(3), point_A, 'FontSize', 12, 'Color', 'k');
    text(C(1)-0.6, C(2)+0.6, C(3), point_C, 'FontSize', 12, 'Color', 'k');
    text(B(1)+0.6, B(2)+0.6, B(3), point_B, 'FontSize', 12, 'Color', 'k');
    text(M(1), M(2)+0.6, M(3), point_M, 'FontSize', 12, 'Color', 'k');
    text(N(1)+0.6, N(2), N(3), point_N, 'FontSize', 12, 'Color', 'k');
    


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
    