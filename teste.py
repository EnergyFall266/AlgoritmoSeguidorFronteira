from numpy import asarray, broadcast_arrays
from PIL import Image
import numpy  
img = Image.open('teste.png')
numpydata = asarray(img)
listaObjetos=[]

for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        # if numpy.not_equal(numpydata[i][j],[255,255,255]):
        print(numpydata.shape[0])
        print(numpydata.shape[1])
            
            
            
    # tratar para ignorar os pontos vermelhos e brancos até achar um preto - ignorar objeto ja tratado


data = Image.fromarray(numpydata)
    
data.save('testeFinal.png')