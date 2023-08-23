
## Descripción
ZupperLink es una herramienta de código abierto diseñada para acortar URLs y realizar pruebas de rendimiento en páginas web. Esta aplicación utiliza diversas librerías de Python para brindar una experiencia completa y funcional.
## Funcionalidades Principales
#### 1. Acortador de URLs
ZupperLink permite a los usuarios acortar URLs largas de manera rápida y sencilla. Al introducir una URL en la interfaz de usuario, la aplicación generará una versión acortada que puede ser compartida de forma más cómoda.
#### 2. Pruebas de Rendimiento Web
El proyecto ZupperLink también cuenta con una funcionalidad para realizar pruebas de rendimiento en páginas web. Utilizando la librería requests, la aplicación simula usuarios concurrentes que acceden al sitio web objetivo, permitiendo a los usuarios evaluar su rendimiento y tiempo de respuesta.

## Librerías de Python Utilizadas

    🔏 hashlib: Permite generar hashes únicos para acortar las URLs de forma segura.
    🔓 base64: Utilizado en la codificación de las URLs acortadas.
    ☢️ ssl: Proporciona funciones para trabajar con certificados SSL en las pruebas de rendimiento web.
    ⚡ socket: Empleado para realizar conexiones a través del protocolo SSL (puerto 443) en las pruebas de rendimiento web.
    🕑 datetime: Utilizado para obtener la fecha de vencimiento de los certificados SSL en las pruebas de rendimiento web.
    🖥️ os: Empleado para obtener información sobre el sistema operativo en el que se ejecuta la aplicación.
    🌐 requests: Utilizado para realizar solicitudes HTTP al acortar URLs y para simular usuarios en las pruebas de rendimiento web.
    🖐️ concurrent.futures: Utilizado para crear múltiples usuarios concurrentes en las pruebas de rendimiento web.
    🕰️ time: Empleado para medir el tiempo de ejecución de las pruebas de rendimiento web.
    🎟️ pyshorteners: Una biblioteca adicional para acortar URLs utilizando servicios como TinyURL, Bitly, etc.
    🖥️ platform: Utilizado para obtener información sobre la plataforma en la que se ejecuta la aplicación.
    🌐 socket: proporciona una interfaz para la creación de sockets y la conexión a servidores remotos utilizando diferentes protocolos de red, como TCP o UDP.
    ☀️ ssl: Esta librería permite establecer conexiones de red cifradas y autenticadas mediante el uso de certificados digitales, lo que garantiza la privacidad y la integridad de los datos transmitidos.

## Requisitos del Sistema
Para ejecutar ZupperLink, asegúrate de tener instalada una versión de Python compatible y todas las librerías mencionadas. Además, ten en cuenta que algunas funcionalidades pueden depender de servicios externos, por lo que asegúrate de contar con acceso a Internet.

## Instalar dependencias
Para la instalación de las dependencias se debe ejecutar el siguiente comando para las librerias con las cuales no cuenta instalada:

      $ python -m pip install <libreria no instalada>

Si no sabes con que librerias cuentas instaladas puedes ejecutar el siguiente comando:

      $ python -m pip install freeze
## Disponibilidad / Compatiblidad
<img src="https://img.shields.io/static/v1?style=for-the-badge&message=Android&color=222222&logo=Android&logoColor=3DDC84&label=">  <img src="https://img.shields.io/static/v1?style=for-the-badge&message=linux&color=222222&logo=linux&logoColor=yellow&label=">  <img src="https://img.shields.io/static/v1?style=for-the-badge&message=Windows&color=0078D4&logo=Windows&logoColor=FFFFFF&label=">  <img src="https://img.shields.io/static/v1?style=for-the-badge&message=macOS&color=000000&logo=macOS&logoColor=FFFFFF&label=">
