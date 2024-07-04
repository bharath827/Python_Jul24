from config.config_manager import get_config, set_config
from loggers.logger import log
from status.status_checker import check_status, list_services



#config management

web_config = get_config("webserver")
log(f"webserver configuration: {web_config}")



new_db_config = {"host":"localhost", "port":5432}
set_config("database", new_db_config)


#status checking

web_status = check_status("webserver")
log(f"webserver status:{web_status}")

all_services = list_services()
log(f"All Services : {all_services}")