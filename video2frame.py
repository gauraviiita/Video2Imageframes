import cv2
import time
  
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file
    
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
    a=1
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames
        if(a==1):
            initial_time=time.time()
            a=0
        
        success, image = vidObj.read()
        current_time=time.time()
        if((current_time-initial_time)>=1):
            print((current_time-initial_time))
            break
  
        # Saves the frames with frame-count
        #cv2.imshow("Im",image)
        print(time.time())
        cv2.imwrite("/home/gaurav/Videos/Movies/inshot/my_frames/frame%6d.jpg" % count, image) 
  
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    #FrameCapture(r"/home/gaurav/Desktop/Gaurav/URV/HMP/H3.6M_ImageData/Visualization-of-Human3.6M-Dataset/images/H3.6M/gt/S1/walkingdog.gif")
    FrameCapture(r"/home/gaurav/Videos/Movies/inshot/my_video.mp4")
