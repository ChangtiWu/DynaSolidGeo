%  1. function header (fixed)
function visual(mode, azimuth, elevation, point_P, point_A, point_B, point_C, point_D, point_E, point_F)
    % mode parameter: 0=save current view image, 1=save rotation animation video
    
    % Close all existing figure windows and create a new invisible window
    close all;
    fig = figure('Visible', 'off');

% 2. establish coordinate system according to the problem conditions (need change)
    hold on;

    A = [0, 2, 2];      
    B = [2, 2, 2];       
    C = [0, 2, 0];      
    D = [0, 2, 4];      
    

    P = [0.5, 1.5, 1.5];
    
    D_P = [0, 2, 1.5];    
    E_P = [-1, 2, 0];    
    F_P = [1.8, 2, 0.5];      
    

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([B(1), F_P(1)], [B(2), F_P(2)], [B(3), F_P(3)], 'k-', 'LineWidth', 1.5);
    

    
    plot3([E_P(1), C(1)], [E_P(2), C(2)], [E_P(3), C(3)], 'k-', 'LineWidth', 1.5);
    plot3([F_P(1), B(1)], [F_P(2), B(2)], [F_P(3), B(3)], 'k-', 'LineWidth', 1.5);
    

    
    plot3([E_P(1), A(1)], [E_P(2), A(2)], [E_P(3), A(3)], 'k-', 'LineWidth', 1.5);
    plot3([F_P(1), C(1)], [F_P(2), C(2)], [F_P(3), C(3)], 'k-', 'LineWidth', 1.5);
    
    text(A(1), A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1), B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1), D(2), D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    

    
    
    text(E_P(1), E_P(2), E_P(3), 'E(P)', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'black');
    text(F_P(1), F_P(2), F_P(3), 'F(P)', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'black');
    

    
    
    plot3(E_P(1), E_P(2), E_P(3), 'bo', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(F_P(1), F_P(2), F_P(3), 'bo', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
   

% 4. save (fixed)
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
    