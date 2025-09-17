function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_A_prime, point_B_prime, point_C_prime, point_D_prime)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    A = [0, 0, 0];
    B = [4, 0, 0];
    D = [0, 3, 0];
    C = B + D - A;  
    

    len_AA = 3;
    theta = 60;     
    x_Ap = len_AA * cosd(theta);
    y_Ap = len_AA * cosd(theta);
    z_Ap = sqrt(len_AA^2 - x_Ap^2 - y_Ap^2);
    A_prime = [x_Ap, y_Ap, z_Ap];
    
 
    B_prime = B + A_prime - A;
    D_prime = D + A_prime - A;
    C_prime = C + A_prime - A;
    
    
    solid_edges = {
        [A; B],       
        [B; C],       
        [B; B_prime], 
        [B_prime; C_prime], 
        [C; C_prime],
        [C_prime; D_prime], 
        [D_prime; A_prime],
        [A_prime; A], 
        [D; C],       
        [D; D_prime], 
        [A; D],
        [B_prime; A_prime]
    };
    
    dashed_edges = {
        
        [A; C_prime]
    };
    
    
    hold on;
    
    
    for i = 1:length(solid_edges)
        edge = solid_edges{i};
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineWidth', 2, 'Color', 'k');
    end
    
    
    for i = 1:length(dashed_edges)
        edge = dashed_edges{i};
        plot3(edge(:,1), edge(:,2), edge(:,3), 'LineStyle', '--', 'LineWidth', 1.5, 'Color', 'k');
    end
    
    
    text(A(1)-0.1, A(2)-0.1, A(3)-0.1, point_A, 'FontSize', 14, 'Color', 'k');
    text(B(1)+0.1, B(2)-0.1, B(3)-0.1, point_B, 'FontSize', 14, 'Color', 'k');
    text(C(1)+0.1, C(2)+0.1, C(3)-0.1, point_C, 'FontSize', 14, 'Color', 'k');
    text(D(1)-0.1, D(2)+0.1, D(3)-0.1, point_D, 'FontSize', 14, 'Color', 'k');
    text(A_prime(1)-0.1, A_prime(2)-0.1, A_prime(3)+0.1, point_A_prime, 'FontSize', 14, 'Color', 'k');
    text(B_prime(1)+0.1, B_prime(2)-0.1, B_prime(3)+0.1, point_B_prime, 'FontSize', 14, 'Color', 'k');
    text(C_prime(1)+0.1, C_prime(2)+0.1, C_prime(3)+0.1, point_C_prime, 'FontSize', 14, 'Color', 'k');
    text(D_prime(1)-0.1, D_prime(2)+0.1, D_prime(3)+0.1, point_D_prime, 'FontSize', 14, 'Color', 'k');
    




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
    