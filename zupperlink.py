#! _*_ encoding: utf-8 _*_
from colors import *
import hashlib,base64,ssl,socket,datetime,os
import requests,concurrent.futures,time
import pyshorteners as ps
import platform as pl
import ssl, socket

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

def verify_ssl(host):
    context = ssl.create_default_context()
    with socket.create_connection((host, 443)) as sock: 
        with context.wrap_socket(sock, server_hostname=host) as ssl_sock:
            # obtain certification
            cert = ssl_sock.getpeercert()
            cert_expired = datetime.datetime.utcnow() > datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            if cert_expired:
                print(f"{R}[STATUS] {W}El certificado ha caducado.")
                return False
            else:
                print(f"{G}[STATUS] {W}El certificado no ha caducado.")

            """ for algo in cert:
                print(cert[algo]) """
            for algo in cert:
                if algo == "version":
                    print(f"{B}[DATA] Versión SSL {P}{cert[algo]}")
                elif algo == "notBefore":
                    print(f"{B}[DATA] Fecha de inicio del certificado {W}[{P}{cert[algo]}{W}]")
                elif algo == "notAfter":
                    print(f"{B}[DATA] Fecha de fin del certificado {W}[{P}{cert[algo]}{W}]")
                elif algo == "subject":
                    for subdata in cert[algo]:
                        for subdatadata in subdata:
                            print(f"{G}[SUBDATA] {O}DOMAINDATA {W}{subdatadata}")
                elif algo == "issuer":
                    for subdata in cert[algo]:
                            for subdatadata in subdata:
                                print(f"{G}[SUBDATA] {O}BUNISSESDATA {W}{subdatadata}")
                
                elif algo == "subjectAltName":
                    for subdata in cert[algo]:
                        for subdatadata in subdata:
                            print(f"{G}[SUBDATA] {O}DOMAINDATA {W}{subdatadata}")
                elif algo == "crDistributionPoints":
                    for subdata in cert[algo]:
                        for subdatadata in subdata:
                            print(f"{G}[SUBDATA] {O}DISTRIBUTIONS {subdatadata}")


            # encryption algorithms used in the SSL/TLS connection
            cipher_name, cipher_version, cipher_bits = ssl_sock.cipher()
            print(f"{G}[INFO] {W}Algoritmo de cifrado SSL/TLS: {P}{cipher_name} ({cipher_bits} bits)")
            return True

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
{W}[{G}2{W}] {R}Probar rendimiento web
{W}[{G}3{W}] {R}Verificar Seguridad SSL""")
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
    elif op == 3:
        verify_ssl(url)
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