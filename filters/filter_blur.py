import cv2
import logger


def filter_blur(img, nb):
    '''
    Apply a filter on pictures
    :param img: String, the file of th e picture to filter
    :param nb: Int value of the blur to apply
    :return: the filtered picture
    '''
    logger.log('Apply the filter blur')
    if (nb > 2) & (nb % 2 != 0):
        blur = cv2.GaussianBlur(img, (nb, nb), cv2.BORDER_DEFAULT)
        return blur
    elif nb <= 1:
        print("Value too small")
        return None
    else:
        print("Please enter impair value")
        return None
