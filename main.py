from numpy import asarray
from PIL import Image
import numpy  
  

if __name__ == '__main__':
    img = Image.open('Imagem.png')
    numpydata = asarray(img)
    

    for i in range(numpydata.shape[0]):
        for j in range(numpydata.shape[1]):
            if numpy.array_equal(numpydata[i][j],[255,255,255]):
                  numpydata[i][j] = [255,0,0]
                  
    
    data = Image.fromarray(numpydata)
      
    data.save('ImagemFinal.png')