    from sys import argv
    from pathlib import Path

    def get_filename(width=3):
        idx = 1
        if len(argv) > 1:
            id = argv[1]
        else:
            id = 'FILEID'
        while True:
            filename = Path(f'{id}{idx:0>{width}}')
            if not filename.is_file():
                yield filename
            idx += 1

    new_file = iter(get_filename())
    for _ in range(10):
        filename = next(new_file)
        print(filename.name)


