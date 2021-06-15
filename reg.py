import scripts.ssim_processing
import scripts.visualize as vis
import cv2
import numpy as np
import sys
import glob

print("Running registration algorithm")

img_path = sys.argv[1]
out_path = sys.argv[2]
img_list = glob.glob(img_path + "/*.png")

crop_y = 70
crop_x = 270

for i in range(len(img_list)-1):

    img1 =cv2.imread(img_list[i])
    img2 =cv2.imread(img_list[i+1])
    crop_lim = [crop_y,img1.shape[0]-crop_y,crop_x,img1.shape[1]-crop_x]
    img1 = img1[crop_lim[0]:crop_lim[1],crop_lim[2]:crop_lim[3]]
    img2 = img2[crop_lim[0]:crop_lim[1],crop_lim[2]:crop_lim[3]]


    ShiftReg    = cv2.reg_MapperGradShift()
    PyrShiftReg = cv2.reg_MapperPyramid(ShiftReg)
    ShiftMap    = PyrShiftReg.calculate(img1, img2)
    ShiftMap    = cv2.reg.MapTypeCaster_toShift(ShiftMap)

    AffineMap   = cv2.reg_MapAffine(np.eye(2),ShiftMap.getShift())

    AffineReg    = cv2.reg_MapperGradAffine()
    PyrAffineReg = cv2.reg_MapperPyramid(AffineReg)
    AffineMap    = PyrAffineReg.calculate(img1, img2,AffineMap)
    AffineMap    = cv2.reg.MapTypeCaster_toAffine(AffineMap)

    H = np.eye(3)
    H[0:2,2:3] = ShiftMap.getShift()
    ProjMap = cv2.reg_MapProjec(H)

    ProjReg    = cv2.reg_MapperGradProj()
    PyrProjReg = cv2.reg_MapperPyramid(ProjReg)
    ProjMap    = PyrProjReg.calculate(img1, img2,ProjMap)
    ProjMap    = cv2.reg.MapTypeCaster_toProjec(ProjMap)

    np.savetxt(out_path+'/H'+str(i+1)+'.txt',ProjMap.getProjTr(),'%10.5f')

    #vis.visualizeImg(img1)
