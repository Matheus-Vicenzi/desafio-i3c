import openpyxl
import traceback


excel_file_path = "/mnt/c/projetos/i3c/desafio-i3c/DESAFIO.xlsx"

# AT, AI


def change_item(item_id, new_price_value, new_quantity_value):
    try:
        wb = openpyxl.load_workbook(
            excel_file_path, data_only=True)

        sheet = wb['BOM']

        id_column = sheet['A']
        for cell in id_column:

            if cell.value == item_id:
                print(
                    f'O valor {cell.value} foi encontrado na célula {cell.coordinate}')
                change_item_price(sheet, cell, new_price_value)
                change_item_quantity(sheet, cell, new_quantity_value)
                new_total_value = change_item_total_value(
                    wb, new_price_value=new_price_value, new_quantity_value=new_quantity_value, item_id=item_id)
                break

        wb.save(excel_file_path)
        return new_total_value

    except Exception as e:
        print(e)
        traceback.print_exc()

    finally:
        wb.close()


def change_item_price(sheet, id_cell, new_price_value):
    try:
        value_cell = sheet.cell(row=id_cell.row, column=10)
        value_cell.value = new_price_value
    except Exception as e:
        print(e)
        traceback.print_exc()


def change_item_quantity(sheet, id_cell, new_quantity_value):
    try:
        quantity_cell = sheet.cell(row=id_cell.row, column=9)
        quantity_cell.value = new_quantity_value
    except Exception as e:
        print(e)
        traceback.print_exc()


def change_item_total_value(wb, new_price_value, new_quantity_value, item_id):
    try:
        print(wb, new_price_value, new_quantity_value, item_id)

        new_total_price = new_price_value * new_quantity_value

        sheet = wb['PROPOSTA']

        id_column = sheet['A']

        for cell in id_column:
            if cell.value == item_id:
                total_price_cell = sheet.cell(
                    row=cell.row, column=8)
                total_price_cell.value = new_total_price

                return new_total_price

    except Exception as e:
        print(e)
        traceback.print_exc()

    finally:
        wb.close()
