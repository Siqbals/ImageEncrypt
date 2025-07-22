'''imports'''

#import image processing module 
import cv2
#import math functions 
import numpy as np
#import polar coordinate conversion module 
from skimage.transform import warp_polar
#import function that converts our iris to a unique code 
import hashlib

'''
function to convert the image to grayscale to make it more efficient 
then use median blur to reduce the noise 
''' 
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.medianBlur(img, 5)
    return img

'''
detect iris function 
detects and iris in the provided image by finding dark pupil first and then expanding outward to find the rest of the eye
returns the pupil center coordinates and the iris radius coordinates (where the iris is in the image) 
'''
def detect_iris(img):
    #pupil detection by detecting the darkest region in the image (ideally )
    _, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #then find the larger dark circle around the darkest region (the pupil)
    max_radius = 0
    pupil_center = None
    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        if radius > max_radius and radius < 60:
            max_radius = radius
            pupil_center = (int(x), int(y))

    #if we do not find a pupil center or a dark region to expand from, there is no iris
    #here ensures the image only detects irises and accepts nothing else as encrypt standard
    if pupil_center is None:
        print("[!] Pupil not found.")
        return None

    # then find iris boundary using a constant estimate
    iris_radius = int(max_radius * 2.5) 

    top = max(0, int(y - iris_radius))
    bottom = min(img.shape[0], int(y + iris_radius))
    left = max(0, int(x - iris_radius))
    right = min(img.shape[1], int(x + iris_radius))

    iris = img[top:bottom, left:right]

    if iris.shape[0] == 0 or iris.shape[1] == 0:
        print("[!] Iris region empty or out of bounds.")
        return None

    # Step 5: Normalize (unwrap) iris region using warp_polar
    try:
        normalized = warp_polar(iris, center=(iris.shape[1]//2, iris.shape[0]//2),
                                radius=iris.shape[0]//2, scaling='linear')
        return normalized
    except Exception as e:
        print("[!] Normalization failed:", e)
        return None

def createirissig(normalized_img):
    #change up the image to get a better hash 
    changesize = cv2.resize(normalized_img, (64, 64))
    onedim = changesize.flatten()

    #return SHA256 hash 
    return hashlib.sha256(onedim.tobytes()).hexdigest()

def irissig(image_path):
    #get the iris signiture 
    img = preprocess_image(image_path)
    normalized_iris = detect_iris(img)

    #check if we have a iris in the image 
    if normalized_iris is not None:
        signature = createirissig(normalized_iris)
        return signature
    else:
        return "Iris not detected."

image_path = "iristest.jpg"
print("Unique Iris Signature:", irissig(image_path))



