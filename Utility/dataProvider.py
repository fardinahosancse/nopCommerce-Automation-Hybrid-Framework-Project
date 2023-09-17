from Utility import excelReader as XOP

def get_data(sheetName,excel_location):
    path = "..//Excel/nopCusData.xlsx"
    rows = XOP.get_row(path,sheetName)
    cols = XOP.get_column(path,sheetName)
    data=[]

    """Responsible for genarate data out of excel file by using excelProvider.py """

    for r in range(2,rows+1):
        dataList=[]
        for c in range(1,cols+1):
            dataAsset = XOP.read_excel(path,sheetName,r,c)
            dataList.insert(c,dataAsset)
        data.insert(r,dataList)
    return data