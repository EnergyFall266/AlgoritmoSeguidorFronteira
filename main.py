
from PIL import Image
import numpy as np 



def SeguidorFronteira(numpydata, i, j):
    oitoVizinhanca=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],[i,j-1]]
    borda=[]

    numpydata[i][j] = [255,0,0]
    borda.append([i,j])
    endObjeto = True
    
    vetorIncidente = 7
    # percorre ate achar o primeiro ponto da figura
    
    while endObjeto:
        indice = (vetorIncidente+1)%8
        vizinhoAtual = numpydata[oitoVizinhanca[indice][0]][oitoVizinhanca[indice][1]]
        # executa até achar um branco

        while  vizinhoAtual[0] != 255 and vizinhoAtual[1] != 255 and vizinhoAtual[2] != 255: 
            indice = (indice+1)%8
            vizinhoAtual = numpydata[oitoVizinhanca[indice][0]][oitoVizinhanca[indice][1]]

            if vetorIncidente == indice or np.array_equal(vizinhoAtual,[255,0,0]):
                endObjeto = False
                break

        if endObjeto:
            numpydata[oitoVizinhanca[indice][0]][oitoVizinhanca[indice][1]] = [255,0,0]
            borda.append([oitoVizinhanca[indice][0],oitoVizinhanca[indice][1]])

            # ponto anterior
            anteriori = i
            anteriorj = j

            # ponto atual
            i = oitoVizinhanca[indice][0]
            j = oitoVizinhanca[indice][1]
            oitoVizinhanca=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],[i,j-1]]
            ind = 0

            # encontrar o proximo vetorIncidente na oitoVizinhanca
            while ind<len(oitoVizinhanca):
                if oitoVizinhanca[ind][0] == anteriori and oitoVizinhanca[ind][1] == anteriorj:
                    vetorIncidente = ind
                    break
                ind +=1

    return borda


if __name__ == '__main__':
    with open("bordas.txt","a") as f:
        f.truncate(0)
    # transforma a img em matriz
    img = Image.open('Imagem.png')
    numpydata = np.array(img)
    # listaObjetos=[]
    i = 0
    j = 0
    while i < numpydata.shape[0]:
        j = 0
        while j < numpydata.shape[1]:
            # procura o pixel do primeiro objeto
            if np.array_equal(numpydata[i][j],[255,255,255]):
                if np.array_equal(numpydata[i][j-1],[255,0,0]):
                    while np.array_equal(numpydata[i][j],[255,255,255]):
                        j+=1
                else:                           
                    borda = SeguidorFronteira(numpydata, i, j)
                    # listaObjetos.append(borda)
                    with open("bordas.txt","a") as f:
                        f.write(f'{borda}\n')
                   
            j += 1
        i += 1
    
    data = Image.fromarray(numpydata)
      
    data.save('ImagemFinal.png')