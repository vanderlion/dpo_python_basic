def get_input_parameters():
    res_cells = []
    for i in range(int(input("Количество клеток: "))):
        cell = int(input(f"Эффективность {i + 1} клетки: "))
        res_cells.append(cell)
    return res_cells


def display_result(cells):
    print(f"Неподходящие значения: ", end="")
    print(*cells)


def select_cells(cells):
    result = []
    for i in range(len(cells)):
        if cells[i] <= i:
            result.append(cells[i])
    return result


if __name__ == "__main__":
    cells = get_input_parameters()
    result_cells = select_cells(cells)
    display_result(result_cells)