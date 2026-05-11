#!/bin/bash

USUARIO="devops_user"

echo "Creando usuario $USUARIO..."

if id "$USUARIO" &>/dev/null; then
    echo "El usuario $USUARIO ya existe."
else
    sudo useradd -m "$USUARIO"
    echo "Usuario $USUARIO creado correctamente."
fi

echo "Asignando permisos sobre el directorio del proyecto..."
sudo chown -R "$USUARIO":"$USUARIO" ~/environment

echo "Agregando usuario al grupo docker..."
sudo usermod -aG docker "$USUARIO"

echo "Restaurando permisos para ec2-user en Cloud9..."
sudo chown -R ec2-user:ec2-user ~/environment

echo "Gestión de usuarios completada."
