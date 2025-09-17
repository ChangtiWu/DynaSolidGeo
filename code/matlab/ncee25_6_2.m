
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_F, point_E, point_D_prime, point_A_prime)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    AD = 2;  
    
    
    A = [0, 0, 0];
    D = [0, AD, 0];           
    B = [3*AD, 0, 0];         
    C = [2*AD, AD, 0];        
    
    
    F = [(D(1) + C(1))/2, (D(2) + C(2))/2, 0];  
    
    
    E = [F(1), 0, 0];         

    
    
    
    
    EF_vec = [F(1)-E(1), F(2)-E(2), F(3)-E(3)];  
    EF_unit = EF_vec / norm(EF_vec);  
    
    
    
    angle = 60 * pi / 90;  
    
    
    R = [cos(angle), 0, sin(angle);
         0, 1, 0;
         -sin(angle), 0, cos(angle)];
    
    
    
    A_rel = A - E;  
    D_rel = D - E;  
    
    A_rel_kotated = (R * A_rel')';  
    D_rel_kotated = (R * D_rel')';  
    
    A_prime = E + A_rel_kotated;  
    D_prime = E + D_rel_kotated;  


    hold on;

    
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([F(1), C(1)], [F(2), C(2)], [F(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), B(1)], [C(2), B(2)], [C(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([F(1), D_prime(1)], [F(2), D_prime(2)], [F(3), D_prime(3)], 'k-', 'LineWidth', 2);
    plot3([D_prime(1), A_prime(1)], [D_prime(2), A_prime(2)], [D_prime(3), A_prime(3)], 'k-', 'LineWidth', 2);
    plot3([A_prime(1), E(1)], [A_prime(2), E(2)], [A_prime(3), E(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 1.5);
    plot3([D(1), F(1)], [D(2), F(2)], [D(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), E(1)], [A(2), E(2)], [A(3), E(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([A_prime(1), B(1)], [A_prime(2), B(2)], [A_prime(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([D_prime(1), C(1)], [D_prime(2), C(2)], [D_prime(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([D_prime(1), B(1)], [D_prime(2), B(2)], [D_prime(3), B(3)], 'k-', 'LineWidth', 2);
    
    text(A(1)-0.2, A(2)-0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)-0.2, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.2, D(2)+0.1, D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1), E(2)-0.2, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1), F(2)+0.1, F(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(A_prime(1)-0.2, A_prime(2)-0.2, A_prime(3)-0.2, point_A_prime, 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'black');
    text(D_prime(1)-0.2, D_prime(2)+0.1, D_prime(3)-0.2, point_D_prime, 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'black');
    
    
    plot3(A(1), A(2), A(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(B(1), B(2), B(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(C(1), C(2), C(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(D(1), D(2), D(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(E(1), E(2), E(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(F(1), F(2), F(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(A_prime(1), A_prime(2), A_prime(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(D_prime(1), D_prime(2), D_prime(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');


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
    