function visual(mode, azimuth, elevation, point_V, point_A, point_B, point_C, point_O, point_M, point_E, point_F, point_G, point_H)
    close all;
    fig = figure('Visible', 'off');

    a = 2; h_v = 3;
    O = [0, 0, 0]; V = [0, 0, h_v];
    r = a / sqrt(3);
    A = [r, 0, 0]; B = [r*cos(2*pi/3), r*sin(2*pi/3), 0]; C = [r*cos(4*pi/3), r*sin(4*pi/3), 0];
    D = (B+C)/2;
    
    m_ratio = 2/3; M = V * m_ratio;
    
    P_ratio = 0.55; E_ratio = 0.7; H_ratio = 0.45;
    P = A + P_ratio * (V - A);
    E = B + E_ratio * (V - B);
    F = C + E_ratio * (V - C);
    G = A + H_ratio * (D - A);
    H = A + H_ratio * (B - A);
    I = A + H_ratio * (C - A);

    hold on;
    
    fill3([P(1) E(1) F(1) I(1) H(1)], [P(2) E(2) F(2) I(2) H(2)], [P(3) E(3) F(3) I(3) H(3)], 'y', 'FaceAlpha', 0.2);

    plot3([V(1), A(1)], [V(2), A(2)], [V(3), A(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), B(1)], [V(2), B(2)], [V(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), C(1)], [V(2), C(2)], [V(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([A(1), C(1)], [A(2), C(2)], [A(3), C(3)], 'k-', 'LineWidth', 2);

    plot3([A(1), B(1)], [A(2), B(2)], [A(3), B(3)], 'k-', 'LineWidth', 2);
    plot3([B(1), C(1)], [B(2), C(2)], [B(3), C(3)], 'k-', 'LineWidth', 2);
    plot3([V(1), O(1)], [V(2), O(2)], [V(3), O(3)], 'k--', 'LineWidth', 2);
    plot3([A(1), D(1)], [A(2), D(2)], [A(3), D(3)], 'k--', 'LineWidth', 2);
    
    plot3([P(1),E(1)],[P(2),E(2)],[P(3),E(3)],'k-','LineWidth',1.5);
    plot3([P(1),H(1)],[P(2),H(2)],[P(3),H(3)],'k-','LineWidth',1.5);
    plot3([E(1),F(1)],[E(2),F(2)],[E(3),F(3)],'k-','LineWidth',1.5);
    plot3([F(1),I(1)],[F(2),I(2)],[F(3),I(3)],'k-','LineWidth',1.5);
    plot3([I(1),H(1)],[I(2),H(2)],[I(3),H(3)],'k-','LineWidth',1.5);
    
    all_points = {V, A, B, C, O, D, M, P, E, F, G, H, I};
    point_coords = cell2mat(all_points');
    scatter3(point_coords(:,1), point_coords(:,2), point_coords(:,3), 50, 'ko', 'filled');
    
    text(V(1), V(2), V(3)+0.1, point_V, 'FontSize', 14, 'FontWeight', 'bold');
    text(A(1)+0.1, A(2), A(3)-0.1, point_A, 'FontSize', 14, 'FontWeight', 'bold');
    text(B(1)-0.1, B(2)+0.1, B(3), point_B, 'FontSize', 14, 'FontWeight', 'bold');
    text(C(1)-0.1, C(2)-0.1, C(3), point_C, 'FontSize', 14, 'FontWeight', 'bold');
    text(O(1), O(2)-0.2, O(3), point_O, 'FontSize', 14, 'FontWeight', 'bold');
    
    text(M(1)+0.1, M(2)+0.1, M(3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    
    text(E(1), E(2)+0.1, E(3), point_E, 'FontSize', 14, 'FontWeight', 'bold');
    text(F(1), F(2)-0.1, F(3), point_F, 'FontSize', 14, 'FontWeight', 'bold');
    text(G(1)+0.1, G(2)-0.1, G(3), point_G, 'FontSize', 14, 'FontWeight', 'bold');
    text(H(1), H(2)+0.1, H(3), point_H, 'FontSize', 14, 'FontWeight', 'bold');
    
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
    