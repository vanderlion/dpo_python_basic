class File:
    """
    Модернизированная версия контекст-менеджера File — теперь при попытке
    открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи.
    """

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)  # Add self.mode
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == '__main__':
    with File('example.txt', 'w+') as file:
        file.write('Hello World!!')