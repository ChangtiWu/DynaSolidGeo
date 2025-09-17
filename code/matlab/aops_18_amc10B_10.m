function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_G, point_H, point_M)
    close all;
    fig = figure('Visible', 'off');
    A = [0, 0, 0];
    B = [3, 0, 0];
    C = [3, 1, 0];
    D = [0, 1, 0];
    E = [0, 0, 2];
    F = [3, 0, 2];
    G = [3, 1, 2];
    H = [0, 1, 2];
    M = (F + G) / 2;
    
    points = [A; B; C; D; E; F; G; H; M];
    
    edges = [
        1 2; 2 3; 3 4; 4 1;
        5 6; 6 7; 7 8; 8 5;
        1 5; 2 6; 3 7; 4 8;
        7 9; 3 9; 6 9; 8 9; 5 9; 2 9;
        2 5; 3 8
    ];

    hold on
    for i = 1:size(edges, 1)
        pt1 = points(edges(i,1), :);
        pt2 = points(edges(i,2), :);
        plot3([pt1(1), pt2(1)], [pt1(2), pt2(2)], [pt1(3), pt2(3)], 'k-', 'LineWidth', 2)
    end
    
    labels = {point_A,point_B,point_C,point_D,point_E,point_F,point_G,point_H,point_M};
    for i = 1:length(labels)
        text(points(i,1), points(i,2), points(i,3), [' ', labels{i}], 'FontSize', 12, 'FontWeight', 'bold')
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
    