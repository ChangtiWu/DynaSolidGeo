function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];         B = [2, 0, 0];         C = [2, 3, 0];         D = [0, 3, 0];
    A1 = [0, 0, sqrt(3)];  B1 = [2, 0, sqrt(3)];  C1 = [2, 3, sqrt(3)];  D1 = [0, 3, sqrt(3)];
    
    
    solid_edges = {
        [A; B],   
        [B; B1],  
        [C1; C],  
        [C1; D1], 
        [D1; A1], 
        [A1; A],  
        [B; C],    
        [A1; B1],
        [B1; C1], 
        [A; D],   
        [D; C],   
        [D; D1],  
    };
    
    
    dashed_edges = {

        [B;C1]
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
    
    
    text(A(1)-0.1, A(2)-0.1, A(3)-0.1, point_A, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3)-0.1, point_B, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3)-0.1, point_C, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)+0.1, D(3)-0.1, point_D, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(A1(1)-0.1, A1(2)-0.1, A1(3)+0.1, point_A1, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(B1(1)+0.1, B1(2)-0.1, B1(3)+0.1, point_B1, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(C1(1)+0.1, C1(2)+0.1, C1(3)+0.1, point_C1, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(D1(1)-0.1, D1(2)+0.1, D1(3)+0.1, point_D1, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');

    

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
    