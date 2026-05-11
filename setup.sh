#!/bin/bash

echo "Actualizando paquetes del sistema..."
sudo dnf update -y

echo "Instalando dependencias necesarias..."
sudo dnf install -y python3 python3-pip git docker vim cronie

echo "Instalando boto3..."
pip3 install boto3

echo "Iniciando servicio Docker..."
sudo service docker start

echo "Habilitando servicio cron..."
sudo systemctl enable crond
sudo systemctl start crond

echo "Verificando versiones instaladas..."
git --version
docker --version
python3 --version
pip3 show boto3

echo "Configuración inicial completada correctamente."
