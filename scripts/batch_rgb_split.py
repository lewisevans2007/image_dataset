from PIL import Image,ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw 
import os
rootdir = "grass"
os.mkdir("edited/"+rootdir+"/")
for g in range(len(os.listdir(rootdir))):
    imgstr = str(os.listdir(rootdir)[g])
    os.mkdir("edited/"+rootdir+"/"+imgstr)
    img = Image.open(rootdir+"/"+imgstr)
    data = img.getdata()
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]
    img.putdata(r)
    img.save("edited/"+rootdir+"/"+imgstr+"/red.png")
    img.putdata(g)
    img.save("edited/"+rootdir+"/"+imgstr+"/green.png")
    img.putdata(b)
    img.save("edited/"+rootdir+"/"+imgstr+"/blue.png")