function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M, point_N)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];
    B = [2, 0, 0];
    C = [1, sqrt(3), 0];
    A1 = [0, 0, 2];
    B1 = [2, 0, 2];
    C1 = [1, sqrt(3), 2];
    
    
    M = (B + B1) / 2;
    N = (B1 + C1) / 2;
    
    
    solid_edges = {
        [A1; A];   
        [A; B];   
        [B; B1];  
        [B1; A1];  
        [B1; N];   
        [N; C1];   
        [C1; C];  
        [C1; A1];
        [A;C];
        [B;C]
    
    };
    
    
    dashed_edges = {
    
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
    
    
    plot3(M(1), M(2), M(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'k');
    plot3(N(1), N(2), N(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'k');
    
    
    text(A(1), A(2), A(3), point_A, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'bottom', 'FontWeight', 'bold');
    text(B(1), B(2), B(3), point_B, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'bottom', 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'top', 'FontWeight', 'bold');
    text(A1(1), A1(2), A1(3), point_A1, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'top', 'FontWeight', 'bold');
    text(B1(1), B1(2), B1(3), point_B1, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'top', 'FontWeight', 'bold');
    text(C1(1), C1(2), C1(3), point_C1, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'top', 'FontWeight', 'bold');
    text(M(1), M(2), M(3), point_M, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'bottom', 'FontWeight', 'bold');
    text(N(1), N(2), N(3), point_N, 'FontSize', 10, 'Color', 'k', 'VerticalAlignment', 'top', 'FontWeight', 'bold');



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
    