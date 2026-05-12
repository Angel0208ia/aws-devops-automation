import boto3
from botocore.exceptions import ClientError

REGION = "us-east-1"
TABLE_NAME = "devops-tabla"

dynamodb = boto3.resource("dynamodb", region_name=REGION)
client = boto3.client("dynamodb", region_name=REGION)


def crear_tabla():
    try:
        table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    "AttributeName": "id",
                    "KeyType": "HASH"
                }
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "id",
                    "AttributeType": "S"
                }
            ],
            BillingMode="PAY_PER_REQUEST"
        )

        print(f"Creando tabla {TABLE_NAME}...")
        table.wait_until_exists()
        print(f"Tabla {TABLE_NAME} creada correctamente.")

    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceInUseException":
            print(f"La tabla {TABLE_NAME} ya existe.")
        else:
            raise


def insertar_registro():
    table = dynamodb.Table(TABLE_NAME)

    table.put_item(
        Item={
            "id": "001",
            "nombre": "registro-devops",
            "status": "creado"
        }
    )

    print("Registro insertado correctamente.")


def actualizar_registro():
    table = dynamodb.Table(TABLE_NAME)

    table.update_item(
        Key={
            "id": "001"
        },
        UpdateExpression="SET #st = :nuevo_status",
        ExpressionAttributeNames={
            "#st": "status"
        },
        ExpressionAttributeValues={
            ":nuevo_status": "actualizado"
        }
    )

    print("Registro actualizado correctamente.")


def consultar_registro():
    table = dynamodb.Table(TABLE_NAME)

    response = table.get_item(
        Key={
            "id": "001"
        }
    )

    item = response.get("Item")

    if item:
        print(f"Registro consultado: {item}")
    else:
        print("No se encontró el registro.")


def eliminar_registro():
    table = dynamodb.Table(TABLE_NAME)

    table.delete_item(
        Key={
            "id": "001"
        }
    )

    print("Registro eliminado correctamente.")


if __name__ == "__main__":
    print("Operaciones DynamoDB con boto3")

    crear_tabla()
    insertar_registro()
    actualizar_registro()
    consultar_registro()
    eliminar_registro()

    print("\nProceso DynamoDB finalizado correctamente.")
