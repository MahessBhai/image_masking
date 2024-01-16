# image_masking
pre-processing cropped images for alpha numeric classification tasks to be fed to KNN/CNN network 

# steps to use
# # for single objects in the frame:
add path to the saved images to the directry
and run script, images will be saved to the inverts folder

# # for multiple objects in the main frame
use a object detection script to detect the objects in the frame and return the x, y, w(width), h(height) values in a list
and save results in inverts folder 
