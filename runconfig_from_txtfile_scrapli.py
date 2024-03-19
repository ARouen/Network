from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_results

nr = initNornir(config_file='config.yaml')

def send_config_test(task):
    task.run(task=send_configs_from_file, file= '/path/to/file', dry_run=True)

results = nr.run(task=send_config_test)
print_results(results)
