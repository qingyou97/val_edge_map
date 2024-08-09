import ast

def load_config(path):
    with open(path, 'r', encoding='utf-8') as file:
        module = ast.parse(file.read())
    config_code = next(node for node in module.body if isinstance(node, ast.Assign) and node.targets[0].id == 'config')
    config_test_code = next(node for node in module.body if isinstance(node, ast.Assign) and node.targets[0].id == 'config_test')
    config = ast.literal_eval(config_code.value)
    config_test = ast.literal_eval(config_test_code.value)
    return config, config_test

def save_config(config, config_test, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write('config = {\
')
        for key, value in config.items():
            file.write(f"    {key!r}: {value!r},\
")
        file.write('}\
\
')

        file.write('config_test = {\
')
        for key, value in config_test.items():
            file.write(f"    {key!r}: {value!r},\
")
        file.write('}\
\
')

        file.write("if __name__ == '__main__':\
")
        file.write("    print(config.keys())\
")

def update_bsds500(config, new_data_root, new_data_lst):
    if 'bsds500' in config:
        config['bsds500']['data_root'] = new_data_root
        config['bsds500']['data_lst'] = new_data_lst
    else:
        print("bsds500 not found in config")

def update_cfg(cfg_path, new_data_root, new_data_lst):
    config, config_test = load_config(cfg_path)
    update_bsds500(config, new_data_root, new_data_lst)
    save_config(config, config_test, cfg_path)
    print('Config updated successfully.')
