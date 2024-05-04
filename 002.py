apertei_parafuso_do_cabecote = str(input("Você apertou o parafuso? sim/não: "))
tenho_parafuso = str(input("Você tem o parafuso? sim/não: "))
tenho_motor = str(input("Você tem o motor? sim/não: "))

# Condição 1: Se eu não tiver o motor e os parafusos, eu não monto o cabeçote
if tenho_motor == 'não' and tenho_parafuso == 'não':
    print("Você não consegue montar o cabeçote")

# Condição 2: Se eu não tiver o parafuso, eu não monto
elif tenho_parafuso == 'não':
    print("Você não monta")
# Condição 3: Se eu já apertei o parafuso, tenho o parafuso, mas não tenho o motor, não posso montar
elif apertei_parafuso_do_cabecote == 'sim' and tenho_parafuso == 'sim' and tenho_motor == 'não':
    print("Você não monta")

# Condição 4: Se eu tiver o motor, mas não tiver o parafuso e não apertei o parafuso, não posso montar
elif tenho_motor == 'sim' and tenho_parafuso == 'não' and apertei_parafuso_do_cabecote == 'não':
    print("Você não consegue montar o cabeçote")

# Condição 5: Se eu já apertei o parafuso, está tudo certo
elif apertei_parafuso_do_cabecote == 'sim':
    print("Está tudo certo")

# Se nenhuma das condições acima for verdadeira, eu posso montar
else:
    print("Você pode montar o cabeçote")           