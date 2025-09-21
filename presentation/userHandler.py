from .accHandler import AccHandler
from business import UserVerifier
import pwinput

class UserHandler:
    def __init__(self):
        self.verifier = UserVerifier()

    def show_menu(self):
        while True:
            print("----------------------------------------\n" 
            "Ingrese una opcion: " \
                "\n- Crear usuario" \
                "\n- Ingresar con usuario existente" \
                "\n- Salir")
            user_input = input('').lower()

            if 'crear' in user_input:
                self.create_user()
            elif 'ingresar' in user_input:
                self.login()
            elif 'salir' in user_input:
                print('\nAdios!')
                break
            else:
                print('Ingreso incorrecto\n')

    def create_user(self): 
        while True: 
            try:
                user = input('\nIngrese un usuario: ')
                self.verifier.valid_entry(user)

                password = pwinput.pwinput('Ingrese su contraseña: ') 
                self.verifier.valid_entry(password)

                pwd_confirm = pwinput.pwinput('Ingrese su contraseña nuevamente: ')
                self.verifier.pwd_match(password,pwd_confirm)
                
                self.verifier.create_user(user,password)
                print('Usuario y cuenta en ARS creados correctamente, volviendo al menu...\n') 
                return
            
            except ValueError as e:
                print(f"Error: {e}")
                user_input = input('\nQueres intentar de nuevo? si/no\n').strip().lower()
                if 'si' not in user_input:
                    print('\nVolviendo al menu\n')
                    return 
                
    
    def login(self):
        while True:
            try:
                user = input('\nIngrese su usuario: ')
                password = pwinput.pwinput('Ingrese la contraseña: ')
                self.verifier.verificar_login(user,password)
                print('Bienvenido!')
                accHandler = AccHandler(user)
                accHandler.show_menu()
                break
            except ValueError as e:
                print(f"Error: {e}")
                user_input = input('\nQueres intentar de nuevo? si/no\n').strip().lower()
                if 'si' not in user_input:
                    print('\nVolviendo al menu\n')
                    return