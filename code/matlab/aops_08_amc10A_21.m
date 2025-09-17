function visual(mode, azimuth, elevation, point_A, point_C, point_B, point_D)
    close all;
    fig = figure('Visible', 'off');
    L = 2;
    
    A = [0, 0, 0];
    B = [L, 0, 0];
    C = [L, L, 0];
    D = [0, L, 0];
    E = [0, 0, L];
    F = [L, 0, L];
    G = [L, L, L];
    H = [0, L, L];
    BB = (H-D) / 3*2+D;
    DD = (B + F) / 2;
    
    points = [A; B; C; D; E; F; G; H; BB;DD];
    
    edges = [
        1 2; 2 3; 3 4; 4 1;      % 底面 ABCD
        5 6; 6 7; 7 8; 8 5;      % 顶面 EFGH
        1 5; 2 6; 3 7; 4 8;      % 竖边

    ];
    
    hold on
    for i = 1:size(edges, 1)
        pt1 = points(edges(i,1), :);
        pt2 = points(edges(i,2), :);
        plot3([pt1(1), pt2(1)], [pt1(2), pt2(2)], [pt1(3), pt2(3)], 'k-', 'LineWidth', 2)
    end
    
    labels = {point_A,' ',' ',' ',' ',' ',point_C,' ',point_B,point_D};
    for i = 1:length(labels)
        text(points(i,1)+0.04, points(i,2)+0.04, points(i,3)+0.04, [' ', labels{i}], 'FontSize', 14, 'FontWeight', 'bold')
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
    