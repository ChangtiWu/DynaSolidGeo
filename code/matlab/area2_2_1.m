function visual(mode, azimuth, elevation, point_S, point_A, point_B, point_C, point_D, point_O)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    
    base_side = 4;  
    O = [0, 0, 0];  
    A = [-base_side/2, -base_side/2, 0];
    B = [base_side/2, -base_side/2, 0];
    C = [base_side/2, base_side/2, 0];
    D = [-base_side/2, base_side/2, 0];
    
    
    height = 5;     
    S = [0, 0, height];
    
    
    E = [base_side/2, 0, 0];  
    
    
    hold on;
    
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), C(1)], [S(2), C(2)], [S(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), E(1)], [S(2), E(2)], [S(3), E(3)], 'k--', 'LineWidth', 2);  
    plot3([S(1), D(1)], [S(2), D(2)], [S(3), D(3)], 'k-', 'LineWidth', 2);  
    
    
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([S(1), O(1)], [S(2), O(2)], [S(3), O(3)], 'k--', 'LineWidth', 1.5);  
    plot3([O(1), E(1)], [O(2), E(2)], [O(3), E(3)], 'k--', 'LineWidth', 1.5);  
    
    
    text(A(1)-0.1, A(2)-0.1, A(3), point_A, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.1, B(3), point_B, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(D(1)-0.1, D(2)+0.1, D(3), point_D, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(S(1), S(2), S(3)+0.1, point_S, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(O(1), O(2), O(3)-0.1, point_O, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    

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
    