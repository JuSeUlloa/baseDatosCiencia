# Instructivo primera clase de Bases de datos
- Juan Sebastian Ulloa Parra 

## Objetivo
Este instructivo tiene como objetivo guiar a los estudiantes en la instalación y configuración de las herramientas necesarias para la primera clase de la asignatura de Bases de Datos.

### 1. Instalación de Vscode
![Imagen de Vscode](https://code.visualstudio.com/assets/images/code-stable.png)     
Visual Studio Code (Vscode) es un editor de código fuente desarrollado por Microsoft. en la siguiente url se encuentra el instalador para su sistema operativo:
- [Descargar Vscode](https://code.visualstudio.com/)
### 2. Instalación de Git (Control de versiones)
![Imagen de Git](https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png)
Git es un sistema de control de versiones distribuido que permite a los desarrolladores gestionar y realizar un seguimiento de los cambios en el código fuente a lo largo del tiempo. Para instalar Git, visite la siguiente URL y siga las instrucciones según su sistema operativo:
- [Descargar Git](https://git-scm.com/)
### 3. Configuración de Git
Después de instalar Git, es importante configurarlo con su nombre de usuario y correo electrónico. Abra la terminal o línea de comandos y ejecute los siguientes comandos, reemplazando "Tu Nombre" y "tu_correo@example.com" con su información:
- comando para configurar el nombre de usuario:
  ```
  git config --global user.name "Tu Nombre"
  ```
- comando para configurar el correo electrónico:
  ```
  git config --global user.email "tu_correo@example.com"
  ```

 ### 3.1.1 Generacion de primer commit
 Una vez configurado Git, puede crear un nuevo repositorio y realizar su primer commit. Siga estos pasos:
 1. Cree un nuevo directorio para su proyecto y navegue hasta él:
    ```
    mkdir mi_proyecto
    cd mi_proyecto
    ```
 2. Inicialice un nuevo repositorio Git:
    ```
    git init
    ```
 3. Cree un archivo README.md (opcional): 
    

 4. Generar el primer commit:
    ```
    git add .
    git commit -m "Primer commit"
    ```
5. publicar el repositorio en GitHub (opcional):
   - Cree un nuevo repositorio en GitHub.
   - Siga las instrucciones proporcionadas por GitHub para conectar su repositorio local con el remoto y subir sus cambios.
