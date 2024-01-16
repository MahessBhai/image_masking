import numpy as np
import cv2
import os

def color_distance(color1, color2):
    return np.linalg.norm(color1 - color2)
def categorize_colors(colors, threshold):
    categories = []
    for color in colors:
        for category in categories:
            if color_distance(color, category[0]) < threshold:
                category.append(color)
                break
        else:

            categories.append([color])
    return categories
def smooth_image(image):
    # Apply Gaussian blur to smooth the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

def invert(image,filename,i=0,):
    unique_colors = np.unique(image.reshape(-1, image.shape[2]), axis=0)

    num_unique_colors = len(unique_colors)

    # adjust according to your needs
    color_threshold = 120.0
    color_categories = categorize_colors(unique_colors, color_threshold)
    binary_images = []
    for category_idx, color_category in enumerate(color_categories):
        category_mask = np.zeros_like(image[:, :, 0], dtype=np.uint8)
        for color in color_category:
            mask = np.all(image == color, axis=-1) 
            category_mask[mask] = 255  

        # innitially this        
        # binary_images.append(category_mask)
        #now this
        smoothed_image = smooth_image(category_mask)
        binary_images.append(smoothed_image)

    for idx, inverted_image in enumerate(binary_images):
        cv2.imwrite("inverts\{}Inverted Image {} - Color {}.jpeg".format(filename,i,idx), inverted_image)


if __name__=="main":

    #path to directry with images
    path = r"path"
    

    for filename in os.listdir(path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            
            # # if there is one object in the frame use this  
            image_path = os.path.join(path, filename)
            frame11 = cv2.imread(image_path)

            crop_img = frame11
            #cv2.imwrite("{}_crop_{}.jpeg".format(filename,i),crop_img)
            invert(crop_img, filename)



            # # for multiple objects in the original image, crop the required object using a object detection algorithm and give input x,y,w,h            
            # detector =   #TargetDetection(yolo_path=path_to_yolo, model_path=path_to_model, image_path=image_path)
            # datt = detector() # list of x,y,w,h coordinates of multiple detected objects
            # print(datt)
            # for i in range(len(datt)):
            #     crop_img = frame11[datt[i][0]:datt[i][1], datt[i][2]:datt[i][3]]
            #     #cv2.imwrite("{}_crop_{}.jpeg".format(filename,i),crop_img)
            #     invert(i,crop_img, filename)
