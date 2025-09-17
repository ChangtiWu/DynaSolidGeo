
function visual(mode, azimuth, elevation, point_P, point_A, point_O, point_B, point_A1)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    radius = 3;         
    height = 4;         
    
    
    O = [0, 0, 0];       
    O1 = [0, 0, height]; 
    
    
    
    A = [-radius, 0, 0]; 
    B = [radius, 0, 0];  
    
    
    A1 = [-radius, 0, height]; 
    B1 = [radius, 0, height];  
    
    
    P_angle = -pi/3; 
    P = [radius*cos(P_angle), radius*sin(P_angle), 0];


    hold on;
    
    
    theta = linspace(0, 2*pi, 100);
    bottom_x = radius * cos(theta);
    bottom_y = radius * sin(theta);
    bottom_z = zeros(size(theta));
    
    
    top_x = radius * cos(theta);
    top_y = radius * sin(theta);
    top_z = height * ones(size(theta));
    
    
    [X,Z] = meshgrid(linspace(-radius,radius,50), linspace(0,height,50));
    Y1 = sqrt(radius^2 - X.^2);
    Y2 = -sqrt(radius^2 - X.^2);
    surf(X,Y1,Z,'FaceAlpha',0.3,'EdgeColor','none','FaceColor',[0.8 0.8 0.8]);
    surf(X,Y2,Z,'FaceAlpha',0.3,'EdgeColor','none','FaceColor',[0.8 0.8 0.8]);
    
    
    plot3(bottom_x, bottom_y, bottom_z, 'k-', 'LineWidth', 2);
    
    
    plot3(top_x, top_y, top_z, 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'k-', 'LineWidth', 1.5);
    
    
    plot3([A(1), A1(1)], [A(2), A1(2)], [A(3), A1(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), B1(1)], [B(2), B1(2)], [B(3), B1(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([P(1), A1(1)], [P(2), A1(2)], [P(3), A1(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1), A1(1)], [B(2), A1(2)], [B(3), A1(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([P(1), O(1)], [P(2), O(2)], [P(3), O(3)], 'k--', 'LineWidth', 1);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k--', 'LineWidth', 1);
    
    
    text(A(1)-0.3, A(2)-0.2, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.2, B(2)-0.2, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(A1(1)-0.3, A1(2)-0.2, A1(3), point_A1, 'FontSize', 14, 'FontWeight', 'bold');

    text(P(1)+0.2, P(2)-0.3, P(3), point_P, 'FontSize', 14, 'FontWeight', 'bold');
    text(O(1), O(2)-0.3, O(3), point_O, 'FontSize', 14, 'FontWeight', 'bold');
    
    
    
    plot3(A(1), A(2), A(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(B(1), B(2), B(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(A1(1), A1(2), A1(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(B1(1), B1(2), B1(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(P(1), P(2), P(3), 'ko', 'MarkerSize', 8, 'MarkerFaceColor', 'black');
    plot3(O(1), O(2), O(3), 'ko', 'MarkerSize', 4, 'MarkerFaceColor', 'black');
    plot3(O1(1), O1(2), O1(3), 'ko', 'MarkerSize', 4, 'MarkerFaceColor', 'black');


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
    