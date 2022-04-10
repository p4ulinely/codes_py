class Tree():
    def __init__(self):
        self.tree = []

    def get_tree(self) -> list:
        return self.tree

    def print_tree(self) -> None:
        # TODO: need to work on it
        for l in self.tree:
            inicial_tab = ''.rjust(len(l['path'])-1, ' ')
            print(l['path'])
            for e, h in zip(l['extensions'], l['extensions_hits']):
                print(f"{inicial_tab}| {e}: {h}")
            print(f"{''.rjust(len(l['path'])-1, ' ')}{l['files_number']} file(s) in the path")

    def add_line(
            self, 
            path: str, 
            files_number: int, 
            extensions: list, 
            extensions_hits: list) -> None:
        '''
            line eg.: { 'path': '/folder','extensions': ['py', 'exe', 'txt'], 'extensions_hits': [2, 3, 4] } 
        '''
        if not path:
            raise Exception('path is empty.')

        line = {
            'path': path,
            'files_number': files_number,
            'extensions': extensions,
            'extensions_hits': extensions_hits
        }
        self.tree.append(line)
