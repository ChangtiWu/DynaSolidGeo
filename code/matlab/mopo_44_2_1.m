function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_M, point_N, point_P, point_Q)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    B = [0, 0, 0];         
    E = [2, 0, 0];         
    N = [4, 0, 0];         
    C = [6, 0, 0];         
    D = [5, 2, 1];         
    
    
    
    A = [1, 2, 6];         
    
    
    P = (B + 2*A)/3;       
    F = (B + P)/2;         
    Q = (D + 2*N)/3;       
    M = (B + D)/2;         
    
    
    

    hold on;          

    
    
    
    
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k', 'LineWidth', 2);  
    plot3([A(1), N(1)], [A(2), N(2)], [A(3), N(3)], 'k', 'LineWidth', 2);  
    plot3([D(1), N(1)], [D(2), N(2)], [D(3), N(3)], 'k', 'LineWidth', 2);  
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k--', 'LineWidth', 1.5);  
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k', 'LineWidth', 2);  
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k', 'LineWidth', 2);  
    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k', 'LineWidth', 2);  
    plot3([E(1), N(1)], [E(2), N(2)], [E(3), N(3)], 'k', 'LineWidth', 2);  
    plot3([N(1), C(1)], [N(2), C(2)], [N(3), C(3)], 'k', 'LineWidth', 2);  
    plot3([B(1), F(1)], [B(2), F(2)], [B(3), F(3)], 'k', 'LineWidth', 2);  
    
    
    
    plot3([P(1), Q(1)], [P(2), Q(2)], [P(3), Q(3)], 'k--', 'LineWidth', 1.5);  
    plot3([A(1), M(1)], [A(2), M(2)], [A(3), M(3)], 'k--', 'LineWidth', 1.5);  
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'k-', 'LineWidth', 2);  
    plot3([M(1), N(1)], [M(2), N(2)], [M(3), N(3)], 'k--', 'LineWidth', 1.5);  
    
    
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k--', 'LineWidth', 1.5);  
    plot3([B(1), N(1)], [B(2), N(2)], [B(3), N(3)], 'k--', 'LineWidth', 1.5);  
    plot3([F(1), P(1)], [F(2), P(2)], [F(3), P(3)], 'k--', 'LineWidth', 1.5);  
    
    
    points = [A; B; C; D; E; N; P; Q; M; F];
    plot3(points(:,1), points(:,2), points(:,3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'k');
    
    
    text(A(1)-0.3, A(2)+0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)-0.3, B(2)-0.2, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2)-0.2, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)+0.2, D(2), D(3)+0.2, point_D, 'FontSize', 14, 'FontWeight', 'bold');
    
    text(N(1)-0.2, N(2)-0.2, N(3), point_N, 'FontSize', 14, 'FontWeight', 'bold');
    text(P(1)-0.3, P(2), P(3)+0.2, point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(Q(1)+0.2, Q(2)-0.2, Q(3), point_Q, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)-0.3, M(2)+0.2, M(3)-0.2, point_M, 'FontSize', 14, 'FontWeight', 'bold');
      

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
    