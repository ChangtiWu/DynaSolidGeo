function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    D  = [0, 0, 0];
    A  = [1, 0, 0];
    B  = [1, 1, 0];
    C  = [0, 1, 0];
    D1 = [0, 0, 1];
    A1 = [1, 0, 1];
    B1 = [1, 1, 1];
    C1 = [0, 1, 1];
    M  = (A + B)/2;  
    N  = (C1 + D1)/2;
    
    
    dashed_edges = { ...
        [M; B1],  ... 
        [N; B1],   ... 
        [D; M],   ... 
        [D; N]    ... 
    };
    
    solid_edges = { ...
        [D; A],   ... 
        [D; C],   ... 
        [D; D1],  ... 
        [A; B],   ... 
        [B; B1],  ... 
        [A1; B1],... 
        [B; C], ...
        [C; C1], ...
        [B1; C1], ... 
        [C1; D1], ... 
        [D1; A1], ... 
        [A1; A]  ... 
        
    };
    
    
    hold on;
    
    
    for i = 1:length(dashed_edges)
        edge = dashed_edges{i};
        x = edge(:,1); y = edge(:,2); z = edge(:,3);
        plot3(x, y, z, 'Color', [0.5, 0.5, 0.5], 'LineWidth', 1.5, 'LineStyle', '--');
    end
    
    
    for i = 1:length(solid_edges)
        edge = solid_edges{i};
        x = edge(:,1); y = edge(:,2); z = edge(:,3);
        plot3(x, y, z, 'Color', 'k', 'LineWidth', 2, 'LineStyle', '-');
    end
    
    
    points = [D; A; B; C; D1; A1; B1; C1; M; N];  
    labels = {point_D,point_A,point_B,point_C,'D1',point_A1,point_B1,point_C1,point_M,point_N};  
    
    
    
    
    
    for i = 1:length(labels)
        text(points(i,1), points(i,2), points(i,3)+0.09, labels{i}, ...
            'HorizontalAlignment', 'center', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
    end



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
    