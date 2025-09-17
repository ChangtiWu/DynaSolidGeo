function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0];     
    B = [4, 0];     
    C = [4, 4];     
    D = [0, 4];     
    
    
    
    y_E = 2;                    
    x_E = 4 - 2*sqrt(3);        
    E = [x_E, y_E];             
    
    
    x_F = 2;                    
    y_F = 2*sqrt(3);            
    F = [x_F, y_F];             
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    hold on;
    
    
    plot([A(1) B(1) C(1) D(1) A(1)], ...
         [A(2) B(2) C(2) D(2) A(2)], ...
         'LineWidth', 2, 'Color', 'k');
    
    
    edges = {
        [E; A], [E; B], [E; D], ... 
        [F; B], [F; C], [F; D], ... 
        [E; F]                   
    };
    for i = 1:length(edges)
        edge = edges{i};
        x = edge(:, 1);
        y = edge(:, 2);
        plot(x, y, 'LineWidth', 2, 'Color', 'k');
    end
    
    text(2, -0.2, 'a', 'FontSize', 12, 'Color', 'k', 'HorizontalAlignment', 'center', 'FontWeight', 'bold'); 
    text(4.2, 2, 'a', 'FontSize', 12, 'Color', 'k', 'VerticalAlignment', 'middle', 'FontWeight', 'bold');   
    text((B(1)+E(1))/2, (B(2)+E(2))/2 - 0.3, 'a', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');     
    text((B(1)+F(1))/2 + 0.3, (B(2)+F(2))/2, 'a', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');     
    text(-0.2, 2, 'a', 'FontSize', 12, 'Color', 'k', 'HorizontalAlignment', 'center', 'FontWeight', 'bold'); 
    text(2, 4.2, 'a', 'FontSize', 12, 'Color', 'k', 'HorizontalAlignment', 'center', 'FontWeight', 'bold'); 
    
    
    text((A(1)+E(1))/2 - 0.3, (A(2)+E(2))/2, 'b', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');     
    text((D(1)+E(1))/2 - 0.3, (D(2)+E(2))/2, 'b', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');     
    text((E(1)+F(1))/2 + 0.3, (E(2)+F(2))/2, 'b', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');     
    text((D(1)+F(1))/2 - 0.3, (D(2)+F(2))/2, 'b', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');     
    text((C(1)+F(1))/2 + 0.3, (C(2)+F(2))/2, 'b', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');     
    hold off;
    
    
    patch([D(1), A(1), E(1)], [D(2), A(2), E(2)], [0.8, 0.8, 0.8], 'EdgeColor', 'none', 'FaceAlpha', 0.5);
    
    patch([D(1), C(1), F(1)], [D(2), C(2), F(2)], [0.8, 0.8, 0.8], 'EdgeColor', 'none', 'FaceAlpha', 0.5);




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
    