function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N, point_E)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];     B = [1, 0, 0];     C = [1, 1, 0];     D = [0, 1, 0];
    A1 = [0, 0, 1];    B1 = [1, 0, 1];    C1 = [1, 1, 1];    D1 = [0, 1, 1];
    
    
    M = (A + B) / 2;   
    N = (C + C1) / 2;  
    E = (B + D) / 2;   
    
    
    solid_edges = {
        [A; B],   
        [B; C],
    
        [A; A1],
        [B; B1],
        [C; C1],
             
        [C; D],
        [D; A],
        [A1; B1],
        [B1; C1],
        [C1; D1],
        [D; D1],
        [D1; A1]
    };
    
    
    dashed_edges = {
        [B; D],       
        [M; D1], 
        [E; N]       
    
    };
    
    
    hold on;
    
    
    for i = 1:length(dashed_edges)
        edge = dashed_edges{i};
        
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    for i = 1:length(solid_edges)
        edge = solid_edges{i};
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineWidth', 2, 'Color', 'k');
    end
    
    
    text(A(1)-0.05, A(2)-0.05, A(3)-0.05, point_A, 'FontSize', 14);
    text(B(1)+0.05, B(2)-0.05, B(3)-0.05, point_B, 'FontSize', 14);
    text(C(1)+0.05, C(2)+0.05, C(3)-0.05, point_C, 'FontSize', 14);
    text(D(1)-0.05, D(2)+0.05, D(3)-0.05, point_D, 'FontSize', 14);
    text(A1(1)-0.1, A1(2)-0.1, A1(3)+0.1, point_A1, 'FontSize', 14);
    text(B1(1)+0.05, B1(2)-0.05, B1(3)+0.05, point_B1, 'FontSize', 14);
    text(C1(1)+0.05, C1(2)+0.05, C1(3)+0.05, point_C1, 'FontSize', 14);
    text(D1(1)-0.05, D1(2)+0.05, D1(3)+0.05, point_D1, 'FontSize', 14);
    text(M(1), M(2)-0.05, M(3)-0.05, point_M, 'FontSize', 14);
    text(N(1)+0.05, N(2)+0.05, N(3)+0.05, point_N, 'FontSize', 14);
    text(E(1), E(2), E(3)-0.05, point_E, 'FontSize', 14);
    
    hold off;



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
    