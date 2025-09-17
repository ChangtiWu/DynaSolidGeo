function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    

    hold on;

    
    
    function drawCube(x, y, z, color)
        
        vertices = [
            x, y, z;     
            x+1, y, z;   
            x+1, y+1, z; 
            x, y+1, z;   
            x, y, z+1;   
            x+1, y, z+1; 
            x+1, y+1, z+1;
            x, y+1, z+1; 
        ];
        
        faces = [
            1 2 3 4; 
            5 6 7 8; 
            1 2 6 5; 
            2 3 7 6; 
            3 4 8 7; 
            4 1 5 8; 
        ];
        
        for faceIdx = 1:size(faces, 1)
            patch(...
                'Vertices', vertices, ...
                'Faces', faces(faceIdx, :), ...
                'FaceColor', color, ...
                'FaceAlpha', 0.7, ... 
                'EdgeColor', 'black', ... 
                'LineWidth', 1 ... 
            );
        end
    end
    
    
    
    drawCube(0, 1, 0, [1, 0.8, 0.6]);
    drawCube(0, 3, 0, [1, 0.8, 0.6]);
    drawCube(0, 4, 0, [1, 0.8, 0.6]);
    drawCube(1, 0, 0, [1, 0.8, 0.6]);
    drawCube(1, 1, 0, [1, 0.8, 0.6]);
    drawCube(1, 3, 0, [1, 0.8, 0.6]);
    drawCube(1, 4, 0, [1, 0.8, 0.6]);
    drawCube(2, 0, 0, [1, 0.8, 0.6]);
    drawCube(2, 1, 0, [1, 0.8, 0.6]);
    drawCube(3, 1, 0, [1, 0.8, 0.6]);
    drawCube(3, 3, 0, [1, 0.8, 0.6]);
    drawCube(3, 4, 0, [1, 0.8, 0.6]);
    drawCube(4, 3, 0, [1, 0.8, 0.6]);
    
    drawCube(0, 1, 1, [0.85, 0.85, 0.85]);
    drawCube(0, 1, 2, [0.85, 0.85, 0.85]);
    drawCube(0, 3, 1, [0.85, 0.85, 0.85]);
    drawCube(1, 0, 1, [0.85, 0.85, 0.85]);
    drawCube(1, 3, 1, [0.85, 0.85, 0.85]);
    drawCube(1, 4, 1, [0.85, 0.85, 0.85]);
    drawCube(2, 0, 1, [0.85, 0.85, 0.85]);
    drawCube(3, 4, 1, [0.85, 0.85, 0.85]);
    drawCube(4, 3, 1, [0.85, 0.85, 0.85]);
    drawCube(4, 3, 2, [0.85, 0.85, 0.85]);

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
    