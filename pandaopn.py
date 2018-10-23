import os
import pandas as  pd;

path = str("C:\\Users\\----py\\Desktop\\ce\\New folder")
fileToRead =[]


for subdir, dirs, files in os.walk(path):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".xlsx"):
            fileToRead.append(filepath)


myheader=[]
# for i in fileToRead:
#     open = pd.read_sas(i)
#     df = pd.DataFrame(open)

# strx=path+"1.xlsx"
# +"shopex_Current9v5d95ZId1i_278_96_161013_1365.sass"
for i in fileToRead:
    # strx=path+i
    if(i.__contains__("~$")):
        pass
    print(i)
    tempsheet=str(i.replace(".","_").replace(":","_")).replace("\\", "_")
    print(tempsheet[-20:])
    open = pd.read_excel(i)
    df = pd.DataFrame(open)
    ds= pd.DataFrame()
    temp = df.iloc[:,[0,4,26,27,39,46]]

    for xm in temp:
        myheader.append(xm)
    # print(df.iloc[:,[0,4,26,27,39,46]])
    print(myheader)
    # print(ds.column(1))
    # :print(df[["Evaluation_ID","Store_Name","Store_State","Store_City","StoreZip","Bonus_Pay", "Shopper_Sex","Client_Survey_Name"]])
    # writex = df.ExcelWriter(path +"\\news.xlsx", engine="xlsxwriter")
    # ds.to_excel(writex,sheet_name=tempsheet[-20:], header=True)
    # writex.save()

writex.close()
