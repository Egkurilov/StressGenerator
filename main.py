example = "914444445555 %s %s 6010 810 000000 000000000000"

terminal = "123456"
counts = 10


def generate(terminal_id, count, third_column):
    for long_tid in range(count):
        write_pool(third_column,f"{long_tid+int(terminal_id):04}")


def write_pool(third_column, two_column):
    file = open(r'TERMS.INI', 'a')
    file.write(example % (third_column, two_column) +"\n")
    file.close()


if len(terminal) == 6:
    second_column, third_column = terminal[:2], terminal[2:]
    generate("01"+second_column, counts, third_column)




