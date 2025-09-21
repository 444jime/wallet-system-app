from business import AccVerifier
from decimal import Decimal
import time

class AccHandler:
    def __init__(self,user):
        self.user = user
        self.verifier = AccVerifier(self.user)

    def show_menu(self):
        while True:
            print("\n---------------------------" \
            "\nSeleccione una opcion:" \
            "\n- Crear cuenta" \
            "\n- Comprar monedas" \
            "\n- Vender monedas" \
            "\n- Depositar ARS" \
            "\n- Ver saldo" \
            "\n- Volver")
            user_input = input('').lower()

            if 'crear' in user_input:
                self.create_acc()
            elif 'comprar' in user_input:
                self.buy_currency()
            elif 'vender' in user_input:
                self.sell_currency()
            elif 'depositar' in user_input:
                self.deposit_amount()
            elif 'ver saldo' in user_input:
                self.check_balance()
            elif 'volver' in user_input:
                break
            else:
                print('Ingreso incorrecto')

    def create_acc(self):
        while True:
            print("\nIngrese el codigo de la moneda en la que desea crear la cuenta:")
            cod = input('- ')

            try:
                self.verifier.cod_verifier(cod)
                self.verifier.create_acc(cod.upper())
                print('Cuenta creada correctamente')
                print('\nVolviendo al menu...')
                break
            except ValueError as e:
                print(f'Error: {e}')
                user_input = input('\nQueres intentar de nuevo? si/no\n').strip().lower()
                if 'si' not in user_input:
                    print('\nVolviendo al menu\n')
                    return 
                

    def check_balance(self):
        while True:
            print('\nIngrese el codigo de la cuenta que quiere saber el saldo:')
            cod = input('- ')
            
            try:
                self.verifier.cod_verifier(cod)
                saldo_cod = self.verifier.get_acc_balance(cod)
                print(f'Saldo actual en {cod.upper()}: {saldo_cod}')
                print('\nVolviendo al menu...')
                break
            except ValueError as e:
                print(e)
                user_input = input('Queres volver a intentarlo? si/no\n').strip().lower()
                if 'si' not in user_input:
                    print('\nVolviendo al menu...')
                    return 
                
    def deposit_amount(self):
        while True:
            print('\nIngrese el monto a depositar:')
            amount = input('ARS$')
            try:
                amount = Decimal(amount)
            except:
                print("Error: Ingrese un número valido")
                continue

            try:
                current_balance = self.verifier.deposit_verify(amount)
                print(f'Monto depositado correctamente, saldo actual en ARS: {current_balance}')
                break
            except ValueError as e:
                print(f'Error: {e}')
        print('\nVolviendo al menu...')
        return 
    
    def buy_currency(self):
        while True: 
            cod = input('\nIngrese el codigo de la moneda a comprar: ').upper()

            try:
                self.verifier.cod_verifier(cod)
            except ValueError as e:
                print(f'Error: {e}')
                continue

            if cod == 'ARS':
                print('\nIngreso invalido, no puede comprar ARS, ingrese un codigo valido')
                continue

            amount = input(f'\nIngrese monto en {cod} a comprar: ')

            start_time = time.time()
            user_input = input("Esta seguro que desea realizar la compra? (S/N)\n")
            if (time.time()-start_time) > 120:
                user_input="N"
                print('\nTiempo agotado, compra cancelada. Volviendo al menu...')
                return                 
            if user_input.upper() != "S":
                print('\nCompra cancelada. Volviendo al menu...')
                return
        
            try:
                saldo_ARS, saldo_cod = self.verifier.buy_verifier("ARS",cod.upper(),amount)
                print('Compra exitosa!')
                print(f'saldo actual en ARS: {saldo_ARS} \nSaldo actual en {cod.upper()}: {saldo_cod}')
                print('\nVolviendo al menu...')
                break        
            except ValueError as e:
                print(f'Error: {e}')
                user_input = input('\nQueres volver a intentarlo? si/no\n').strip().lower()
                if 'si' not in user_input:
                    print('\nVolviendo al menu...')
                    return

    def sell_currency(self):
        while True: 
            cod = input('\nIngrese el codigo de la moneda a vender: ').upper()

            try:
                self.verifier.cod_verifier(cod)
            except ValueError as e:
                print(f'Error: {e}')
                continue

            if cod == 'ARS':
                print('\nIngreso invalido, no puede vender ARS, ingrese un codigo valido')
                continue

            amount = input(f'\nIngrese monto en {cod} a vender: ')
        
            try:
                saldo_origen, saldo_ARS = self.verifier.sell_verifier(cod,"ARS",amount)
                print('\nVenta exitosa!')
                print(f'Saldo actual en {cod.upper()}: {saldo_origen} \nSaldo actual en ARS: {saldo_ARS}')
                print('\nVolviendo al menu...')
                break        
            except ValueError as e:
                print(f'Error: {e}')
                user_input = input('\nQueres volver a intentarlo? si/no\n').strip().lower()
                if 'si' not in user_input:
                    print('\nVolviendo al menu...')
                    return                