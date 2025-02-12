def find_children(santas_list, children):
    return sorted(child_name for child_name in children if child_name in santas_list)
