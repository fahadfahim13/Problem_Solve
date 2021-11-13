class Path:
    def __init__(self, _path: str) -> None:
        self.current_path = _path

    def cd(self, new_path):
        if new_path.startswith('/'):
            self.current_path = new_path
        else:
            orig = self.current_path.split('/')
            for part in new_path.split('/'):
                if part == '..':
                    if len(orig) > 0:
                        orig.pop()
                    else:
                        orig = ['']
                else:
                    orig.append(part)
            if orig == ['']:
                self.current_path = '/'
            else:
                self.current_path = '/'.join(orig)


path = Path('/a/b/c/d')
path.cd('e/x/r')
print(path.current_path)
