#!/usr/bin/python3

import os
import result_tree

def main() -> None:
    result = result_tree.Tree()
    current_dir = './'
    #files_dir = os.listdir()
    root = os.walk(current_dir)

    for path, subdirs, files in root:
        #paths.append(path)
        files_extensions = [] 
        for f in files:
            name, *sufix = f.split('.')
            if len(sufix) > 0:
                files_extensions.append(sufix[-1])
        
        extensions_grouped_sum = groupby_sum(files_extensions)
        result.add_line(path, len(files), extensions_grouped_sum[0], extensions_grouped_sum[1])

    result.print_tree()

def groupby_sum(extensions: list) -> tuple:
    names = []
    hits = []

    for extension in extensions:
        if extension in names:
            hits[names.index(extension)] += 1
        else:
            names.append(extension)
            hits.append(1)

    return names, hits

main()
