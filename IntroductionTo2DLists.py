dictionary = [[3,7,8],[2,4,6],[1,9,5]]
print (dictionary)
print (dictionary[0][2])
print (dictionary[1])
print (dictionary[2])
for i in range (3):
    for j in range (3):
        print (dictionary[i][j])


print ("Here is the second 2D List! ¬.¬")


thesaurus = [[11,13,15],[12,14,16],[17,18,19]]
sigma = [[0,0,0],[0,0,0],[0,0,0]]
def adlib() :
   
   for x in range (3):
       for y in range (3):

        sigma[x][y] =  dictionary [x][y] / thesaurus [x][y]
        print (sigma)

adlib ()



