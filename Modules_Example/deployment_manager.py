deployments = []

def deploy_application(app_name, version):
    deployments.append((app_name, version))
    print(f"Deploying {app_name} version {version}... Done!")

def rollback_application(app_name, version):
    if(app_name, version) in deployments:
        deployments.remove((app_name, version))
        print(f"Rolled back {app_name} version {version}")


def list_deployments():
    print("Deployments")
    for app_name, version in deployments:
        print(f"- {app_name} version {version}")