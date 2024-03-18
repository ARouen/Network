#pushes a running config from nornir inventory yaml file



from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_results



startkey = InitNornir(config_file="config.yaml")

#task.host in square brackets can parse through running config to whatever sub-config you want, i.e. ospf config
def push_config(task):
    task.run(task=send_config, config=f'running config {task.host['running_config']}')

results = startkey.run(task-push_config)
print_results(results)

