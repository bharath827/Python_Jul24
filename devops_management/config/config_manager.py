configurations = {
    "webserver" : {'host': "localhost", 'port' : 8080},
    "database" : {"host": "localhost", 'port' : 3306}
}


def get_config(service_name):
    return configurations.get(service_name, "configuration not found" )



def set_config(service_name, config):
    configurations[service_name] = config
    print(f"Configuration for {service_name} set to {config}")