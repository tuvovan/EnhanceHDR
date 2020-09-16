import cv2
import argparse
import numpy as np

from utils import *
from filters import *

def HDR(path, flag):
    image = cv2.imread(path)
    S = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)/255.0
    S = S + 1e-20
    image = 1.0*image/255

    if flag:
        I = gdft(S, 3)
    else:
        I = wlsFilter(S)
    mI = np.mean(I)
    R = np.log(S+1e-20) - np.log(I+1e-20)
    R_eh = SRS(R, I)

    v_s = [0.2, (mI+0.2)/2, mI, (mI+0.8)/2, 0.8]

    I_vts = VIG(I, 1.0-I, v_s)
    L_eh = tone_production(R_eh, I_vts)
    
    ratio = np.clip(L_eh/ S, 0, 3)
    b,g,r = cv2.split(image)

    b_eh = ratio * b
    g_eh = ratio * g
    r_eh = ratio * r

    out = cv2.merge((b_eh, g_eh, r_eh))
    return np.clip(out, 0.0, 1.0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

	# Input Parameters

    parser.add_argument('--image_path', type=str, default="imgs/Duck.png")
    parser.add_argument('--filter', type=bool, default=True)
    config = parser.parse_args()

    out = HDR(config.image_path, config.filter)
    save_name = config.image_path.split('/')[0] + '/rs_' + config.image_path.split('/')[1]
    cv2.imwrite(save_name, np.uint8(out*255))

