import yaml

services = {}


class NoKeyWordException(Exception): pass


def raise_exception(service_name, field_name):
    raise NoKeyWordException('%s: %s not config.' % (service_name, field_name))


class GitConfig:
    def __init__(self, service_name, git_map):
        check_fields = ['git_url', 'git_user', 'git_password', 'jar_path', 'branch']

        for field in check_fields:
            if field not in git_map:
                raise_exception(service_name, field)

        self.git_url = git_map['git_url']
        self.git_user = git_map['git_user']
        self.git_password = git_map['git_password']
        self.jar_path = git_map['jar_path']
        self.jar_path = git_map['branch']


class MachineConfig:
    def __init__(self, service_name, default_map):
        self.deploy_path = default_map.get('deploy_path', None)
        self.machine_user = default_map.get('machine_user', None)
        self.machine_password = default_map.get('machine_password', None)
        self.params = default_map.get('params', None)


class TargetConfig:
    def __init__(self, service_name, target_map, machine_config):
        check_fields = ['ip', 'port']

        for field in check_fields:
            if field not in target_map:
                raise_exception(service_name, field)

        self.ip = target_map['ip']
        self.port = target_map['port']
        self.params = target_map.get('params', [])

        self.machine_user = target_map.get('machine_user', machine_config.machine_user)
        self.machine_password = target_map.get('machine_password', machine_config.machine_password)
        self.deploy_path = target_map.get('deploy_path', machine_config.deploy_path)

        if self.machine_user is None:
            raise_exception(service_name, 'machine_user')

        if self.machine_password is None:
            raise_exception(service_name, 'machine_password')

        if self.deploy_path is None:
            raise_exception(service_name, 'deploy_path')


class ServiceConfig:
    def __init__(self, service_name, service_map):
        if service_name is None:
            raise NoKeyWordException("no service_name in services.")

        self.service_name = service_name

        machine_map = service_map.get('machine', {})
        git_map = service_map.get('git', {})
        target_maps = service_map.get('targets', [])

        machine_config = MachineConfig(service_name, machine_map)

        self.git_config = GitConfig(service_name, git_map)
        self.targets_config = []

        for target_map in target_maps:
            self.targets_config.append(TargetConfig(service_name, target_map, machine_config))


with open('configs.yml') as file:
    yaml_configs = yaml.load(file, Loader=yaml.FullLoader)
    configs = yaml_configs['configs']

    if 'services' not in configs:
        raise NoKeyWordException('services config is missing.')

    service_maps = configs.get('services', [])
    for service_map in service_maps:
        if 'service_name' not in service_map:
            raise NoKeyWordException('service_name config is missing.')
        service_name = service_map.get('service_name')
        services[service_name] = ServiceConfig(service_name, service_map)
