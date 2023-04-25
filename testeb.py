import boto3
from nombres import *



#Itera sobre cada cliente y cada beastalk de la cuenta
for cnt in range(len(beanstalks)):
    init = beanstalks[cnt]
    for count in range(len(clientes)):
        session = boto3.session.Session(profile_name="CT_DEV", region_name="us-east-1")
        bean_cli = session.client(service_name="elasticbeanstalk", region_name="us-east-1")
        
        # Obtiene el estado actual del entorno del beanstalk
        response = bean_cli.describe_environments(EnvironmentNames=[init])
        status = response['Environments'][0]['Status']
        
        # Espera hasta que el estado sea ready
        while status != 'Ready':
            response = bean_cli.describe_environments(EnvironmentNames=[init])
            status = response['Environments'][0]['Status']
            print(f"Esperando a que el entorno de Elastic Beanstalk {init} esté disponible. Estado actual: {status}")
            #time.sleep(60)  # Espera 60 segundos antes de verificar nuevamente
            
        try:
            # Actualiza el entorno de Elastic Beanstalk con el nuevo SolutionStackName
            bean_dict = bean_cli.update_environment(EnvironmentName=init, SolutionStackName=Value)
            print('Update Exitoso:',init,'---',Value)
            
            # Espera hasta que el estado sea 'Ready' nuevamente
            status = response['Environments'][0]['Status']
            while status != 'Ready':
                response = bean_cli.describe_environments(EnvironmentNames=[init])
                status = response['Environments'][0]['Status']
                print(f"Esperando a que el entorno de Elastic Beanstalk {init} esté disponible después del primer cambio. Estado actual: {status}")
                #time.sleep(60)  # Espera 60 segundos antes de verificar nuevamente
                
            # Actualiza el entorno de Elastic Beanstalk con la nueva AMI
            bean_dict = bean_cli.update_environment(EnvironmentName=init, OptionSettings=[{'Namespace': namespace, 'OptionName': optioname, 'Value': AMI}])
            print('Update Exitoso:',init,'---',AMI)
        except Exception as e:
         print('Error:', e)    
            

