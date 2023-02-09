import os


class File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
   
    def __enter__(self):
        if not os.path.exists(self.filename):
            open(self.filename, 'w', encoding='utf8').close()
            self.file = open(self.filename, self.mode, encoding='utf8')
            return self.file
   
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type and issubclass(exc_type, IOError):
            return True
        return True


with File("example.txt", "w") as file:
    file.write("Hello, World!")