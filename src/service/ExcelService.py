import openpyxl
import traceback
from infra.Enviroment import EXCEL_FILE_PATH


def change_item(item_id, new_quantity_value):

    try:
        row = get_item_row(item_id)
        set_item_quantity(row, new_quantity_value)
        proposta_row = get_item_proposta_row(item_id)
        total_value = get_item_total_value(proposta_row)
        return total_value
    
    except Exception as e:
        print(e)
        traceback.print_exc()


def set_item_quantity(row, new_quantity_value):
    try:
        wb = openpyxl.load_workbook(
            EXCEL_FILE_PATH, data_only=False)
        sheet = wb['BOM']

        quantity_cell = sheet.cell(row=row, column=9)
        quantity_cell.value = new_quantity_value

        wb.save(EXCEL_FILE_PATH)

    except Exception as e:
        print(e)
        traceback.print_exc()

    finally:
        wb.close()


def get_item_proposta_row(item_id):
    try:
        wb = openpyxl.load_workbook(
            EXCEL_FILE_PATH, data_only=True)
        sheet = wb['PROPOSTA']

        id_column = sheet['B']
        for cell in id_column:
            print(cell.value)
            if cell.value == item_id:
                print(cell.coordinate, "coordenada")
                return cell.coordinate

    except Exception as e:
        print(e)
        traceback.print_exc()

    finally:
        wb.close()


def get_item_row(item_id):
    try:
        wb = openpyxl.load_workbook(
            EXCEL_FILE_PATH, data_only=True)
        sheet = wb['BOM']

        id_column = sheet['A']
        for cell in id_column:
            print(cell.value)
            if cell.value == item_id:
                return cell.row

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
        print("cell", quantity_cell)
        quantity_cell.value = new_quantity_value
        print(quantity_cell.value)
    except Exception as e:
        print(e)
        traceback.print_exc()


def get_item_total_value(proposta_row):
    try:
        wb = openpyxl.load_workbook(
            EXCEL_FILE_PATH, data_only=True)
        
        sheet = wb['PROPOSTA']

        cell = sheet.cell(row=proposta_row, column=9)

        return cell.value

    except Exception as e:
        print(e)
        traceback.print_exc()

    finally:
        wb.close()
