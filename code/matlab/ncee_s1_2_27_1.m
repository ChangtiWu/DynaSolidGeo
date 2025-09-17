function visual(mode, azimuth, elevation, point_O, point_A, point_B, point_C, point_D, point_E, point_F, point_S)
    close all;
    fig = figure('Visible', 'off');

    R_circ = 5;
    r_tri = 2.5;

    O = [0, 0, 0];

    A = [r_tri*cosd(60), r_tri*sind(60), 0];
    B = [r_tri*cosd(180), r_tri*sind(180), 0];
    C = [r_tri*cosd(300), r_tri*sind(300), 0];
    
    E = [R_circ*cosd(0), R_circ*sind(0), 0];
    F = [R_circ*cosd(120), R_circ*sind(120), 0];
    D = [R_circ*cosd(240), R_circ*sind(240), 0];

    hold on;
    
    theta = linspace(0, 2*pi, 200);
    x_circ = R_circ * cos(theta);
    y_circ = R_circ * sin(theta);
    plot(x_circ, y_circ, 'k-', 'LineWidth', 1.5);

    patch([A(1) B(1) C(1)], [A(2) B(2) C(2)], [0.9 0.9 0.9]);
    plot([A(1) B(1)], [A(2) B(2)], 'k-', 'LineWidth', 1.5);
    plot([B(1) C(1)], [B(2) C(2)], 'k-', 'LineWidth', 1.5);
    plot([C(1) A(1)], [C(2) A(2)], 'k-', 'LineWidth', 1.5);

    plot([A(1) F(1)], [A(2) F(2)], 'k--', 'LineWidth', 1);
    plot([B(1) F(1)], [B(2) F(2)], 'k--', 'LineWidth', 1);
    plot([B(1) D(1)], [B(2) D(2)], 'k--', 'LineWidth', 1);
    plot([C(1) D(1)], [C(2) D(2)], 'k--', 'LineWidth', 1);
    plot([C(1) E(1)], [C(2) E(2)], 'k--', 'LineWidth', 1);
    plot([A(1) E(1)], [A(2) E(2)], 'k--', 'LineWidth', 1);

    all_points = {A, B, C, D, E, F, O};
    labels = {point_A, point_B, point_C, point_D, point_E, point_F, point_O};
    
    for i = 1:length(all_points)
        pt = all_points{i};
        scatter(pt(1), pt(2), 30, 'k', 'filled');
        text_offset = 0.25;
        text(pt(1), pt(2) + text_offset, labels{i}, 'FontSize', 14, 'FontWeight', 'bold', 'HorizontalAlignment', 'center');
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
    