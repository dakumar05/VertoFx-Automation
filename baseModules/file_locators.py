def get_Browser_Path(browser):
    if browser == "chrome":
        path = "./externalFiles/chromedriver.exe"
        return path
    else:
        path = "./externalFiles/chromedriver.exe"
        return path

def get_Data_File(file_name):
    if file_name == "vertofx1":
        path = "./dataFiles/Vertofx1.xlsx"
        return path

def get_Url(url):
    if url == "uat":#
        url1 = "https://uat.vertofx.com"
        return url1
    else:
        url = "https://uat.vertofx.com"
        return url