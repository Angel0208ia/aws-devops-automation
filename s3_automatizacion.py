import boto3
from datetime import datetime

REGION = "us-east-1"

s3 = boto3.client("s3", region_name=REGION)
sts = boto3.client("sts", region_name=REGION)

account_id = sts.get_caller_identity()["Account"]
bucket_name = f"devops-bucket-{account_id}"

archivo_local = "archivo_prueba_s3.txt"
objeto_s3 = "pruebas/archivo_prueba_s3.txt"


def crear_archivo_prueba():
    with open(archivo_local, "w", encoding="utf-8") as archivo:
        archivo.write("Archivo de prueba para automatizacion S3 con boto3.\n")
        archivo.write(f"Fecha de creacion: {datetime.now()}\n")

    print(f"Archivo local creado: {archivo_local}")


def subir_archivo():
    s3.upload_file(archivo_local, bucket_name, objeto_s3)
    print(f"Archivo subido correctamente a s3://{bucket_name}/{objeto_s3}")


def listar_objetos():
    print(f"\nObjetos dentro del bucket: {bucket_name}")

    response = s3.list_objects_v2(Bucket=bucket_name)

    if "Contents" not in response:
        print("El bucket no contiene objetos.")
        return

    for obj in response["Contents"]:
        print(
            f"Nombre: {obj['Key']} | "
            f"Tamaño: {obj['Size']} bytes | "
            f"Modificado: {obj['LastModified']}"
        )


if __name__ == "__main__":
    print("Automatizacion de S3 con boto3")
    print(f"Bucket utilizado: {bucket_name}")

    crear_archivo_prueba()
    subir_archivo()
    listar_objetos()

    print("\nProceso S3 finalizado correctamente.")
