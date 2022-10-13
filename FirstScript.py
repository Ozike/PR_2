while True:     
    inp : str = input()
    if (len(inp) < 3):
        print("Ввод не менее трёх символов")
    else:   
        count : int = 0
        for value in inp:
            try:
                float(value)    
            except:
                count += 1 
        if(count == len(inp)):
            con = open('./Folder/'+inp, 'w')
            con.close()
        else:
            print("Вводить числа нельзя")
            continue



            


