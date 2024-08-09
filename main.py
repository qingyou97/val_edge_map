import ast
import astor

def update_cfg(filename, new_data_root, new_data_lst):
    # 读取文件内容
    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # 将内容转换为AST（抽象语法树）
    tree = ast.parse(file_content)
    
    # 遍历AST，修改指定内容
    class ConfigTransformer(ast.NodeTransformer):
        def visit_Dict(self, node):
            new_keys = []
            new_values = []
            for key, value in zip(node.keys, node.values):
                if isinstance(key, ast.Constant) and key.value == 'bsds500':
                    if isinstance(value, ast.Dict):
                        for k, v in zip(value.keys, value.values):
                            if isinstance(k, ast.Constant) and k.value == 'data_root':
                                v = ast.Constant(value=new_data_root)
                            if isinstance(k, ast.Constant) and k.value == 'data_lst':
                                v = ast.Constant(value=new_data_lst)
                            new_keys.append(k)
                            new_values.append(v)
                        value.keys = new_keys
                        value.values = new_values
                else:
                    new_keys.append(key)
                    new_values.append(value)

            node.keys = new_keys
            node.values = new_values
            return node

    transformer = ConfigTransformer()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    
    # 将新的AST转回Python代码
    new_content = astor.to_source(new_tree)
    
    # 保存回原文件
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 调用更新函数
update_cfg('cfg.py', './new_data_root/', 'new_image_lst.lst')
