from imgToVec import Img2Vec
from preprocessCatFace import cutFaceAndSave
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

img2vec = Img2Vec()

def changePicDepth(img):
    ###################################
    #改变位宽度
    if len(img.getbands()) > 3:
        img.load() # required for png.split()
        background= Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3]) # 3 is the alpha channel
    else:
        background = img
    return background
    ###################################

def comparePicWithImg(img1,img2):
    background1 = changePicDepth(img1)
    background2 = changePicDepth(img2)
    
    vec1 = img2vec.get_vec(background1)
    vec2 = img2vec.get_vec(background2)

    return cosine_similarity(vec1.reshape((1, -1)), vec2.reshape((1, -1)))[0][0]

def comparePicWithPath(filepath1,filepath2):
    cutFaceAndSave(filepath1)
    cutFaceAndSave(filepath2)

    img1 = Image.open(filename1)
    img2 = Image.open(filename2)

    return comparePicWithImg(img1,img2)



if __name__ == '__main__':    
    filename1 = r"./images/1_3.jpg"
    filename2 = r"./images/1_4.jpg" 

    print(comparePicWithPath(filename1,filename2))