function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_F, point_E, point_N)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    A = [0, 0, 0];        
    B = [4, 0, 0];        
    D = [0, 3, 0];        
    C = [4, 3, 0];        
    N = [0, 1.5, 0];      
    
    
    E = [0, 1.5, 1];      
    F = [2, 1.5, 1];      
    
    
    solid_edges = [
        E; A; ...  
        A; B; ...  
        B; C; ...  
        C; F; ...  
        F; E; ...  
        B; F; ...  
        D; C; ...  
        E; D; ...  
        D; N; ...  
        A; N];     
    
    
    dashed_edges = [
        N; B; ...  
        E; N; ...  
        F; N];     
    
    
    hold on;

    
    
    for i = 1:size(solid_edges, 1)/2
        start_idx = 2*i - 1;
        end_idx = 2*i;
        x = [solid_edges(start_idx, 1), solid_edges(end_idx, 1)];
        y = [solid_edges(start_idx, 2), solid_edges(end_idx, 2)];
        z = [solid_edges(start_idx, 3), solid_edges(end_idx, 3)];
        plot3(x, y, z, 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:size(dashed_edges, 1)/2
        start_idx = 2*i - 1;
        end_idx = 2*i;
        x = [dashed_edges(start_idx, 1), dashed_edges(end_idx, 1)];
        y = [dashed_edges(start_idx, 2), dashed_edges(end_idx, 2)];
        z = [dashed_edges(start_idx, 3), dashed_edges(end_idx, 3)];
        plot3(x, y, z, 'LineWidth', 1.5, 'LineStyle', '--', 'Color', 'k');
    end
    
    
    text(A(1)-0.3, A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.3, D(2), D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1)-0.3, E(2), E(3)+0.2, point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1)+0.1, F(2), F(3)+0.2, point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(N(1)-0.3, N(2), N(3), point_N, 'FontSize', 14, 'FontWeight', 'bold');
    
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

        camzoom(0.7);

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
    