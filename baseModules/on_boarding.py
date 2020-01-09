import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from BaseFiles import filePaths, readExcel
from BaseFiles.AuthorizeNewUser import Authorize
from BaseFiles.VertoUtil import Utilities



class SigingUp:
    def __init__(self, driver):

        self.driver = driver
        self.nextbtn = ".btn.btn-sm.btn-custom-navy"
        self.UItext = ".text-gray.m-b-5"

    def readData(self):
        global Fname
        global Lname
        global email
        global password
        global concode
        global country
        global bname
        global compnumm
        global site
        global badd
        global zcode
        global city
        global btype
        global bcat
        global brol
        global emps
        global benowner
        global oper
        global birthd
        global bdoc
        global pdoc
        global pownerper
        global pdob
        global padd
        global pcon
        global pzip
        global pcity
        global phon
        global answ

        path = filePaths.getfile("vertofx1")
        sheetname = "signup"
        email = readExcel.ReadingFile.getemails(path, sheetname)
        password = readExcel.ReadingFile.getpassword(path, sheetname)
        Fname = readExcel.ReadingFile.getFirstnanme(path, sheetname)
        Lname = readExcel.ReadingFile.getLastname(path, sheetname)
        concode = readExcel.ReadingFile.getCountrycode(path, sheetname)
        phon = readExcel.ReadingFile.getPhonenumber(path, sheetname)
        sheetname = "activationform"
        country = readExcel.ReadingFile.getCountry(path, sheetname)
        bname = readExcel.ReadingFile.getbname(path, sheetname)
        compnumm = readExcel.ReadingFile.getcomnum(path, sheetname)
        site = readExcel.ReadingFile.getwebsite(path, sheetname)
        badd = readExcel.ReadingFile.getaddress(path, sheetname)
        zcode = readExcel.ReadingFile.getzipcode(path, sheetname)
        city = readExcel.ReadingFile.getCity(path, sheetname)
        btype = readExcel.ReadingFile.getbtype(path, sheetname)
        bcat = readExcel.ReadingFile.getbcat(path, sheetname)
        brol = readExcel.ReadingFile.getbrole(path, sheetname)
        emps = readExcel.ReadingFile.getempst(path, sheetname)
        benowner = readExcel.ReadingFile.getbenOwner(path, sheetname)
        oper = readExcel.ReadingFile.getOwnerper(path, sheetname)
        birthd = readExcel.ReadingFile.getDOB()
        sheetname = "business_documents"
        bdoc = readExcel.ReadingFile.getdocs(path, sheetname)
        sheetname = "personalinfo"
        pownerper = readExcel.ReadingFile.getdocs(path, sheetname)
        pdob = readExcel.ReadingFile.getDOB(path, sheetname)
        padd = readExcel.ReadingFile.getaddress(path, sheetname)
        pcon = readExcel.ReadingFile.getCountry(path, sheetname)
        pzip = readExcel.ReadingFile.getzipcode(path, sheetname)
        pcity = readExcel.ReadingFile.getCity(path, sheetname)
        sheetname = "personal_doc"
        pdoc = readExcel.ReadingFile.getdocs(path, sheetname)
        sheetname = "answer"
        answ = readExcel.ReadingFile.getanswer(path, sheetname)

    def signup(self):
        self.readData()
        new_var = SignUpproc()
        new_var.InitiateSignUP()
        for i in range(0, len(Fname)):
            new_var.FillActivationForm(Fname[i], Lname[i], email[i], concode[i], phon[i], password[i])
            new_var.ConfirmMail(email[i])
            new_var.SelectBusCountry(country[i])
            new_var.FillBusDetails(bname[i], compnumm[i], site[i], badd[i], zcode[i], city[i], btype[i], bcat[i],
                                   brol[i], emps[i])
            new_var.CheckBenificiary(benowner[i])
            for j in range(0, len(bdoc)):
                new_var.UploadBusDocuments(bdoc[j])
            util.Click_Element(self.driver.find_element_by_css_selector(self.nextbtn))
            util.WaitForProgressSpinner()
            new_var.FillPersonalDetails(Fname[i], Lname[i], phon[i], pdob[i], email[i], pownerper[i], padd[i], pzip[i],
                                        pcity[i], pcon[i])
            for z in range(0, len(pdoc)):
                new_var.UploadPersonalDoc(pdoc[z])
            util.Click_Element(self.driver.find_element_by_css_selector(self.nextbtn))
            util.WaitForProgressSpinner()
            new_var.FillQuestionier(answ[0], answ[1])
            divheader = self.driver.find_elements(By.CSS_SELECTOR, self.UItext)

            assert divheader[0].text == "Company Name"
            assert divheader[1].text == "e-Wallet Balance"
            assert divheader[2].text == "My Open Orders"
            assert divheader[3].text == "My Offers"

            new_var.Logout()

    def AdminAuth(self):
        c3 = Authorize()
        for i in range(0, len(Fname)):
            c3.AdminLoginfun(email[i], Fname[i])
