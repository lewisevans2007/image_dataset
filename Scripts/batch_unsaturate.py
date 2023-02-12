from PIL import Image,ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw 
import os
rootdir = "wood"
os.mkdir("edited/"+rootdir+"/")
for g in range(len(os.listdir(rootdir))):
    imgstr = str(os.listdir(rootdir)[g])
    img = Image.open(rootdir+"/"+imgstr)
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(0)
    img2.save("edited/"+rootdir+"/"+str(imgstr[:imgstr.index(".")]+str(".JPEG")))