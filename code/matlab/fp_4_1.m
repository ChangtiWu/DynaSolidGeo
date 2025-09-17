
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_O1, point_O2, point_M)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    bottom_radius = 3;    
    top_radius = 1.5;     
    height = 2.5;         
    
    
    O1 = [0, 0, 0];       
    O2 = [0, 0, height];  
    

    A = [-bottom_radius, 0, 0];  
    B = [bottom_radius, 0, 0];   
    D = [-top_radius, 0, height]; 
    C = [top_radius, 0, height];  
    

    M_angle = pi/-1.5;  
    M = [top_radius*cos(M_angle), top_radius*sin(M_angle), height];


    hold on;
    
    theta = linspace(0, 2*pi, 100);
    bottom_x = bottom_radius * cos(theta);
    bottom_y = bottom_radius * sin(theta);
    bottom_z = zeros(size(theta));
    

    top_x = top_radius * cos(theta);
    top_y = top_radius * sin(theta);
    top_z = height * ones(size(theta));
    

    [R,Z] = meshgrid(linspace(0,1,20), linspace(0,1,20));
    X = (bottom_radius*(1-Z) + top_radius*Z) .* cos(2*pi*R);
    Y = (bottom_radius*(1-Z) + top_radius*Z) .* sin(2*pi*R);
    Z = height * Z;
    

    surf(X, Y, Z, 'FaceAlpha', 0.3, 'EdgeAlpha', 0.1, 'FaceColor', [0.8 0.8 0.8]);
    

    plot3(bottom_x, bottom_y, bottom_z, 'k-', 'LineWidth', 2);
    

    plot3(top_x, top_y, top_z, 'k-', 'LineWidth', 2);
    

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5);
    

    plot3([D(1), C(1)], [D(2), C(2)], [D(3), C(3)], 'k-', 'LineWidth', 1.5);
    

    plot3([O1(1), O2(1)], [O1(2), O2(2)], [O1(3), O2(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([M(1), O1(1)], [M(2), O1(2)], [M(3), O1(3)], 'k--', 'LineWidth', 1);
    plot3([D(1), O1(1)], [D(2), O1(2)], [D(3), O1(3)], 'k--', 'LineWidth', 1);

    scatter3(A(1), A(2), A(3), 100, 'ko', 'filled');
    scatter3(B(1), B(2), B(3), 100, 'ko', 'filled');
    scatter3(C(1), C(2), C(3), 100, 'ko', 'filled');
    scatter3(D(1), D(2), D(3), 100, 'ko', 'filled');
    scatter3(M(1), M(2), M(3), 120, 'ko', 'filled');
    scatter3(O1(1), O1(2), O1(3), 80, 'ko', 'filled');
    scatter3(O2(1), O2(2), O2(3), 80, 'ko', 'filled');
    

    text(A(1)-0.2, A(2)-0.2, A(3)+0.1, point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2)-0.2, B(3)+0.1, point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)+0.2, C(2)-0.2, C(3)+0.1, point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1)-0.2, D(2)-0.2, D(3)+0.1, point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(M(1)+0.1, M(2)+0.1, M(3)+0.1, point_M, 'FontSize', 14, 'FontWeight', 'bold');
    text(O1(1)+0.1, O1(2)-0.3, O1(3)+0.1, point_O1, 'FontSize', 12, 'FontWeight', 'bold');
    text(O2(1)+0.1, O2(2)-0.3, O2(3)+0.1, point_O2, 'FontSize', 12, 'FontWeight', 'bold');


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
    