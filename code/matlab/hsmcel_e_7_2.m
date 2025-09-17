function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D)
    close all;
    fig = figure('Visible', 'off');

    x = 5; 
    y = 4;
    z = 3;

    P1 = [0, 0, 0];
    P2 = [x, 0, 0];
    P3 = [0, y, 0];
    P4 = [x, y, 0];
    P5 = [0, 0, z];
    P6 = [x, 0, z];
    P7 = [0, y, z];
    P8 = [x, y, z];
    
    prism_vertices = [P1; P2; P3; P4; P5; P6; P7; P8];
    prism_edges = [1, 2; 1, 3; 1, 5; 2, 4; 2, 6; 3, 4; 3, 7; 4, 8; 5, 6; 5, 7; 6, 8; 7, 8];

    A = P7;
    B = P4;
    C = P6;
    D = P1;

    tetra_vertices = [A; B; C; D];
    tetra_labels = {point_A, point_B, point_C, point_D};
    
    hold on;

    for i = 1:size(prism_edges, 1)
        v1_idx = prism_edges(i, 1);
        v2_idx = prism_edges(i, 2);
        plot3([prism_vertices(v1_idx, 1), prism_vertices(v2_idx, 1)], ...
              [prism_vertices(v1_idx, 2), prism_vertices(v2_idx, 2)], ...
              [prism_vertices(v1_idx, 3), prism_vertices(v2_idx, 3)], '--', 'Color', [0.7 0.7 0.7], 'LineWidth', 1);
    end

    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), D(1)], [B(2), D(2)], [B(3), D(3)], 'k-', 'LineWidth', 2);
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    
    scatter3(tetra_vertices(:,1), tetra_vertices(:,2), tetra_vertices(:,3), 50, 'k', 'filled');
    for i = 1:length(tetra_labels)
        text(tetra_vertices(i,1)+0.1, tetra_vertices(i,2)+0.1, tetra_vertices(i,3)+0.1, ...
             tetra_labels{i}, 'FontSize', 14, 'FontWeight', 'bold', 'HorizontalAlignment', 'center');
    end

    axis equal;
    axis off;
    view(azimuth, elevation);
    
    set(gcf, 'Color', 'white');
    
    
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
    