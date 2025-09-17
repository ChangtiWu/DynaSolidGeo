function visual(mode, azimuth, elevation)
    
    
    
    close all;
    fig = figure('Visible', 'off');


    
    
    
    cutDistance = 0.3;  
    
    
    xA = 0;    yA = 0;     zA = 0;   
    xB = 2;    yB = 0;     zB = 0;   
    xC = 2;    yC = 2;     zC = 0;   
    xD = 0;    yD = 2;     zD = 0;   
    xA1 = 0;   yA1 = 0;    zA1 = 2;  
    xB1 = 2;   yB1 = 0;    zB1 = 2;  
    xC1 = 2;   yC1 = 2;    zC1 = 2;  
    xD1 = 0;   yD1 = 2;    zD1 = 2;  
    
    
    
    
    
    
    A_B = [xA + cutDistance, yA, zA];       
    A_D = [xA, yA + cutDistance, zA];       
    A_A1 = [xA, yA, zA + cutDistance];      
    
    
    B_A = [xB - cutDistance, yB, zB];       
    B_C = [xB, yB + cutDistance, zB];       
    B_B1 = [xB, yB, zB + cutDistance];      
    
    
    C_B = [xC - cutDistance, yC, zC];       
    C_D = [xC, yC - cutDistance, zC];       
    C_C1 = [xC, yC, zC + cutDistance];      
    
    
    D_A = [xD + cutDistance, yD, zD];       
    D_C = [xD, yD - cutDistance, zD];       
    D_D1 = [xD, yD, zD + cutDistance];      
    
    
    A1_A = [xA1, yA1, zA1 - cutDistance];   
    A1_B1 = [xA1 + cutDistance, yA1, zA1];  
    A1_D1 = [xA1, yA1 + cutDistance, zA1];  
    
    
    B1_B = [xB1, yB1, zB1 - cutDistance];   
    B1_A1 = [xB1 - cutDistance, yB1, zB1];  
    B1_C1 = [xB1, yB1 + cutDistance, zB1];  
    
    
    C1_C = [xC1, yC1, zC1 - cutDistance];   
    C1_B1 = [xC1 - cutDistance, yC1, zC1];  
    C1_D1 = [xC1, yC1 - cutDistance, zC1];  
    
    
    D1_D = [xD1, yD1, zD1 - cutDistance];   
    D1_A1 = [xD1 + cutDistance, yD1, zD1];  
    D1_C1 = [xD1, yD1 - cutDistance, zD1];  
    
    

    hold on;
    
    
    
    
    plot3([A_B(1), B_A(1)], [A_B(2), B_A(2)], [A_B(3), B_A(3)], 'k-', 'LineWidth', 2);  
    plot3([B_C(1), C_D(1)], [B_C(2), C_D(2)], [B_C(3), C_D(3)], 'k-', 'LineWidth', 2);  
    plot3([C_B(1), D_A(1)], [C_B(2), D_A(2)], [C_B(3), D_A(3)], 'k-', 'LineWidth', 2);  
    plot3([D_C(1), A_D(1)], [D_C(2), A_D(2)], [D_C(3), A_D(3)], 'k-', 'LineWidth', 2);  
    
    
    plot3([A1_B1(1), B1_A1(1)], [A1_B1(2), B1_A1(2)], [A1_B1(3), B1_A1(3)], 'k-', 'LineWidth', 2);  
    plot3([B1_C1(1), C1_D1(1)], [B1_C1(2), C1_D1(2)], [B1_C1(3), C1_D1(3)], 'k-', 'LineWidth', 2);  
    plot3([C1_B1(1), D1_A1(1)], [C1_B1(2), D1_A1(2)], [C1_B1(3), D1_A1(3)], 'k-', 'LineWidth', 2);  
    plot3([D1_C1(1), A1_D1(1)], [D1_C1(2), A1_D1(2)], [D1_C1(3), A1_D1(3)], 'k-', 'LineWidth', 2);  
    
    
    plot3([B_B1(1), B1_B(1)], [B_B1(2), B1_B(2)], [B_B1(3), B1_B(3)], 'k-', 'LineWidth', 2);  
    plot3([C_C1(1), C1_C(1)], [C_C1(2), C1_C(2)], [C_C1(3), C1_C(3)], 'k-', 'LineWidth', 2);  
    plot3([D_D1(1), D1_D(1)], [D_D1(2), D1_D(2)], [D_D1(3), D1_D(3)], 'k-', 'LineWidth', 2);  
    plot3([A_A1(1), A1_A(1)], [A_A1(2), A1_A(2)], [A_A1(3), A1_A(3)], 'k-', 'LineWidth', 2);  
    
    
    
    
    plot3([A_B(1), A_D(1)], [A_B(2), A_D(2)], [A_B(3), A_D(3)], 'k-', 'LineWidth', 2);
    plot3([A_D(1), A_A1(1)], [A_D(2), A_A1(2)], [A_D(3), A_A1(3)], 'k-', 'LineWidth', 2);
    plot3([A_A1(1), A_B(1)], [A_A1(2), A_B(2)], [A_A1(3), A_B(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([B_A(1), B_C(1)], [B_A(2), B_C(2)], [B_A(3), B_C(3)], 'k-', 'LineWidth', 2);
    plot3([B_C(1), B_B1(1)], [B_C(2), B_B1(2)], [B_C(3), B_B1(3)], 'k-', 'LineWidth', 2);
    plot3([B_B1(1), B_A(1)], [B_B1(2), B_A(2)], [B_B1(3), B_A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([C_B(1), C_D(1)], [C_B(2), C_D(2)], [C_B(3), C_D(3)], 'k-', 'LineWidth', 2);
    plot3([C_D(1), C_C1(1)], [C_D(2), C_C1(2)], [C_D(3), C_C1(3)], 'k-', 'LineWidth', 2);
    plot3([C_C1(1), C_B(1)], [C_C1(2), C_B(2)], [C_C1(3), C_B(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([D_A(1), D_C(1)], [D_A(2), D_C(2)], [D_A(3), D_C(3)], 'k-', 'LineWidth', 2);
    plot3([D_C(1), D_D1(1)], [D_C(2), D_D1(2)], [D_C(3), D_D1(3)], 'k-', 'LineWidth', 2);
    plot3([D_D1(1), D_A(1)], [D_D1(2), D_A(2)], [D_D1(3), D_A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([A1_A(1), A1_B1(1)], [A1_A(2), A1_B1(2)], [A1_A(3), A1_B1(3)], 'k-', 'LineWidth', 2);
    plot3([A1_B1(1), A1_D1(1)], [A1_B1(2), A1_D1(2)], [A1_B1(3), A1_D1(3)], 'k-', 'LineWidth', 2);
    plot3([A1_D1(1), A1_A(1)], [A1_D1(2), A1_A(2)], [A1_D1(3), A1_A(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([B1_B(1), B1_A1(1)], [B1_B(2), B1_A1(2)], [B1_B(3), B1_A1(3)], 'k-', 'LineWidth', 2);
    plot3([B1_A1(1), B1_C1(1)], [B1_A1(2), B1_C1(2)], [B1_A1(3), B1_C1(3)], 'k-', 'LineWidth', 2);
    plot3([B1_C1(1), B1_B(1)], [B1_C1(2), B1_B(2)], [B1_C1(3), B1_B(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([C1_C(1), C1_B1(1)], [C1_C(2), C1_B1(2)], [C1_C(3), C1_B1(3)], 'k-', 'LineWidth', 2);
    plot3([C1_B1(1), C1_D1(1)], [C1_B1(2), C1_D1(2)], [C1_B1(3), C1_D1(3)], 'k-', 'LineWidth', 2);
    plot3([C1_D1(1), C1_C(1)], [C1_D1(2), C1_C(2)], [C1_D1(3), C1_C(3)], 'k-', 'LineWidth', 2);
    
    
    plot3([D1_D(1), D1_A1(1)], [D1_D(2), D1_A1(2)], [D1_D(3), D1_A1(3)], 'k-', 'LineWidth', 2);
    plot3([D1_A1(1), D1_C1(1)], [D1_A1(2), D1_C1(2)], [D1_A1(3), D1_C1(3)], 'k-', 'LineWidth', 2);
    plot3([D1_C1(1), D1_D(1)], [D1_C1(2), D1_D(2)], [D1_C1(3), D1_D(3)], 'k-', 'LineWidth', 2);
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

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
    