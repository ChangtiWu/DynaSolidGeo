function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_U, point_Z, point_X, point_Y, point_V, point_W)
    close all;
    fig = figure('Visible', 'off');
    L = 1;
    
    A = [0, sqrt(3)/3];
    B = [0.5, -sqrt(3)/6];
    C = [-0.5, -sqrt(3)/6];
    
    V = A + 1/3 * (C - A);
    U = A + 1/3 * (B - A);
    
    W = C + 1/3 * (A - C);
    Z = B - 1/3 * (B - A);
    
    X = (B - C)/3 + C;
    Y = (B - C)/3*2 + C;
    
    hold on;
    plot([A(1), B(1)], [A(2), B(2)], 'k', 'LineWidth', 2);
    plot([B(1), C(1)], [B(2), C(2)], 'k', 'LineWidth', 2);
    plot([C(1), A(1)], [C(2), A(2)], 'k', 'LineWidth', 2);
    
    plot([V(1), U(1)], [V(2), U(2)], 'k--', 'LineWidth', 1.5);
    plot([W(1), X(1)], [W(2), X(2)], 'k--', 'LineWidth', 1.5);
    plot([Z(1), Y(1)], [Z(2), Y(2)], 'k--', 'LineWidth', 1.5);
    
    points = struct(point_A, A, point_B, B, point_C, C, ...
                    point_V, V, point_U, U, ...
                    point_W, W, point_Z, Z, ...
                    point_X, X, point_Y, Y);
    fields = fieldnames(points);
    for i = 1:length(fields)
        name = fields{i};
        pt = points.(name);
        plot(pt(1), pt(2), 'ko', 'MarkerFaceColor', 'k');
        text(pt(1)+0.02, pt(2)+0.02, name, 'FontSize', 12, 'FontWeight', 'bold');
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
    