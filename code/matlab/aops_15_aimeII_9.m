function visual(mode, azimuth, elevation, point_A)
    close all;
    fig = figure('Visible', 'off');
    r = 4;
    h_cyl = 10;
    [xc, yc, zc] = cylinder(r, 100);
    zc = zc * h_cyl;
    
    L = 8;
    v0 = [0 0 0;
          L 0 0;
          L L 0;
          0 L 0;
          0 0 L;
          L 0 L;
          L L L;
          0 L L];
    v0 = v0 - L/2;
    
    u = [1;1;1] / norm([1;1;1]);
    v = [0;0;1];
    axis_rot = cross(u, v);
    theta = acos(dot(u, v));
    
    K = [   0        -axis_rot(3)  axis_rot(2);
         axis_rot(3)     0       -axis_rot(1);
        -axis_rot(2)  axis_rot(1)     0      ];
    R = eye(3) + sin(theta)*K + (1-cos(theta))*(K^2);
    
    v_rot = (R * v0')';
    v_shifted = v_rot + [0 0 h_cyl - L/sqrt(3)/2];
    
    faces = [1 2 3 4;
             5 6 7 8;
             1 2 6 5;
             2 3 7 6;
             3 4 8 7;
             4 1 5 8];
    

    hold on
    
    surf(xc, yc, zc, 'FaceAlpha', 0, 'EdgeColor', 'k', 'LineWidth', 0.01);
    
    for i = 1:6
        fill3(v_shifted(faces(i,:),1), v_shifted(faces(i,:),2), v_shifted(faces(i,:),3)+6.5, ...
            [1 1 1], 'EdgeColor', 'k', 'FaceAlpha', 0.3, 'LineWidth', 2);
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
    