function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    R = 2;          
    H = 3;          
    S = [0, 0, H];  
    O = [0, 0, 0];  
    O1 = [0, 0, H/2]; 
    r = R / 2;      
    m1=[-r,0,H/2];
    m2=[-r,0,0];
    n1=[r,0,H/2];
    n2=[r,0,0];
    
    

    hold on;

    
    
    
    theta = linspace(0, 2*pi, 100);
    
    
    x_bottom_fill = [0; R * cos(theta')];
    y_bottom_fill = [0; R * sin(theta')];
    z_bottom_fill = zeros(size(x_bottom_fill));
    fill3(x_bottom_fill, y_bottom_fill, z_bottom_fill, [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    [THETA, Z] = meshgrid(theta, linspace(0, H, 50));
    R_surf = R * (H - Z) / H;  
    X = R_surf .* cos(THETA);
    Y = R_surf .* sin(THETA);
    surf(X, Y, Z, 'FaceColor', [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    x_section_fill = [0; r * cos(theta')];
    y_section_fill = [0; r * sin(theta')];
    z_section_fill = (H/2) * ones(size(x_section_fill));
    fill3(x_section_fill, y_section_fill, z_section_fill, [0.7, 0.8, 0.9], 'FaceAlpha', 0.4, 'EdgeColor', 'none');
    
    
    
    A = [-R, 0, 0];
    plot3([S(1), A(1)], [S(2), A(2)], [S(3), A(3)], 'k-', 'LineWidth', 2);
    
    
    B = [R, 0, 0];
    plot3([S(1), B(1)], [S(2), B(2)], [S(3), B(3)], 'k-', 'LineWidth', 2);
    
    
    theta_vis = linspace(-pi, pi, 50);  
    x_vis = r * cos(theta_vis) + O1(1);
    y_vis = r * sin(theta_vis) + O1(2);
    z_vis = ones(size(theta_vis)) * H/2;
    plot3(x_vis, y_vis, z_vis, 'k--', 'LineWidth', 1.5);
    theta_vis = linspace(-pi, pi, 50);  
    x_vis1 = r * cos(theta_vis) + O(1);
    y_vis1 = r * sin(theta_vis) + O(2);
    z_vis1 = 0.*theta_vis;
    plot3(x_vis1, y_vis1, z_vis1, 'k--', 'LineWidth', 1.5);
    
    
    x_base_vis = R * cos(theta_vis) + O(1);
    y_base_vis = R * sin(theta_vis) + O(2);
    z_base_vis = zeros(size(theta_vis));
    plot3(x_base_vis, y_base_vis, z_base_vis, 'k-', 'LineWidth', 2);
    
    
    plot3([B(1), r, B(1)], [B(2), 0, B(2)], [B(3), H/2, B(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A(1), -r, A(1)], [A(2), 0, A(2)], [A(3), H/2, A(3)], 'k-', 'LineWidth', 2);
    
    
    
    plot3([S(1), O(1)], [S(2), O(2)], [S(3), O(3)], 'k--', 'LineWidth', 1.5);
    plot3([m1(1), m2(1)], [m1(2), m2(2)], [m1(3), m2(3)], 'k--', 'LineWidth', 1.5);
    plot3([n1(1), n2(1)], [n1(2), n2(2)], [n1(3), n2(3)], 'k--', 'LineWidth', 1.5);
    
    theta_hid = linspace(pi/2, 3*pi/2, 50);  
    x_hid = r * cos(theta_hid) + O1(1);
    y_hid = r * sin(theta_hid) + O1(2);
    z_hid = ones(size(theta_hid)) * H/2;
    plot3(x_hid, y_hid, z_hid, 'k--', 'LineWidth', 1.5);
    
    
    x_base_hid = R * cos(theta_hid) + O(1);
    y_base_hid = R * sin(theta_hid) + O(2);
    z_base_hid = zeros(size(theta_hid));
    plot3(x_base_hid, y_base_hid, z_base_hid, 'k--', 'LineWidth', 1.5);
    
    
    plot3([S(1), x_hid(1)], [S(2), y_hid(1)], [S(3), z_hid(1)], 'k--', 'LineWidth', 1.5);
    plot3([S(1), x_hid(end)], [S(2), y_hid(end)], [S(3), z_hid(end)], 'k--', 'LineWidth', 1.5);
    
    
    text(S(1), S(2), S(3) + 0.1, 'S', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    
    
    text(A(1) - 0.1, A(2), A(3), 'A', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');
    text(B(1) + 0.1, B(2), B(3), 'B', 'FontSize', 14, 'Color', 'black', 'FontWeight', 'bold');


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
    