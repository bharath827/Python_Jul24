services ={
    "webserver" : "stopped",
    "database" : "stopped"
}


def start_service(service_name):
    if service_name in services:
        services[service_name] = "running"
        return f"{service_name} started"
    else:
        return f"Service {service_name} not found"


def stop_service(service_name):
    if service_name in services:
        services[service_name] = "stopped"
        return f"{service_name} stopped"
    else:
        return f"Service {service_name} not found"

def get_status(service_name):
    return services.get(service_name, "Service  not  found")

def list_services():
    print("Service Statuses")
    for service, status in services.items():
        print(f"- {service} : {status}")