function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_Q)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    A = [-2, 0, 0];    
    C = [2, 0, 0];     
    B = [0, 1, 0];     
    P = [0, 0, 2];     
    Q = [0, 0, -3];    
    
    
    solid_edges = [
        P; A; ...  
        P; C; ...  
        Q; A; ...  
        Q; C; ...  
        A; B; ...  
        B; C; ...  
        P; B; ...  
        A; C; ...
        B; Q];     

    

    hold on;

    
    
    for i = 1:size(solid_edges, 1)/2
        start_idx = 2*i - 1;
        end_idx = 2*i;
        x = [solid_edges(start_idx, 1), solid_edges(end_idx, 1)];
        y = [solid_edges(start_idx, 2), solid_edges(end_idx, 2)];
        z = [solid_edges(start_idx, 3), solid_edges(end_idx, 3)];
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');
    end
    
    
    
    text(A(1)-0.2, A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1), B(2)+0.2, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1), P(2), P(3)+0.2, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(Q(1), Q(2), Q(3)-0.2, point_Q, 'FontSize', 14, 'FontWeight', 'bold');
    


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
    