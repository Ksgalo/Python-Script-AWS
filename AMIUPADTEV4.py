import boto3

client = boto3.client('elasticbeanstalk')

environment_name = 'nombre_del_entorno'

while True:
    response = client.describe_environments(EnvironmentNames=[environment_name])
    status = response['Environments'][0]['Status']

    if status == 'Ready':
        break

    print(f"Esperando a que el entorno de Elastic Beanstalk {environment_name} esté disponible. Estado actual: {status}")

# El entorno está ahora en estado Ready, puede proceder con la actualización
