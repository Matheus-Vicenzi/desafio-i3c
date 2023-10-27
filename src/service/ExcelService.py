import openpyxl

def read_sheet(item_descricao):
    try:
        wb = openpyxl.load_workbook('/mnt/c/projetos/i3c/desafio-i3c/DESAFIO.xlsx')

        planilha = wb['BOM']

        coluna_descricao = planilha['F']

        valores_coluna = []
        print(type(coluna_descricao))

        # for cell in coluna_descricao:
        #     #if cell.value is not None :
        #     if type(cell.value) is str:
        #         #valores_coluna.append(cell.value)

        # print(valores_coluna)

    except Exception as e:
        print(e)