nome = "Guilherme"
idade = 28

pessoa = {"nome":"Paloma", "idade":28}

print ("Olá, me chamo %s. Eu tenho %d anos de idade." % (nome, idade))

print ("Olá, me chamo {}. Eu tenho {} anos de idade." .format(nome, idade)) 

print ("Olá, me chamo {0}. Eu tenho {1} anos de idade." .format(nome, idade)) 

print ("Olá, me chamo {nome}. Eu tenho {idade} anos de idade." .format(nome=nome, idade=idade)) 

print ("Olá, me chamo {nome}. Eu tenho {idade} anos de idade." .format(**pessoa)) 

print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade.") 

PI = 3.14159

print (f"Valor de PI é: {PI:.2f}")



