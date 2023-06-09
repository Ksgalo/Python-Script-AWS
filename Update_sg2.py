import boto3
from botocore.exceptions import ProfileNotFound, ClientError

def add_security_group_rules(security_group_ids, rules):
    try:
        session = boto3.Session(profile_name='prod', region_name='us-east-1')
        ec2 = session.resource('ec2')

        for sg_id in security_group_ids:
            security_group = ec2.SecurityGroup(sg_id)

            for rule in rules:
                ip_protocol = rule['IpProtocol']
                from_port = rule['FromPort']
                to_port = rule['ToPort']
                ip_ranges = rule['IpRanges']
                try:
                    security_group.authorize_ingress(
                        IpPermissions=[
                                {
                                    'FromPort': from_port,
                                    'IpProtocol': ip_protocol,
                                    'IpRanges': ip_ranges,
                                    'ToPort': to_port,
                                }
                            ]
                        )
                except ClientError as e:
                    if e.response['Error']['Code'] == 'InvalidPermission.Duplicate':
                        print(f"La regla de seguridad ya existe en el grupo {sg_id}. Ignorando el error.")
                    else:
                        raise e
    except ProfileNotFound:
        print("El perfil 'prod' no se encontró en el archivo de credenciales de AWS.")

# Lista de IDs de grupos de seguridad en AWS EC2
security_group_ids = [
'sg-0c212adce34d7c977'


]
# Reglas específicas de entrada que deseas agregar
rules = [
    {
        'FromPort': 22,
        'IpProtocol': 'tcp',
        'IpRanges': [
            {
                'CidrIp': '192.168.242.0/23',
                'Description': 'Usuarios VPN Puntos Colombia firewallvpn_1',
            },
            {
                'CidrIp': '192.168.244.0/23',
                'Description': 'Usuarios VPN Puntos Colombia firewallvpn_2',
            }
        ],
        'ToPort': 22,
    }
]

# Llamar a la función para agregar las reglas de seguridad
add_security_group_rules(security_group_ids, rules)
