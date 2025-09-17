function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_O1, point_O2, point_E, point_F, point_G, point_H)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    R1 = 2;          
    R2 = 4;          
    h = 5;           
    O1 = [0, 0, h];  
    O2 = [0, 0, 0];  
    
    
    A = [-R2, 0, 0];
    B = [R2, 0, 0];
    C = [R1, 0, h];
    D = [-R1, 0, h];
    
    
    theta_E = pi/3;  
    E = [R1*cos(theta_E), R1*sin(theta_E), h];
    
    
    theta_F = theta_E;
    F = [R2*cos(theta_F), R2*sin(theta_F), 0];
    
    
    G = (O2 + B)/2;
    H = (B + F)/2;
    
    
    hold on;
    
    
    theta = linspace(0, 2*pi, 50);
    z = linspace(0, h, 20);
    [THETA, Z] = meshgrid(theta, z);
    R = R2 - (R2-R1)*Z/h;  
    X = R .* cos(THETA);
    Y = R .* sin(THETA);
    surf(X, Y, Z, 'FaceColor', [0.8 0.8 0.8], 'FaceAlpha', 0.3, 'EdgeColor', 'none');
    
    
    
    plot3([E(1), F(1)], [E(2), F(2)], [E(3), F(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k--', 'LineWidth', 1.5);  
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);  
    plot3([C(1), D(1)], [C(2), D(2)], [C(3), D(3)], 'k-', 'LineWidth', 2);  
    plot3([D(1), A(1)], [D(2), A(2)], [D(3), A(3)], 'k-', 'LineWidth', 2);  
    
    
    theta_top_vis = linspace(-pi, 0, 50);
    x_top_vis = R1*cos(theta_top_vis);
    y_top_vis = R1*sin(theta_top_vis);
    z_top_vis = h*ones(size(theta_top_vis));
    plot3(x_top_vis, y_top_vis, z_top_vis, 'k-', 'LineWidth', 2);
    
    
    theta_bot_vis = linspace(-pi, 0, 50);
    x_bot_vis = R2*cos(theta_bot_vis);
    y_bot_vis = R2*sin(theta_bot_vis);
    z_bot_vis = zeros(size(theta_bot_vis));
    plot3(x_bot_vis, y_bot_vis, z_bot_vis, 'k--', 'LineWidth', 1.5);
    
    
    plot3([C(1), G(1)], [C(2), G(2)], [C(3), G(3)], 'k--', 'LineWidth', 1.5);
    plot3([G(1), H(1)], [G(2), H(2)], [G(3), H(3)], 'k--', 'LineWidth', 1.5);
    
    plot3([H(1), C(1)], [H(2), C(2)], [H(3), C(3)], 'k--', 'LineWidth', 1.5);
    plot3([A(1), F(1)], [A(2), F(2)], [A(3), F(3)], 'k--', 'LineWidth', 1.5);
    plot3([O2(1), F(1)], [O2(2), F(2)], [O2(3), F(3)], 'k--', 'LineWidth', 1.5);
    
    
    theta_top_hid = linspace(0, pi, 50);
    x_top_hid = R1*cos(theta_top_hid);
    y_top_hid = R1*sin(theta_top_hid);
    z_top_hid = h*ones(size(theta_top_hid));
    plot3(x_top_hid, y_top_hid, z_top_hid, 'k-', 'LineWidth', 2);
    
    
    theta_bot_hid = linspace(0, pi, 50);
    x_bot_hid = R2*cos(theta_bot_hid);
    y_bot_hid = R2*sin(theta_bot_hid);
    z_bot_hid = zeros(size(theta_bot_hid));
    plot3(x_bot_hid, y_bot_hid, z_bot_hid, 'k-', 'LineWidth', 2);
    
    
    plot3([O1(1), O2(1)], [O1(2), O2(2)], [O1(3), O2(3)], 'k--', 'LineWidth', 1.5);
    
    
    plot3([O2(1), B(1)], [O2(2), B(2)], [O2(3), B(3)], 'k--', 'LineWidth', 1.5);
    plot3([B(1), F(1)], [B(2), F(2)], [B(3), F(3)], 'k--', 'LineWidth', 1.5);
    
    
    text(A(1), A(2), A(3)-0.5, point_A, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(B(1), B(2), B(3)-0.5, point_B, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(C(1), C(2), C(3)+0.5, point_C, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(D(1), D(2), D(3)+0.5, point_D, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(E(1), E(2), E(3)+0.5, point_E, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(F(1), F(2), F(3)-0.5, point_F, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(O1(1), O1(2), O1(3)+0.3, point_O1, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(O2(1), O2(2), O2(3)-0.5, point_O2, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(G(1), G(2), G(3)-0.5, point_G, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');
    text(H(1), H(2), H(3)-0.5, point_H, 'FontSize', 14, 'Color', 'black','FontWeight', 'bold');


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
    