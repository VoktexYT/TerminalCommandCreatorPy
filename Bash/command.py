"""

The command.py file is user to build the command whit decorator

"""

# all the commands will to store here
all_command_dict = {}


class Command:
    def add(self, *, only_one_value: type = None, only_one_param: str = '', **value):
        def inner(fn):
            def wrapper():
                if not only_one_value and not only_one_param:
                    new_value = {}
                    for x in value:
                        new_value['-'+x] = value[x]
                    all_command_dict[fn.__name__] = {'param': new_value, 'code': fn}
                else:
                    if only_one_param:
                        all_command_dict[fn.__name__] = {'result': f'-{only_one_param}', 'code': fn}
                    else:
                        all_command_dict[fn.__name__] = {'result': only_one_value, 'code': fn}
            return wrapper()
        return inner

    # developer zone: just a reminder
    def Doc(self):
        return {
            'param_dash': "add dash in keyword => 'rm -r project' if not activate => 'rm r project'",
            'only_one_value': "put just a value => 'mkdir project'",
            'only_one_param': "put just a param => 'node -v'",
            '**value': "add param to use with a type => '-m 'hello world'' == "
        }
