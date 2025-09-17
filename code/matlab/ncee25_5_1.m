
function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_R, point_T, point_S)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    side_length = 2;    
    
    
    F = [0, 0, 0];
    A = [2, 0, 0];
    B = [side_length, side_length, 0];
    E = [0, side_length, 0];
    
    
    height = side_length;  
    R = [side_length/2, 0, height];      
    S = [1, 4, height];  
    
    
    C = [5, 4, 0];    
    D = [0, 4, 0];    
    G = [0, 2, 0];    
    J = [5, 2, 0];    
    
    
    U = [5, 4, 2];    
    V = [0, 3, 2];    


    hold on;

    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([F(1), A(1)], [F(2), A(2)], [F(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([R(1), S(1)], [R(2), S(2)], [R(3), S(3)], 'k-', 'LineWidth', 2);
    
    
    
    plot3([A(1), R(1)], [A(2), R(2)], [A(3), R(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([B(1), S(1)], [B(2), S(2)], [B(3), S(3)], 'k-', 'LineWidth', 2);
    
    
    
    plot3([R(1), F(1)], [R(2), F(2)], [R(3), F(3)], 'k-', 'LineWidth', 2);
    
    
    text(A(1)+0.1, A(2)-0.3, A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)+0.1, B(2)+0.1, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    
    text(F(1)-0.3, F(2)-0.3, F(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    
    
    text(R(1), R(2)-0.3, R(3)+0.2, point_R, 'FontSize', 14, 'FontWeight', 'bold');
    text(S(1), S(2)+0.1, S(3)+0.2, point_S, 'FontSize', 14, 'FontWeight', 'bold');
    
    
    plot3(A(1), A(2), A(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(B(1), B(2), B(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    
    plot3(F(1), F(2), F(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(R(1), R(2), R(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(S(1), S(2), S(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    
    
    
    
    
    
    
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), F(1)], [D(2), F(2)], [D(3), F(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), J(1)], [B(2), J(2)], [B(3), J(3)], 'k-', 'LineWidth', 2);
    plot3([J(1), C(1)], [J(2), C(2)], [J(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), D(1)], [S(2), D(2)], [S(3), D(3)], 'k-', 'LineWidth', 2);
    
    
    
    
    plot3([C(1), U(1)], [C(2), U(2)], [C(3), U(3)], 'k-', 'LineWidth', 2);
    plot3([S(1), U(1)], [S(2), U(2)], [S(3), U(3)], 'k-', 'LineWidth', 2);
    plot3([J(1), U(1)], [J(2), U(2)], [J(3), U(3)], 'k-', 'LineWidth', 2);
    
    
    text(C(1)+0.1, C(2)+0.1, C(3), point_D, 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'black');
    text(D(1)-0.3, D(2)+0.1, D(3), point_E, 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'black');
    
    text(J(1)+0.1, J(2)-0.3, J(3), point_C, 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'black');
    text(U(1)+0.1, U(2)+0.1, U(3)+0.2, point_T, 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'black');
    
    
    
    plot3(C(1), C(2), C(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(D(1), D(2), D(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    
    plot3(J(1), J(2), J(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');
    plot3(U(1), U(2), U(3), 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'black');


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

        camzoom(0.9);

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
    