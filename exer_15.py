dia1 = {"Mouse", "Teclado", "Monitor"}
dia2 = {"Monitor", "Notebook", "Mouse"}
vendidos_nos_dois_dias = dia1.union(dia2)
vendidos_apenas_no_dia1 = dia1.difference(dia2)
vendidos_apenas_no_dia2 = dia2.difference(dia1)
print("Produtos vendidos nos dois dias:", vendidos_nos_dois_dias)
print("Produtos vendidos apenas no dia 1:", vendidos_apenas_no_dia1)
print("Produtos vendidos apenas no dia 2:", vendidos_apenas_no_dia2)