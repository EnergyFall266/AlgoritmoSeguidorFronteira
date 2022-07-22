from numpy import asarray, broadcast_arrays
from PIL import Image
import numpy  



def SeguidorFronteira(numpydata, i, j):
    oitoVizinhanca=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],[i,j-1]]
    borda=[]

    numpydata[i][j] = [255,0,0]
    borda.append([i,j])
    
    indice = 7
    # percorre ate achar o primeiro ponto da figura
    while i != borda[0][0] and j != borda[0][1]:
        indice = (indice+1)%8
        vizinhoAtual = numpydata[oitoVizinhanca[indice][0]][oitoVizinhanca[indice][1]]
        # executa até achar um branco
        while numpy.not_equal(vizinhoAtual, [255,255,255]): 
            # n entrou
            print("deu")
            indice = (indice+1)%8
            vizinhoAtual = numpydata[oitoVizinhanca[indice][0]][oitoVizinhanca[indice][1]]
        
        numpydata[oitoVizinhanca[indice][0]][oitoVizinhanca[indice][1]] = [255,0,0]
        borda.append([oitoVizinhanca[indice][0],oitoVizinhanca[indice][1]])
        # ponto anterior
        anteriori = i
        anteriorj = j
        # ponto atual
        i = oitoVizinhanca[indice][0]
        j = oitoVizinhanca[indice][1]
        ind = 0
        while ind<range(len(oitoVizinhanca)):
            if oitoVizinhanca[ind][0] == anteriori and oitoVizinhanca[ind][1] == anteriorj:
                indice = ind
                break

            ind +=1
        


    return borda


if __name__ == '__main__':
    img = Image.open('Imagem.png')
    numpydata = asarray(img)
    listaObjetos=[]

    for i in range(numpydata.shape[0]):
        for j in range(numpydata.shape[1]):
            if numpy.array_equal(numpydata[i][j],[255,255,255]):
                
                borda = SeguidorFronteira(numpydata, i, j)
                listaObjetos.append(borda)
                break        
        # tratar para ignorar os pontos vermelhos e brancos até achar um preto - ignorar objeto ja tratado
    
   
    data = Image.fromarray(numpydata)
      
    data.save('ImagemFinal.png')

