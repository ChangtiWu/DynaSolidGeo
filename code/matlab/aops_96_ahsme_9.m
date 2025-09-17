function visual(mode, azimuth, elevation, point_A, point_B, point_P, point_C, point_D)
    close all;
    fig = figure('Visible', 'off');
    A = [5, 0, 0];
    B = [0, 0, 0];
    P = [2, 4, 0];
    
    C = B + [0, 0, 5];
    D = A + [0, 0, 5];

    hold on;
    axis equal;
    
    square_pts = [A; B; C; D; A];
    plot3(square_pts(:,1), square_pts(:,2), square_pts(:,3), 'k-', 'LineWidth', 2);
    
    plot3([P(1), A(1)], [P(2), A(2)], [P(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([P(1), B(1)], [P(2), B(2)], [P(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    
    % fill3([P(1), A(1), B(1)], [P(2), A(2), B(2)], [P(3), A(3), B(3)], ...
    %       [0.8 0.8 1], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    % 
    % fill3([A(1), B(1), C(1), D(1)], [A(2), B(2), C(2), D(2)], ...
    %       [A(3), B(3), C(3), D(3)], [1 0.9 0.9], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    labels = {point_P,point_A,point_B,point_C,point_D};
    points = {P, A, B, C, D};
    for i = 1:length(labels)
        pt = points{i};
        text(pt(1)+0.2, pt(2)+0.2, pt(3)+0.2, labels{i}, 'FontSize', 12, 'FontWeight', 'bold');
    end
    view(3);
    grid on;


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
    