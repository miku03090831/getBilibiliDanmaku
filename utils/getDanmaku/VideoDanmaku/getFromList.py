import ByUid
print("请输入起始和终止下标（范围是1~500）")
print("包含起始和终止，例如爬取前一百应该输入1和100")
start = int(input("起始："))
end = int(input("终止："))
try:
    with open("UidList.txt","r") as f:
        lines = f.readlines()
        uids = lines[start-1:end]
        for uid in uids:
            ByUid.main(uid.strip())
except:
    print("读取文件出错，请检查路径")