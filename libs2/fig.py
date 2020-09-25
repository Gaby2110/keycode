def fig1(alt,ancho):
    for i in range(alt):
        print ()
        for l in range(i+1):
            print("* ", end="")
            for j in range(ancho-2):
                print("- ", end="")
                
def fig2(b,h):
    for i in range(1,h):
        print ()
        for j in range(1,b):
            print ("* ", end="")

def fig3(h): 
    for i in range(h):
        print ()
        for j in range(i+1):
            print ("* ", end="")


