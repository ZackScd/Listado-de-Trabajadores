Para la correcta ejecución del código se requiere una serie de pasos necesarios para el funcionamiento de la aplicación, concretamente su conexión a la base de datos. 

Como primer requisito, se requiere la instalación del conjunto de soluciones de WampServer. Se puede adquirir gratuitamente desde la siguiente URL: 

https://wampserver.aviatechno.net/

Es posible que sea necesaria la instalación de los paquetes de Visual C++ si no se encuentran instalados en el equipo. Pueden adquirirse desde misma página de WampServer, en el apartado "VC++ Packages"


-----------------------------------------------------------------------------------------------



Una vez que WampServer se encuentre instalado en el equipo en donde se ejecutará el programa, se deberá realizar el proceso de creación y configuración de la base de datos. 

La serie de pasos necesaria es la siguiente: 

- Acceder a la siguiente URL: http://localhost/phpmyadmin/

- Rellenar los datos de ingreso: 
	- Usuario = root
	- Contraseña en blanco
	- Servidor = MySQL

- Acceder al editor de sentencias SQL en el menú superior de la página. Copiar todo el texto del archivo "trabajadores.sql" y pegarlo en la hoja, luego ejecutar. 
(si este paso arroja error, se deben borrar los comentarios del texto copiado [Comienzan con "--"])


-----------------------------------------------------------------------------------------------


Para asegurarse de que la aplicación funcione correctamente, se debe ejecutar el archivo "conexión.py"

- Si la respuesta es "code=0", la aplicación conecta correctamente. 

En caso de que la ejecución cause un error, es posible que se deba instalar la librería de mysql.connector. 
Para realizar la instalación, se debe ejecutar el siguiente comando en la terminal.

- pip install mysql-connector-python


-----------------------------------------------------------------------------------------------


Luego de la realización de todos estos pasos, la aplicación debería funcionar correctamente. 
El archivo "login.py" se trata de la aplicación principal.































