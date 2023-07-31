#! _*_ encoding: utf-8 _*_
from colors import *
import hashlib,base64,ssl,socket,datetime,os
import requests,concurrent.futures,time
import pyshorteners as ps
import platform as pl

sh = os.system

def clear():
    if "indow" in pl.platform():
        sh("cls")
    else:
        sh("clear")
def banner():
    print(f"""{O}
                                     __ __       __    
 .-----.--.--.-----.-----.-----.----|  |__.-----|  |--.
 |-- __|  |  |  _  |  _  |  -__|   _|  |  |     |    < 
 |_____|_____|   __|   __|_____|__| |__|__|__|__|__|__|
             |__|  |__|                                
                        {W}Author: https://github.com/mrx04programmer
{W}""")

def short(long_url):
    short_url = ps.Shortener().tinyurl.short(long_url)
    return str(short_url)

def change_website(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a {url}: {e}")
        return None

def run_test_web(target_url, num_usuarios=1):
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_usuarios) as executor:
        futures = {executor.submit(change_website, target_url): i for i in range(num_usuarios)}

        for future in concurrent.futures.as_completed(futures):
            user_id = futures[future]
            try:
                status_code = future.result()
                print(f"{P} Testeo exitosamente completo del usuario {O}{user_id}")
            except Exception as e:
                print(f"Usuario {user_id} - Error: {e}")

    elapsed_time = time.time() - start_time
    print(f"{G}[+] Pruebas de rendimiento finalizadas en {O}{elapsed_time:.2f} {G}segundos.")


def main():
    print(f"""
{O}¿Qué desea hacer con la URL? {P}Ctrl+c para salir

{W}[{G}1{W}] {R}Acortar URL
{W}[{G}2{W}] {R}Probar rendimiento web""")
    op = int(input(f"{C}>>> {W}"))
    url = input(f"{C}URL>>> {G}")
    if op == 1:
        c = []
        clear()
        banner()
        s = short(url)
        print(f"{G}[+] URL NUEVA {P}{s}")
    elif op == 2:
        num_users = int(input(f"{C}Cuantos usuarios desea emular? {W}"))
        clear()
        banner()
        run_test_web(url, num_users)
    else:
        
        print(f"{R}- {W}URL no valida.")
        exit()

if __name__ == '__main__':
    try:
        clear()
        banner()
        main()
    except KeyboardInterrupt:
        print(f"{R}Bye bye.")
    except Exception as e:
        print(f"{R}ERR {W}Causado por {O}{e}")