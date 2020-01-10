import dlib
from skimage import io

detec = dlib.get_frontal_face_detector()
win = dlib.image_window()
img = io.imread('1.jpg')
dets = detec(img, 1)
win.set_image(img)
win.add_overlay(dets)
dlib.hit_enter_to_continue()

