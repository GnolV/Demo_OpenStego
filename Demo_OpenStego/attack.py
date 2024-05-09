import cv2
import numpy as np
import random as rd

class Attack:
    @staticmethod
    def blur(img: np.ndarray):
        return cv2.blur(img, (10, 10))

    @staticmethod
    def rotate180(img: np.ndarray):
        img = img.copy()
        return cv2.rotate(img, cv2.ROTATE_180)

    @staticmethod
    def rotate90(img: np.ndarray):
        img = img.copy()
        return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    @staticmethod
    def chop5(img: np.ndarray):
        img = img.copy()
        w, h = img.shape[:2]
        return img[int(w * 0.05):, :]

    @staticmethod
    def chop10(img: np.ndarray):
        img = img.copy()
        w, h = img.shape[:2]
        return img[int(w * 0.1):, :]

    @staticmethod
    def chop30(img: np.ndarray):
        img = img.copy()
        w, h = img.shape[:2]
        return img[int(w * 0.3):, :]

    @staticmethod
    def gray(img: np.ndarray):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray

    @staticmethod
    def saltnoise(img: np.ndarray):
        img = img.copy()
        for k in range(1000):
            i = int(np.random.random() * img.shape[1])
            j = int(np.random.random() * img.shape[0])
            if img.ndim == 2:
                img[j, i] = 255
            elif img.ndim == 3:
                img[j, i, 0] = 255
                img[j, i, 1] = 255
                img[j, i, 2] = 255
        return img

    @staticmethod
    def randline(img: np.ndarray):
        img = img.copy()
        h, w = img.shape[:2]
        cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
        cv2.rectangle(img, (0, 0), (300, 128), (255, 0, 0), 3)
        cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
        cv2.line(img, (0, 511), (511, 0), (255, 0, 255), 5)
        return img

    @staticmethod
    def cover(img: np.ndarray):
        img = img.copy()
        h, w = img.shape[:2]
        cv2.circle(img, (rd.randint(63, h - 63), rd.randint(63, w - 63)), 63, (0, 0, 255), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'D19ATTT', (10, 500), font, 4, (255, 255, 0), 5)
        return img

    @staticmethod
    def brighter(img: np.ndarray):
        img = img.copy()
        alpha = 1.2
        beta = 20
        img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        return img

    @staticmethod
    def darker(img: np.ndarray):
        img = img.copy()
        alpha = 0.8
        beta = -20
        img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        return img

    @staticmethod
    def largersize(img: np.ndarray):
        w, h = img.shape[:2]
        return cv2.resize(img, (int(h * 1.5), int(w * 1.5)))

    @staticmethod
    def smallersize(img: np.ndarray):
        w, h = img.shape[:2]
        return cv2.resize(img, (int(h * 0.5), int(w * 0.5)))
    
    @staticmethod
    def flip_ver(img: np.ndarray):
        return cv2.flip(img, 0)
    
    @staticmethod
    def flip_hor(img: np.ndarray):
        return cv2.flip(img, 1)
    
    @staticmethod
    def negative(img: np.ndarray):
        return cv2.bitwise_not(img)

if __name__ == "__main__":
    img_dir = input("Enter image directory: ")
    img_format = img_dir.split(".")
    format = img_format[1]
    img_locat = "./Attacked"
    img = cv2.imread(img_dir)
    img_blur = Attack.blur(img)
    cv2.imwrite(img_locat + "img_blur." + format, img_blur)
    img_rot180 = Attack.rotate180(img)
    cv2.imwrite(img_locat + "img_rot180." + format, img_rot180)
    img_rot90 = Attack.rotate90(img)
    cv2.imwrite(img_locat + "img_rot90." + format, img_rot90)
    img_chop5 = Attack.chop5(img)
    cv2.imwrite(img_locat + "img_chop5." + format, img_chop5)
    img_chop10 = Attack.chop10(img)
    cv2.imwrite(img_locat + "img_chop10." + format, img_chop10)
    img_chop30 = Attack.chop30(img)
    cv2.imwrite(img_locat + "img_chop30." + format, img_chop30)
    img_gray = Attack.gray(img)
    cv2.imwrite(img_locat + "img_gray." + format, img_gray)
    img_salt = Attack.saltnoise(img)
    cv2.imwrite(img_locat + "img_salt." + format, img_salt)
    img_rand = Attack.randline(img)
    cv2.imwrite(img_locat + "img_rand." + format, img_rand)
    img_cover = Attack.cover(img)
    cv2.imwrite(img_locat + "img_cover." + format, img_cover)
    img_bright = Attack.brighter(img)
    cv2.imwrite(img_locat + "img_brighter." + format, img_bright)
    img_dark = Attack.darker(img)
    cv2.imwrite(img_locat + "img_darker." + format, img_dark)
    img_larger = Attack.largersize(img)
    cv2.imwrite(img_locat + "img_larger." + format, img_larger)
    img_smaller = Attack.smallersize(img)
    cv2.imwrite(img_locat + "img_smaller." + format, img_smaller)
    img_flip_ver = Attack.flip_ver(img)
    cv2.imwrite(img_locat + "img_flip_ver." + format, img_flip_ver)
    img_flip_hor = Attack.flip_hor(img)
    cv2.imwrite(img_locat + "img_flip_hor." + format, img_flip_hor)
    img_negative = Attack.negative(img)
    cv2.imwrite(img_locat + "img_negative." + format, img_negative)