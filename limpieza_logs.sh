#!/bin/bash

LOG_DIR="$HOME/environment/devops-proyecto-aws/logs"
REPORTE="$HOME/environment/devops-proyecto-aws/limpieza_logs_reporte.txt"

mkdir -p "$LOG_DIR"

echo "Inicio de limpieza de logs: $(date)" >> "$REPORTE"

find "$LOG_DIR" -type f -name "*.log" -mtime +7 -exec rm -f {} \;

echo "Limpieza completada: $(date)" >> "$REPORTE"
echo "--------------------------------------" >> "$REPORTE"
