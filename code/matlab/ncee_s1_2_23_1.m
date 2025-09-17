function visual(mode, azimuth, elevation)
    close all;
    fig = figure('Visible', 'off');

    a = 2; 
    s = a / 2;

    V = {[s,s,s], [-s,s,s], [-s,-s,s], [s,-s,s], [s,s,-s], [-s,s,-s], [-s,-s,-s], [s,-s,-s]};
    
    F = {
        [s,0,0], [-s,0,0], [0,s,0], [0,-s,0], [0,0,s], [0,0,-s]
    };
    
    hold on;

    edges = [1,2; 2,3; 3,4; 4,1; 5,6; 6,7; 7,8; 8,5; 1,5; 2,6; 3,7; 4,8];
    for i = 1:size(edges, 1)
        p1 = V{edges(i,1)};
        p2 = V{edges(i,2)};
        if p1(1) < 0 && p2(1) < 0 && p1(2) < 0 && p2(2) < 0
            plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], 'k-', 'LineWidth', 2);
        elseif i==7 || i==6 || i==10
            plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], 'k-', 'LineWidth', 2);
        else
            plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], 'k-', 'LineWidth', 2);
        end
    end

    % Connect face centers
    for i = 1:length(F)
        for j = (i+1):length(F)
            p1 = F{i};
            p2 = F{j};
            plot3([p1(1), p2(1)], [p1(2), p2(2)], [p1(3), p2(3)], 'k--', 'LineWidth', 1.5);
        end
    end

    for i = 1:length(F)
        pt = F{i};
        scatter3(pt(1), pt(2), pt(3), 25, 'ko', 'filled');
    end

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

        camzoom(0.8);

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
    