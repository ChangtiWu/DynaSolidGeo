
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_P, point_M)
    

    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    A = [0, 0, 0];          
    C = [3, 2, 0];          
    D = [4, 0, 0];          
    M = [2,0.8,1.2];

    
    
    
    
    
    P = [1.5, 1, 1.5];      



    hold on;

    
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);  
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);   
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);   
    plot3([C(1), M(1)], [C(2), M(2)], [C(3), M(3)], 'k--', 'LineWidth', 2);   
    plot3([M(1), A(1)], [M(2), A(2)], [M(3), A(3)], 'k--', 'LineWidth', 2);   

    
    plot3([A(1), P(1)], [A(2), P(2)], [A(3), P(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), C(1)], [P(2), C(2)], [P(3), C(3)], 'k-', 'LineWidth', 2);   
    plot3([P(1), D(1)], [P(2), D(2)], [P(3), D(3)], 'k-', 'LineWidth', 2);  

    
    scatter3(A(1), A(2), A(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(P(1), P(2), P(3), 100, 'ko', 'filled');
    scatter3(M(1), M(2), M(3), 100, 'ko', 'filled');

    
    text(A(1)-0.1, A(2)-0.1, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+0.1, D(2)-0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1)+0.1, P(2), P(3)+0.1, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)+0.1, M(2)-0.1, M(3)-0.1, point_M, 'FontSize', 14, 'FontWeight', 'bold');


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
    