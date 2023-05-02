l = [1,2,3,(1,2,3),4,5,6,[1,{"key1":1,"key2":2,"key3":{"Alumno1","Alumno2",True}},{1,2,3}]]

def verListaRecursivaConTipoDatos(l,num,tipo,y):
    if num>7:
        print("fin")
        
    else:
        if type(l[num]) == tuple:
            print(" _>",l[num])
            verListaRecursivaConTipoDatos(l,num+1,type(l),0)
        elif type(l[num]) == list:
            if y<3:
                if y==0:
                    print("  ->",l[num][y])
                    verListaRecursivaConTipoDatos(l,num,type(l),y+1)
                elif y==1:
                    print("  .>",l[num][y])
                    verListaRecursivaConTipoDatos(l,num,type(l),y+1)
                elif y==2:
                    print("   =>",l[num][y])
                    verListaRecursivaConTipoDatos(l,num,type(l),y+1)
            
            else:
                print("Feo")
        
        else:
            print(l[num])
            verListaRecursivaConTipoDatos(l,num+1,type(l),0)
    
    return
verListaRecursivaConTipoDatos(l,0,type(l),0)