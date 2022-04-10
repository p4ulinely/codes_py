class Tree():
    def __init__(self):
        self.tree = []

    def get_tree(self) -> list:
        return self.tree

    def print_tree(self) -> None:
        for l in self.tree:
            print(l)

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
