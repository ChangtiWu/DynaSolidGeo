function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_A1, point_B1, point_C1, point_O, point_O1)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    a = 2;                
    R = a / sqrt(3);      
    
    
    A = [R, 0, 0];        B = [-R/2, (R*sqrt(3))/2, 0];    C = [-R/2, -(R*sqrt(3))/2, 0];
    A1 = [R, 0, a];       B1 = [-R/2, (R*sqrt(3))/2, a];   C1 = [-R/2, -(R*sqrt(3))/2, a];
    
    
    O = [0, 0, 0];        O1 = [0, 0, a];
    
    
    D = [R*cos(pi/4), R*sin(pi/4), 0];   D1 = [R*cos(pi/4), R*sin(pi/4), a];
    E = [R*cos(3*pi/4), R*sin(3*pi/4), 0]; E1 = [R*cos(3*pi/4), R*sin(3*pi/4), a];
    
    
    
    hold on;         
    
    
    [X,Y,Z] = cylinder(R, 50);
    Z = Z * a;
    surf(X, Y, Z, 'FaceAlpha', 0.3, 'FaceColor', [0.8 0.8 1], 'EdgeColor', 'none');
    
    
    
    
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k--', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k', 'LineWidth', 2);
    
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k', 'LineWidth', 2);
    plot3([C1(1), A1(1)], [C1(2), A1(2)], [C1(3), A1(3)], 'k', 'LineWidth', 2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k--', 'LineWidth', 2);
    plot3([C(1), A(1)], [C(2), A(2)], [C(3), A(3)], 'k', 'LineWidth', 2);
    
    
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k', 'LineWidth', 2);
    
    
    
    
    
    theta = linspace(0, 2*pi, 100);  
    x_circle = R * cos(theta);
    y_circle = R * sin(theta);
    z_circle = zeros(size(theta));
    plot3(x_circle, y_circle, z_circle, 'k', 'LineWidth', 1.5);
    
    
    z_circle1 = ones(size(theta)) * a;
    plot3(x_circle, y_circle, z_circle1, 'k', 'LineWidth', 1.5);
    
    
    plot3([O(1), O1(1)], [O(2), O1(2)], [O(3), O1(3)], 'k--', 'LineWidth', 1.5);
    
    
    
    text(A(1)+0.1, A(2)+0.1, A(3)+0.1, point_A, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)+0.1, B(3)+0.1, point_B, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');
    text(C(1)+0.1, C(2)+0.1, C(3)+0.1, point_C, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');
    text(A1(1)+0.1, A1(2)+0.1, A1(3)+0.1, point_A1, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');
    text(B1(1)+0.1, B1(2)+0.1, B1(3)+0.1, point_B1, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');
    text(C1(1)+0.1, C1(2)+0.1, C1(3)+0.1, point_C1, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');
    text(O(1), O(2), O(3), point_O, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');
    text(O1(1), O1(2), O1(3), point_O1, 'FontSize', 14, 'HorizontalAlignment', 'center', 'FontWeight', 'bold');



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
    