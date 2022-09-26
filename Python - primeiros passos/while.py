while True:
  number = int(input('Número PAR para continuar e ÍMPAR para parar: '))
  
  if number % 2:  # se houver resto é impar
    print('OBRIGADO!')
    break
  else:
    print('AEEEE, vamos continuar!!!')
    