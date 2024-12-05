# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:51:56 2024

@author: manu9
"""

import subprocess

def ejecutar_comando(comando):
    """
    Ejecuta un comando en la terminal y captura errores si ocurren.
    """
    try:
        resultado = subprocess.run(comando, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(resultado.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {' '.join(comando)}")
        print(e.stderr)
        return False

def git_add():
    """
    Realiza 'git add .' para agregar todos los cambios.
    """
    comando = ["git", "add", "."]
    print(f"Ejecutando: {' '.join(comando)}")
    return ejecutar_comando(comando)

def git_commit(mensaje):
    """
    Realiza 'git commit -m "mensaje"' para confirmar los cambios.
    """
    comando = ["git", "commit", "-m", mensaje]
    print(f"Ejecutando: {' '.join(comando)}")
    return ejecutar_comando(comando)

def git_push(rama):
    """
    Realiza 'git push origin rama' para subir los cambios a la rama remota.
    """
    comando = ["git", "push", "origin", rama]
    print(f"Ejecutando: {' '.join(comando)}")
    return ejecutar_comando(comando)

def git_tag(tag_name):
    """
    Crea un tag en el repositorio local con el nombre especificado.
    """
    comando = ["git", "tag", tag_name]
    print(f"Ejecutando: {' '.join(comando)}")
    return ejecutar_comando(comando)

def git_push_tag(tag_name):
    """
    Realiza 'git push origin tag_name' para subir un tag al repositorio remoto.
    """
    comando = ["git", "push", "origin", tag_name]
    print(f"Ejecutando: {' '.join(comando)}")
    return ejecutar_comando(comando)

def main(mensaje_commit, rama, tag_name=None):
    """
    Realiza add, commit, push y opcionalmente crea y sube un tag.

    Args:
        mensaje_commit (str): Mensaje para el commit.
        rama (str): Nombre de la rama remota a la que se enviarán los cambios.
        tag_name (str, optional): Nombre del tag a crear y subir. Si es None, no se crea tag.
    """
    # Secuencia de comandos Git
    if not git_add():
        print("Error al ejecutar 'git add'.")
        return False

    if not git_commit(mensaje_commit):
        print("Error al ejecutar 'git commit'.")
        return False

    if not git_push(rama):
        print("Error al ejecutar 'git push'.")
        return False

    if tag_name:
        if not git_tag(tag_name):
            print("Error al crear el tag.")
            return False
        if not git_push_tag(tag_name):
            print("Error al subir el tag.")
            return False

    print("Cambios subidos con éxito a la rama:", rama)
    if tag_name:
        print("Tag subido con éxito:", tag_name)
    return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Uso: python script.py 'mensaje de commit' 'nombre_de_la_rama' [tag]")
        sys.exit(1)

    mensaje_commit = sys.argv[1]
    rama = sys.argv[2]
    tag_name = sys.argv[3] if len(sys.argv) > 3 else None

    main(mensaje_commit, rama, tag_name)
