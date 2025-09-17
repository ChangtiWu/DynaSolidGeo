function visual(mode, azimuth, elevation, point_A)
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
    J1 = (A + B) / 3*2;
    J12 = (C-B) / 3+B;
    J13 = (F-B) / 3+B;

    I1 = (F-B) / 3*2+B;
    I12 = (C-B) / 3+B+E;
    I13 = (A + B) / 3*2+E;



    I21 = (D - A) / 3*2;
    I22 = (H - D) / 3+D;
    I23 = (C- D) / 3+D;


    J21 = (A + B) / 3+H;
    J22 = (H-D)/3*2+D;
    J23 = I21+E;
    
    J31 = (G-C) / 3+C;
    J32 = (A + B) / 3*2+D;
    J33 = (C-B) / 3*2+B;

    I31 = (E - A) / 3*2;
    I32 = (C-B) / 3+E;
    I33 = (A + B) / 3+H-D;

    J41 = (F-B) / 3*2+B+D;
    J42 = (A + B) / 3*2+D+E;
    J43 = (C-B) / 3*2+B+E;

    A1=E/3;
    A2=B/3;
    A3=D/3;
    
    points = [A; B; C; D; E; F; G; H; J1;J12;J13; I1; I12; I13;J21;J22;J23;I21;I22;I23;J31;J32;J33;I31;I32;I33;J41;J42;J43;A1;A2;A3];
    
    edges = [
        1 2; 2 3; 3 4; 4 1;      % 底面 ABCD
        5 6; 6 7; 7 8; 8 5;      % 顶面 EFGH
        1 5; 2 6; 3 7; 4 8;      % 竖边
    ];
    edges1 = [
        9 10; 9 11;11 10;
        12 13; 12 14; 13 14;
        15 16; 15 17 ;16 17;
        18 19; 18 20; 19 20;
        21 22; 21 23; 22 23;
        24 25 ;25 26 ;24 26;
        27 28; 27 29; 28 29;
        30 31; 30 32; 31 32 
    ];

    hold on
    for i = 1:size(edges, 1)
        pt1 = points(edges(i,1), :);
        pt2 = points(edges(i,2), :);
        plot3([pt1(1), pt2(1)], [pt1(2), pt2(2)], [pt1(3), pt2(3)], 'k-', 'LineWidth', 2)
    end
    for i = 1:size(edges1, 1)
        pt1 = points(edges1(i,1), :);
        pt2 = points(edges1(i,2), :);
        plot3([pt1(1), pt2(1)], [pt1(2), pt2(2)], [pt1(3), pt2(3)], 'k--', 'LineWidth', 1.5)
    end
    
    % labels = {point_A,point_B,point_C,point_D,point_E,point_F,point_G,point_H,'J11','J12','J13','I11','I12','I13','J21','J22','J23','I21','I22','I23','J31','J32','J33','I31','I32','I33','J41','J42','J43','A1','A2','A3'};
    % for i = 1:length(labels)
    %     text(points(i,1), points(i,2), points(i,3), [' ', labels{i}], 'FontSize', 12)
    % end
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

    end
    hold off;
    close(fig);
end    