from source.k import *


icc=readIcc() #reading icc top100
nblist=readNb() #reading nb top10
calist=readCart() #reading cart top10

merge(icc,nblist,calist) #Merging Icc nb and cart ranks into single list
convert(sys.argv[1:]) # to convert into json for graph input