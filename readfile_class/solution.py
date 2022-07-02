
class FileReader:
    def __init__(self, dest):
        self.dest = dest
    def __str__(self):
        pass
    def read(self):
        try:
            with open(self.dest, 'r') as file:
                data = file.read()
                if data:
                    return data
                return ''
        except FileNotFoundError:
            return ''
