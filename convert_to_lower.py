    from sys import argv

    source, target = argv[1], argv[2]
    with open(source) as f_source, open(target, 'w') as f_to:
        for line in f_source:
            f_to.write(line.lower() + "\n")