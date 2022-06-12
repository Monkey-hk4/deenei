import requests
from colorama import Fore,init
init()
### colores
v = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
b = Fore.LIGHTWHITE_EX
a = Fore.LIGHTBLUE_EX
reset = Fore.RESET

def consulta_individual():
    ndni = input("Escribe el número de dni: ")
    url = "http://webexterno.sutran.gob.pe/WebExterno/Pages/SolicitudAIP/TramiteGeneral.aspx/consulta_persona2"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Content-Type': 'application/json',
        'Referer': 'https://webexterno.sutran.gob.pe/WebExterno/Pages/SolicitudAIP/TramiteGeneral.aspx?TW=S'
    }
    payload = {"num_doc": ndni,"tipo_doc":"2"}
    respuesta = requests.post(url, headers=headers, json=payload)
    re = respuesta.json()
    if 'RazonSocial' in respuesta.text:
        nombre = re['d']['data']['RazonSocial']
        direccion = re['d']['data']['Direccion']
        depa = re['d']['data']['Departamento']
        provin = re['d']['data']['Provincia']
        distrito = re['d']['data']['Distrito']
        print(f"{v}NOMBRE: {b}{nombre}\n{v}DIRECCION: {b}{direccion}\n{v}DEPARTAMENTO: {b}{depa}\n{v}PROVINCIA: {b}{provin}\n{v}DISTRITO: {b}{distrito}\n")
    else:
        print(f"{r}NO SE ENCONTRO INFORMACION DEL NUMERO DE DNI {ndni}{reset}")
    men_opciones()

def consulta_masiva():
    lista_usuarios = input("Ruta del archivo .txt con los dni´s: ")
    with open(lista_usuarios) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
        ndni = line.strip()
        url = "http://webexterno.sutran.gob.pe/WebExterno/Pages/SolicitudAIP/TramiteGeneral.aspx/consulta_persona2"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
            'Content-Type': 'application/json',
            'Referer': 'https://webexterno.sutran.gob.pe/WebExterno/Pages/SolicitudAIP/TramiteGeneral.aspx?TW=S'
        }
        payload = {"num_doc": ndni,"tipo_doc":"2"}
        respuesta = requests.post(url, headers=headers, json=payload)
        re = respuesta.json()
        if 'RazonSocial' in respuesta.text:
            nombre = re['d']['data']['RazonSocial']
            direccion = re['d']['data']['Direccion']
            depa = re['d']['data']['Departamento']
            provin = re['d']['data']['Provincia']
            distrito = re['d']['data']['Distrito']
            print(f"[+] {v}NOMBRE: {b}{nombre}| {v}DIRECCION: {b}{direccion}|{v}DEPARTAMENTO: {b}{depa}| {v}PROVINCIA: {b}{provin}| {v}DISTRITO: {b}{distrito}")
            pass
        else:
            print(f"{r}NO SE ENCONTRO INFORMACION DEL NUMERO DE DNI {ndni}{reset}")
            pass
    men_opciones()


def dibujito():
    print(f"""{b}
{a}      _       _ 
{a}   __| |_ __ (_)
{a}  / _` | '_ \| | {v}MHK4.
{a} | (_| | | | | | {r}====================
{a}  \__,_|_| |_|_| {b}& dirección de casa. 

 [ 1 ] - CONSULTA DNI INDIVIDUAL.
 [ 2 ] - CONSULTA DNI MASIVOS.
 [ 3 ] - SALIR.
    """)
def men_opciones():
    opcion = input("[>>]: ")
    if opcion == "1":
        consulta_individual()
    elif opcion == "2":
        consulta_masiva()
    elif opcion == "3":
        exit()
    else:
        print(f"{r}OPCION INVALIDA.")

if __name__ == "__main__":
    dibujito()
    men_opciones()