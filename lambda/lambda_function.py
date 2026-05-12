import json
import random

def lambda_handler(event, context):
    mensajes = [
        "Despliegue automatizado completado correctamente.",
        "Microservicio DevOps ejecutandose en AWS Lambda.",
        "Monitoreo y automatizacion activos en la nube.",
        "Pipeline CI/CD integrado con GitHub Actions.",
        "Proyecto DevOps funcionando correctamente."
    ]

    respuesta = {
        "mensaje": random.choice(mensajes),
        "servicio": "microservicio-devops"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(respuesta)
    }
