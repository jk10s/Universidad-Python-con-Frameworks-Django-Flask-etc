
a="asdas"
b=0

try:
    resultado=a/b
    print(resultado)

except TypeError as e:
    print(f'TypeError -Ocurrio un error {e}, {type(e)}')

except ZeroDivisionError as e:
    print(f'zerDivisionerror -Ocurrio un error {e}, {type(e)}')

except Exception as e:
    print(f'error de excepcion {e}')

print("ominiennto el error")