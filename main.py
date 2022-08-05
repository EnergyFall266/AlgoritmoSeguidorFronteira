
from PIL import Image
import numpy as np 



def SeguidorFronteira(numpydata, i, j, maxi, maxj):
    oitoVizinhanca=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],[i,j-1]]
    borda=[]

    numpydata[i][j] = [255,0,0]
    borda.append([i,j])
    endObjeto = True
    
    vetorIncidente = 7
    # percorre ate achar o primeiro ponto da figura
    while endObjeto:
        indice = (vetorIncidente+1)%8
        while ( oitoVizinhanca[indice][0]>= maxi or oitoVizinhanca[indice][1] >= maxj) or (oitoVizinhanca[indice][0] < 0 or oitoVizinhanca[indice][1] < 0):
            indice = (indice+1)%8
        
        vizinhoAtual = numpydata[oitoVizinhanca[indice][0]][oitoVizinhanca[indice][1]]

        # executa até achar um branco
        while  vizinhoAtual[0] != 255 and vizinhoAtual[1] != 255 and vizinhoAtual[2] != 255: 
            indice = (indice+1)%8
            atualI = oitoVizinhanca[indice][0]
            atualJ = oitoVizinhanca[indice][1]            
            
            if (atualI >= maxi or atualJ >= maxj) or (atualI < 0 or atualJ < 0):
                continue 

            vizinhoAtual = numpydata[atualI][atualJ]

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

            
                
            vetorIncidente = oitoVizinhanca.index([anteriori, anteriorj])
               

    return borda


if __name__ == '__main__':
    with open("bordas.txt","a") as f:
        f.truncate(0)
    imagem = input("Insira o caminho da imagem: ")
    imagemFinal = input("Insira o nome da imagem de saida (com a extensao): ")
    # transforma a img em matriz
    img = Image.open(imagem)
    numpydata = np.array(img)
    # listaObjetos=[]
    maxi = numpydata.shape[0]
    maxj = numpydata.shape[1]
    i = 0
    j = 0
    while i < maxi:
        j = 0
        while j < maxj:
            # procura o pixel do primeiro objeto
            if np.array_equal(numpydata[i][j],[255,255,255]):
                if np.array_equal(numpydata[i][j-1],[255,0,0]):
                    while np.array_equal(numpydata[i][j],[255,255,255]):
                        j+=1
                else:                           
                    borda = SeguidorFronteira(numpydata, i, j, maxi, maxj)
                    # listaObjetos.append(borda)

                    string = ''

                    for object in borda:
                        string += str(object[0]) + ',' + str(object[1]) + ','
                    string = string[:-1] + ';'

                    f = open('bordas.txt', 'a')
                    f.write(string + '\n')
                    

      
            j += 1
        i += 1
    
    data = Image.fromarray(numpydata)
      
    data.save(imagemFinal)