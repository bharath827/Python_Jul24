# modules =>

#
# production => start, stop, rollback
# development =>  start, stop, rollback
# testing =>  start, stop, rollback


# list = [1,2,3,4,5]
#
# list.remove()

services = {
    "webserver" : "running",
    "database" : "stopped"
}

def check_status(service_name):
    return services.get(service_name, "Service is not found")

def list_services():
    return services


