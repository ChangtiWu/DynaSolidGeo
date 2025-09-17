function visual(mode, azimuth, elevation, point_A, point_B, point_C, point_D, point_E, point_F, point_M, point_N)
    close all;
    fig = figure('Visible', 'off');
    hold on;

    a = 2;
    dihedral_angle = acos(-1/3);

    A_orig = [0, -a, 0];
    B_orig = [-a*sqrt(3)/2, -a/2, 0];
    C_orig = [-a*sqrt(3)/2, a/2, 0];
    D_orig = [0, a, 0];
    E_orig = [a*sqrt(3)/2, a/2, 0];
    F_orig = [a*sqrt(3)/2, -a/2, 0];
    
    theta_M = -dihedral_angle / 2;
    R_M = [cos(theta_M), 0, sin(theta_M); 0, 1, 0; -sin(theta_M), 0, cos(theta_M)];
    
    theta_N = dihedral_angle / 2;
    R_N = [cos(theta_N), 0, sin(theta_N); 0, 1, 0; -sin(theta_N), 0, cos(theta_N)];

    A = (R_N * A_orig')';
    D = (R_N * D_orig')';
    C = (R_N * C_orig')';
    B = (R_N * B_orig')';
    E = (R_M * E_orig')';
    F = (R_M * F_orig')';
    
    G = (A + D) / 2;
    H = (C + D) / 2;

    plane_extend = a * 1.5;
    plane_corner_N_orig = [-plane_extend, -a, 0];
    plane_corner_N2_orig = [-plane_extend, a, 0];
    plane_corner_M_orig = [plane_extend, -a, 0];
    plane_corner_M2_orig = [plane_extend, a, 0];
    
    plane_N_verts = [A; D; (R_N * plane_corner_N2_orig')'; (R_N * plane_corner_N_orig')'];
    plane_M_verts = [A; D; (R_M * plane_corner_M2_orig')'; (R_M * plane_corner_M_orig')'];

    patch(plane_M_verts(:,1), plane_M_verts(:,2), plane_M_verts(:,3), [0.8 0.9 1], 'FaceAlpha', 0.2, 'EdgeColor', 'k');
    patch(plane_N_verts(:,1), plane_N_verts(:,2), plane_N_verts(:,3), [0.8 1 0.9], 'FaceAlpha', 0.2, 'EdgeColor', 'k');
    
    plot3([A(1) B(1)], [A(2) B(2)], [A(3) B(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1) D(1)], [C(2) D(2)], [C(3) D(3)], 'k-', 'LineWidth', 1.5);
    plot3([E(1) F(1)], [E(2) F(2)], [E(3) F(3)], 'k-', 'LineWidth', 1.5);
    plot3([F(1) A(1)], [F(2) A(2)], [F(3) A(3)], 'k-', 'LineWidth', 1.5);
    plot3([D(1) E(1)], [D(2) E(2)], [D(3) E(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([B(1) C(1)], [B(2) C(2)], [B(3) C(3)], 'k-', 'LineWidth', 1.5);
    
    plot3([A(1) D(1)], [A(2) D(2)], [A(3) D(3)], 'k--', 'LineWidth', 1.0);

    plot3([F(1) C(1)], [F(2) C(2)], [F(3) C(3)], 'k-', 'LineWidth', 1.5);
    plot3([C(1) E(1)], [C(2) E(2)], [C(3) E(3)], 'k-', 'LineWidth', 1.5);

    plot3([C(1) G(1)], [C(2) G(2)], [C(3) G(3)], 'k--', 'LineWidth', 1.0);
    plot3([E(1) H(1)], [E(2) H(2)], [E(3) H(3)], 'k--', 'LineWidth', 1.0);
    plot3([F(1) H(1)], [F(2) H(2)], [F(3) H(3)], 'k--', 'LineWidth', 1.0);

    all_points = [A; B; C; D; E; F; H];
    labels = {point_A, point_B, point_C, point_D, point_E, point_F};
    scatter3(all_points(:,1), all_points(:,2), all_points(:,3), 30, 'k', 'filled');
    
    text_offset = 0.2;
    text(A(1), A(2) - text_offset, A(3), labels{1}, 'FontSize', 12, 'FontWeight', 'bold');
    text(B(1) - text_offset, B(2), B(3), labels{2}, 'FontSize', 12, 'FontWeight', 'bold');
    text(C(1) - text_offset, C(2), C(3), labels{3}, 'FontSize', 12, 'FontWeight', 'bold');
    text(D(1), D(2) + text_offset, D(3), labels{4}, 'FontSize', 12, 'FontWeight', 'bold');
    text(E(1) + text_offset, E(2), E(3), labels{5}, 'FontSize', 12, 'FontWeight', 'bold');
    text(F(1) + text_offset, F(2), F(3), labels{6}, 'FontSize', 12, 'FontWeight', 'bold');
    
    
    text(plane_M_verts(4,1) + 0.5, plane_M_verts(4,2), plane_M_verts(4,3), point_M, 'FontSize', 14, 'FontWeight', 'bold');
    text(plane_N_verts(4,1) - 0.5, plane_N_verts(4,2), plane_N_verts(4,3), point_N, 'FontSize', 14, 'FontWeight', 'bold');

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
    