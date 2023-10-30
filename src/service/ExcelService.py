import openpyxl


excel_file_path = "/mnt/c/projetos/i3c/desafio-i3c/DESAFIO.xlsx"


def change_item(item_id, new_price_value, new_quantity_value):
    try:
        wb = openpyxl.load_workbook(
            excel_file_path, data_only=True)

        planilha = wb['BOM']

        coluna_id = planilha['A']

        for cell in coluna_id:
            if cell.value == item_id:
                change_item_price(cell, new_price_value)
                change_item_quantity(cell, new_quantity_value)
                break

        # /mnt/c/projetos/i3c/desafio-i3c/DESAFIO.xlsx
        wb.save(excel_file_path)

    except Exception as e:
        print(e)


def change_item_price(cell, new_price_value):
    try:
        cell.offset(0, 19).value = new_price_value
    except Exception as e:
        print(e)


def change_item_quantity(cell, new_quantity_value):
    try:
        cell.offset(0, 8).value = new_quantity_value
    except Exception as e:
        print(e)


def get_total_item_price(item_id):
    try:
        wb = openpyxl.load_workbook(
            excel_file_path, data_only=True)

        planilha = wb['PROPOSTA']

        coluna_id = planilha['B']

        for cell in coluna_id:
            print(cell.value)
            if cell.value == item_id:
                print(cell.value)
                return cell.offset(0, 6).value

    except Exception as e:
        print(e)
