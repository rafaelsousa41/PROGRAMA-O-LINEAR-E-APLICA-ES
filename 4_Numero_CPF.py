from createdFunctions import cpfValidator


cpf = str(input("Digite seu CPF (XXX.XXX.XXX-XX): "))
valid = cpfValidator(cpf)

if valid:
    print(f"CPF {cpf} é válido!")
else:
    print(f"CPF {cpf} não é um número válido!")

# 197.049.030-40
# 452.959.518-20
# 123.747.258-09

# Inválidos
# 111.111.222-34
