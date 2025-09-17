function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_E, point_F)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];          
    B = [2, 0, 0];          
    C = [2, 2, 0];          
    D = [0, 4, 0];          
    P = [0, 0, 2];          
    E = (P + D) / 2;        
    F = (P + C) / 2;        
    
    
    solid_edges = {
        [P; A],   
        [A; B],     
        [A; D],   
        [B; C],   
        [C; D],   
        [D; P],   
        [P; B],   
        [P; C],
        
    };
    
    
    dashed_edges = {
        [F;B],
        [F;E],
        [C;E],
        [F;D],
        [A; F],   
        [F; E],   
        [A; E]    
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
    text(P(1)-0.1, P(2)-0.1, P(3)+0.1, point_P, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(E(1), E(2)+0.1, E(3), point_E, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');
    text(F(1), F(2), F(3)+0.1, point_F, 'FontSize', 14, 'Color', 'k', 'FontWeight', 'bold');





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
    