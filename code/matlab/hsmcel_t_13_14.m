function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    

    faces = [1 2 3 4;    
             5 6 7 8;    
             1 2 6 5;    
             2 3 7 6;    
             3 4 8 7;    
             4 1 5 8];   
    
    
    hold on;
    
    
    faceColor = [1 1 1];  
    edgeColor = 'k';      
    faceAlpha = 0.8;      
    
    
    vertices1 = [1  1  0;
                 -1 1  0;
                 -1 -1 0;
                 1  -1 0;
                 1  1  2;
                 -1 1  2;
                 -1 -1 2;
                 1  -1 2];
    
    
    patch('Vertices',vertices1,'Faces',faces,'FaceColor',faceColor,...
          'EdgeColor',edgeColor,'FaceAlpha',faceAlpha);
    
    
    vertices2 = [0  1  2;
                 -1 0  2;
                 0  -1 2;
                 1  0  2;
                 0  1  3;
                 -1 0  3;
                 0  -1 3;
                 1  0  3];
    
    
    patch('Vertices',vertices2,'Faces',faces,'FaceColor',faceColor,...
          'EdgeColor',edgeColor,'FaceAlpha',faceAlpha);
    
    
    vertices3 = [0.5 0.5 3;
                 -0.5 0.5 3;
                 -0.5 -0.5 3;
                 0.5 -0.5 3;
                 0.5 0.5 4;
                 -0.5 0.5 4;
                 -0.5 -0.5 4;
                 0.5 -0.5 4];
    
    
    patch('Vertices',vertices3,'Faces',faces,'FaceColor',faceColor,...
          'EdgeColor',edgeColor,'FaceAlpha',faceAlpha);
    
    
    vertices4 = [0  0.5 4;
                 -0.5 0  4;
                 0  -0.5 4;
                 0.5 0  4;
                 0  0.5 5;
                 -0.5 0  5;
                 0  -0.5 5;
                 0.5 0  5];
    
    
    patch('Vertices',vertices4,'Faces',faces,'FaceColor',faceColor,...
          'EdgeColor',edgeColor,'FaceAlpha',faceAlpha);




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

        camzoom(0.5);

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
    