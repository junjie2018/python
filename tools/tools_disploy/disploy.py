import yaml


# import paramiko
#
#
#
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('120.78.168.136', 22, 'root', 'PC+1111222', timeout=10)
# stdin, stdout, stderr = ssh.exec_command("ls")
# print(stdout.read())


class NoKeyWordException(Exception): pass


class DefaultConfig:
    def __init__(self, default_map):
        self.machine_user = default_map.get('machine_user', None)
        self.machine_password = default_map.get('machine_password', None)
        self.git_user = default_map.get('git_user', None)
        self.git_password = default_map.get('git_password', None)


class ServiceDefaultConfig:
    def __init__(self, service_default_map, default_config):
        self.git_user = default_map.get('git_user', default_config.git_user)
        self.git_password = default_map.get('git_password', default_config.git_password)
        self.machine_user = service_map.get('machine_user', default_config.machine_user)
        self.machine_password = service_map.get('machine_user', default_config.machine_password)

        self.jar_path = service_default_map.get('jar_path', default_config.jar_path)
        self.params = service_map.get('params', [])


class TargetConfig:


class ServiceConfig:
    def __init__(self, service_map, default_config):
        if 'target' not in service_map:
            raise NoKeyWordException('%s: target not config.' % service_map.get('service_map'))

        service_default_map = service_map.get('default', {})
        service_default_config = DefaultConfig(service_default_map)

        target_maps = service_map.get('targets')

        self.service_name = service_map.get('service_map')
        self.git_url = service_map.get('git_url', None)
        self.targets =

        ServiceConfig.check_field(self)

    def check_field(self):
        print([item for item in self.__dict__ if item.startswith('__')])


class TargetConfig:
    def __init__(self, target_map, default_config, service_default_config):
        if 'ip' not in target_map:
            raise NoKeyWordException('ip config is missing.')
        self.ip = target_map['ip']

        self.user = target_map.get('user', default_config.machine_user)
        self.password = target_map.get('password', default_config.machine_password)
        self.params = target_map.get('params', [])


services = {}

with open('configs.yml') as file:
    yaml_configs = yaml.load(file, Loader=yaml.FullLoader)
    configs = yaml_configs['configs']

    if 'services' not in configs:
        raise NoKeyWordException('services config is missing.')

    # 转换为default_config
    default_map = configs.get('default', {})
    default_config = DefaultConfig(default_map)

    service_maps = configs.get('services', [])

    for service_map in service_maps:
        if 'service_name' not in service_map:
            raise NoKeyWordException('service_name config is missing.')
        services[service_map.get('service_name')] = ServiceConfig(service_map, default_config)

print("")
