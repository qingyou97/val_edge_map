items = ["hazelnut_hole", "hazelnut_print", "leather_color", "leather_cut", "leather_fold", "leather_glue", "leather_poke", "metal_nut_bent", "metal_nut_color", "metal_nut_flip"]

for item in items:
    exec(f"{item}_recall_list = []")

# 验证一下是否创建了这些列表
print(hazelnut_hole_recall_list)
print(leather_color_recall_list)
print(metal_nut_color_recall_list)
