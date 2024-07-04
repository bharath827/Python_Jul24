# import service_manager
#
# print(service_manager.start_service("webserver")) #webserver started
# print(service_manager.get_status("webserver")) #running
# print(service_manager.stop_service("webserver")) #webserver stopped
# print(service_manager.get_status("webserver")) #stopped


import service_manager
import deployment_manager
import monitor_manager

#Manage Services
service_manager.start_service("webserver")
service_manager.stop_service("database")
service_manager.list_services()


#Deploy and Rollback application

deployment_manager.deploy_application("MyApp", "1.0.0")
deployment_manager.deploy_application("MyApp", "1.0.0")
deployment_manager.list_deployments()

deployment_manager.rollback_application("MyApp", "1.0.0")


#Monitor system resources

monitor_manager.display_resources()