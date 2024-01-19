import collectdata
def message():
    date=collectdata.gettime()
    handinfo=collectdata.hardinfo()
    return date+"\n"+handinfo