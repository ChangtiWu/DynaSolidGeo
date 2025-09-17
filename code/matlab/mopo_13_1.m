function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_G)





    close all;
    fig = figure('Visible', 'off');

    
    r = 1.5;  
    h = 3;    
    
    
    B = [-r, 0, 0];     
    C = [r, 0, 0];      
    D = [r, 0, h];      
    A = [-r, 0, h];     
    
    
    
    
    theta = pi/3;  
    E = [-r*cos(theta), -r*sin(theta), 0];
    
    
    t_f = 1/2;
    F = [A(1) + t_f*(B(1)-A(1)), A(2) + t_f*(B(2)-A(2)), A(3) + t_f*(B(3)-A(3))];
    
    
    t_g = 1/4;
    G = [A(1) + t_g*(C(1)-A(1)), A(2) + t_g*(C(2)-A(2)), A(3) + t_g*(C(3)-A(3))];
    
    
    
    theta_circle = 0:pi/20:2*pi;
    x_top = r * cos(theta_circle);
    y_top = r * sin(theta_circle);
    z_top = h * ones(size(theta_circle));
    plot3(x_top, y_top, z_top, 'k-', 'LineWidth', 2);
    
    
    z_bottom = zeros(size(theta_circle));


    hold on;

    plot3(x_top, y_top, z_bottom, 'k-', 'LineWidth', 2);
    
    
    plot3([r, r], [0, 0], [0, h], 'k-', 'LineWidth', 2);
    plot3([-r, -r], [0, 0], [0, h], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k--', 'LineWidth', 2);
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([B(1), E(1)], [B(2), E(2)], [B(3), E(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([C(1), E(1)], [C(2), E(2)], [C(3), E(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([A(1), F(1)], [A(2), F(2)], [A(3), F(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([A(1), G(1)], [A(2), G(2)], [A(3), G(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([F(1), G(1)], [F(2), G(2)], [F(3), G(3)], 'k--', 'LineWidth', 1.5);
    plot3([F(1), E(1)], [F(2), E(2)], [F(3), E(3)], 'k--', 'LineWidth', 1.5);
    
    
    theta_hidden = pi:pi/20:2*pi;
    x_hidden = r * cos(theta_hidden);
    y_hidden = r * sin(theta_hidden);
    z_hidden_top = h * ones(size(theta_hidden));
    z_hidden_bottom = zeros(size(theta_hidden));
    plot3(x_hidden, y_hidden, z_hidden_top, 'k-', 'LineWidth', 1.5);
    plot3(x_hidden, y_hidden, z_hidden_bottom, 'k-', 'LineWidth', 1.5);
    
    
    text(A(1), A(2), A(3), point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1), B(2), B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1), C(2), C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(D(1), D(2), D(3), point_D, 'FontSize', 14, 'FontWeight', 'bold');
    text(E(1), E(2), E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1), F(2), F(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(G(1), G(2), G(3), point_G, 'FontSize', 14, 'FontWeight', 'bold');
    
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
    