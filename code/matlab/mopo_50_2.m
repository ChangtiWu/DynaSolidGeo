function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_P, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];       
    B = [2, 0, 0];       
    D = [0, 1, 0];       
    C = [2, 1, 0];       
    A1 = [0, 0, 1];      
    B1 = [2, 0, 1];      
    D1 = [0, 1, 1];      
    C1 = [2, 1, 1];      
    E = (A + B) / 2;     
    F = (D1 + C1) / 2;   
    P = [1, 0.5, 0];     
    
    
    solid_edges = [
        A; D; ...    
        D; C; ...    
        D; D1; ...   
        A1; D1; ...  
        D1; F; ...   
        F; C1; ...   
        C1; C; ...   
        C; B; ...    
        B; A; ...    
        A; A1; ...   
        A1; B1; ...  
        B1; C1; ...  
        B; B1];      
    
    
    dashed_edges = [
        B1; C; ...   
        E; P; ...    
        B; P; ...    
        C; P; ...    
        B1; P; ...   
        C; F];       
    
    
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
    
    
    text(A(1)-0.1, A(2)-0.1, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.1, D(2)+0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1)-0.1, A1(2)-0.1, A1(3)+0.1, point_A1, 'FontSize', 14, 'FontWeight', 'bold');
    text(B1(1)+0.1, B1(2)-0.1, B1(3)+0.1, point_B1, 'FontSize', 14, 'FontWeight', 'bold');
    text(C1(1)+0.1, C1(2)+0.1, C1(3)+0.1, point_C1, 'FontSize', 14, 'FontWeight', 'bold');
    text(D1(1)-0.1, D1(2)+0.1, D1(3)+0.1, point_D1, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1), E(2)-0.1, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1), F(2)+0.1, F(3)+0.1, point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1), P(2), P(3)-0.1, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    
    
    xlim([-0.5, 2.5]);
    ylim([-0.5, 1.5]);
    zlim([-0.5, 2.5]);  


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
    