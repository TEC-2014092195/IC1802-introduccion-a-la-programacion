##c_matriz=[]
##m_matriz=[]
##        
##for i in range(5):#16 filas
##    for j in range(6):#10 columnas
##        c_matriz.append(j)
##    m_matriz.append(c_matriz)
##    c_matriz=[]
##
##print(m_matriz)


c={}
p={}
h={}
e={'vip':0,'normal':0,'graderia':0}
e['asien']="5x5"

h['3:30']=[e]
p['Peli0']=[h]
c['Cine0']=[p]
nom_cine=input("Ingrese nom de cine: ")
peli=input("Ingrese nom de peli: ")
hora=input("Ingrese nom de hora: ")
tipo_entrada=input("Ingrese tipo entrada: ")
can_entrada=int(input("Ingrese cantidad entradas: "))

print("estado Viejo")
print(c)
print("\n\nestado Nuevo")
l={}
l1={}
l2={}
l3={'vip':0,'normal':0,'graderia':0,'asien':0}


e2={}
h2={}
p2={}
c2={}

if not nom_cine in c:
    e2={'vip':0,'normal':0,'graderia':0,'asien':0}
    h2[hora]=[e2]
    p2[peli]=[h2]
    c2[nom_cine]=[p2]
    c.update(c2)
else:
    if not peli in c[nom_cine][0]:
        e2={'vip':0,'normal':0,'graderia':0,'asien':0}
        h2[hora]=[e2]
        p2[peli]=[h2]
        c[nom_cine][0].update(p2)
    else:
        if not hora in c[nom_cine][0][peli][0]:
            e2={'vip':0,'normal':0,'graderia':0,'asien':0}
            h2[hora]=[e2]
            c[nom_cine][0][peli][0].update(h2)
        else:
            e2={'vip':0,'normal':0,'graderia':0,'asien':0}
            
            old_asientos=c[nom_cine][0][peli][0][hora][0]['asien']
            old_can_entradas=c[nom_cine][0][peli][0][hora][0][tipo_entrada]

            e2['asien']="Matriz" + old_asientos
            e2[tipo_entrada]=can_entrada + old_can_entradas
            c[nom_cine][0][peli][0][hora][0].update(e2)

print(c)
            

    
##if not cine in c:
##    c[nom_cine]=[0]
##else:
##    if not peli in c[nom_cine][0][peli]:
        
        




















##if not hora in h:
##    l3['asien']="25x25"
##    l3[tipo_entrada]=can_entrada
##    l2[hora]=[l3]
##    n_h = l2.copy()
##
##else:
##
##    old_asientos=h[hora][0]['asien']
##    old_can_entradas=h[hora][0][tipo_entrada]
##    e['asien']="Matriz" + old_asientos
##    e[tipo_entrada]=can_entrada + old_can_entradas
##    h[hora]=[e]
##    n_h = h.copy()
##
##
##
##
##if not peli in p:
##    l1[peli]=[n_h]
##    n_p = l1.copy()
##else:
##    p[peli]=[n_h]
##    n_p = p.copy()
##    
##if not nom_cine in c:
##    l[nom_cine]=[n_p]
##    c.update(l)
##    print(c)
##else:
##    c[nom_cine]=[n_p]
##    print(c)





##if not hora in h:
##    print("La hora no esta",hora)
##    l3['asien']="25x25"
##    l3[tipo_entrada]=can_entrada
##    l2[hora]=[l3]
##    if not peli in p:
##        l1[peli]=[l2]
##        if not nom_cine in c:
##            l[nom_cine]=[l1]
##            c.update(l)
##            print(c)
##        else:
##            c[nom_cine]=[p]
##            print(c)
##    else:
##        p[peli]=[h]
##else:
##    old_asientos=h[hora][0]['asien']
##    old_can_entradas=h[hora][0][tipo_entrada]
##    e['asien']="Matriz" + old_asientos
##    e[tipo_entrada]=can_entrada + old_can_entradas
##    h[hora]=[e]
##
##print(c)
    
    
#print(c)
##if not nom_cine in c:
##    print("El cine no esta",nom_cine)
##    c[nom_cine]=[p]
##    if not peli in p:
##        print("La peli no esta",peli)
##        c[nom_cine][0][peli]=[h]
##        if not hora in h:
##            print("La hora no esta",hora)
##            c[nom_cine][0][peli][0][hora]['asien']=m_matriz
##            c[nom_cine][0][peli][0][hora][tipo_entrada]=int(can_entrada)
##            
##else:
##    print("Ya esta ",nom_cine)




##a = {'a' : 0, 'b' : 1}
##old_a=a['b']
##
##b = {'b' : old_a+2}
##
##a.update(b)
##print (a)
