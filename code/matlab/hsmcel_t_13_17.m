function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_A1, point_B1, point_C1, point_D1, point_E1)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    r = 2;         
    h = 3;         
    theta = 0:2*pi/5:2*pi; 
    theta = theta(1:5);    
    
    
    x = r * cos(theta);
    y = r * sin(theta);
    A = [x(1), y(1), 0];
    B = [x(2), y(2), 0];
    C = [x(3), y(3), 0];
    D = [x(4), y(4), 0];
    E = [x(5), y(5), 0];
    
    
    A1 = [x(1), y(1), h];
    B1 = [x(2), y(2), h];
    C1 = [x(3), y(3), h];
    D1 = [x(4), y(4), h];
    E1 = [x(5), y(5), h];

    hold on;    

    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), E(1)], [D(2), E(2)], [D(3), E(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), A(1)], [E(2), A(2)], [E(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([B1(1), C1(1)], [B1(2), C1(2)], [B1(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([C1(1), D1(1)], [C1(2), D1(2)], [C1(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([D1(1), E1(1)], [D1(2), E1(2)], [D1(3), E1(3)], 'k-', 'LineWidth', 2);
    plot3([E1(1), A1(1)], [E1(2), A1(2)], [E1(3), A1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), C1(1)], [C(2), C1(2)], [C(3), C1(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), D1(1)], [D(2), D1(2)], [D(3), D1(3)], 'k-', 'LineWidth', 2);
    plot3([E(1), E1(1)], [E(2), E1(2)], [E(3), E1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([E(1), A(1)], [E(2), A(2)], [E(3), A(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), D(1)], [E(2), D(2)], [E(3), D(3)], 'k--', 'LineWidth', 1.5);
    plot3([E(1), E1(1)], [E(2), E1(2)], [E(3), E1(3)], 'k--', 'LineWidth', 1.5);
    
    
    text(A(1), A(2), A(3), point_A, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1), B(2), B(3), point_B, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1), D(2), D(3), point_D, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1), E(2), E(3), point_E, ...
        'VerticalAlignment', 'middle', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    
    text(A1(1), A1(2), A1(3), point_A1, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    text(B1(1), B1(2), B1(3), point_B1, ...
        'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(C1(1), C1(2), C1(3), point_C1, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'left', 'FontSize', 14, 'FontWeight', 'bold');
    text(D1(1), D1(2), D1(3), point_D1, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'right', 'FontSize', 14, 'FontWeight', 'bold');
    text(E1(1), E1(2), E1(3), point_E1, ...
        'VerticalAlignment', 'top', 'HorizontalAlignment', 'center', 'FontSize', 14, 'FontWeight', 'bold');

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
    