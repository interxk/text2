def sp2sp(path):

    from cv2 import cv2
    import os,png2png2
    import matplotlib.pyplot as plt
    cap = cv2.VideoCapture(path)
    ret, frame = cap.read()
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*"MP42")
    raw_height,raw_width,_ = frame.shape
    video_writer = cv2.VideoWriter('result01.avi', fourcc, fps, (raw_width, raw_height))
    count=0
    while(ret):
    
        now=png2png2.png2png(frame)
        video_writer.write(now)
        count+=1
        if(count%10==0):
            print("已完成"+str(count)+"帧")
        ret, frame = cap.read()
    video_writer.release
    cap.release
    print("zhongzhi")
