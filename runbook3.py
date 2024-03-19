from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_command_test():
    task.run(task=send_commands_from_file, file= '/path/to/file')

results = nr.run(task=show_commands-from_file)
print_results(results)
