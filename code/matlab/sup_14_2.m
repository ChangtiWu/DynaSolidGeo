function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_O)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    B = [0, 0, 0];           
    B1 = [1, sqrt(3), 0];    
    C = [2, 0, 0];           
    C1 = [3, sqrt(3), 0];    
    O = [(B1(1)+C(1))/2, (B1(2)+C(2))/2, 0];  
    A = [O(1), O(2), 2];      
    A1 = A + (B1 - B);        
    
    
    solid_edges = {
        [A; B],   
        [B; B1],  
        [B1; C1], 
        [C1; A1], 
        [A1; A],  
        [A; C],   
        [C; C1],
        [C; B],
        [A1; B1]
    };
    
    
    dashed_edges = {
        [B; C1],  
        [B1; C],  
        [A; O],
        [A; B1],
        [A; C1],
        
    };
    
    
    hold on;
    
    
    for i = 1:length(solid_edges)
        edge = solid_edges{i};
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(dashed_edges)
        edge = dashed_edges{i};
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    text(A(1)+0.1, A(2)+0.1, A(3)+0.1, point_A, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(B(1)-0.1, B(2)-0.1, B(3)-0.1, point_B, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(B1(1), B1(2)+0.1, B1(3)-0.1, point_B1, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)-0.1, C(3)-0.1, point_C, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(C1(1)+0.1, C1(2)+0.1, C1(3)-0.1, point_C1, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(A1(1)+0.1, A1(2)+0.1, A1(3)+0.1, point_A1, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(O(1), O(2), O(3)-0.1, point_O, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');



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
    