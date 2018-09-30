


# import saprfc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 


#url="https://eqc.euhreka.com/sap/bc/bsp/sap/YEOPGL101301/index.html?sap-client=510&sesid=W3at4BQF1ZWfjaZC2GcIQCalCii&light=false&right=false&newUI=true&land=true&label=true#app=VIEW_PT"

#driver = webdriver.Firefox()
#wait=driver.implicitly_wait(10)

#driver.get("https://eqc.euhreka.com/sap/public/bc/ur/eWS/standard/newlogInPage.html?sap-client=510")

#inputElement1 = driver.find_element_by_name("name")

# inputElement1.send_keys("GL_AU_MG001")

# inputElement2 = driver.find_element_by_name("password")
# inputElement2.send_keys("ews12345")
# driver.find_element_by_xpath("//*[@id='loginButton']").click()

# print driver.current_url()
# .//*[@id='subMenuContainerIcons']/div[4]

#wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='subMenu_WA_PT']"))

#driver.implicitly_wait(40)
#driver.find_element_by_xpath("//*[@id='subMenuContainerIcons']/div[5]").click()
# driver.implicitly_wait(40)
# driver.maximize_window()
# driver.find_element_by_css_selector(".application_magnifier_icon.topMenuSearchIcon.datePicker_month_link").click()

# inputelement3=driver.find_element_by_css_selector("text_area_topMenuSearchAutoC")
# inputElement3.send_keys("Who is Who")
# driver.find_element_by_xpath(".subMenuArrow.application_verticalR_arrow").click()
# driver.implicitly_wait(40)
# driver.find_element_by_xpath(".//*[@id='subMenu_SC_WIW']").click()
# driver.implicitly_wait(40)
# driver.find_element_by_xpath(".//*[@id='OM_WIW_selectorViewMenu']/div/div[1]/input").click()
# driver.implicitly_wait(40)
# driver.find_element_by_xpath(".//*[@id='OM_WIW_selectorViewMenu']/div/div[3]/input").click()
# driver.implicitly_wait(40)

appurl="https://eqc.euhreka.com/sap/public/bc/ur/eWS/standard/newlogInPage.html?sap-client=510"
user="GL_AU_MG001"
password="ews12345"
submod="Who is Who"
tab="Who is Who"

def login_and_navigate(url, username, pwd, submodule, tabname= None):
    '''sample method'''
    driver = webdriver.Firefox()
    driver.implicitly_wait(40)
    driver.get(url)
    driver.implicitly_wait(40)
    inputElement1 = driver.find_element_by_name("name")
    inputElement1.send_keys(username)
    inputElement2 = driver.find_element_by_name("password")
    inputElement2.send_keys(pwd)
    driver.implicitly_wait(40)
    driver.find_element_by_xpath("//*[@id='loginButton']").click()

login_and_navigate(appurl,user,password,submod,tab)


#inputElement3.click

#Adding to numbers
# class Sample:
  # def _init_():
   # print "self"
  # def add(self,x,y):
   # z=x+y
   # return z
   # to get odd or 
  
  # def even(self,x):
   # if(x%2==0):
    # print "Given number is even number"    
   # else:
    # print "Given number is odd number"    
  
  # def prime(self,x):
   # for i in range(2,x):
    # if(x%i==0):
	 # print "Given number is prime number"
	 # break
   # else:
	 # print "Given number is not prime number"
   # return x
# a=Sample()
# a.prime(11)
# import re
# url=r'https://eqc.euhreka.com/sap/bc/bsp/sap/YEOPGL101301/index.html?sap-client=510&sesid=0wwXSHDPNnrhLNlSmzwBh7HRxh9&light=false&right=false&newUI=true&land=true&label=true#app=VIEW_PT#app=VIEW_PT'
# appId=r'LANDAPP'
# print url
# tab_url, reps = re.subn(r'(https?://.*#app=).*', r'\1%s' % (appId), url)
# print (r'\1%s' %(appId))
# print tab_url
# print reps


# import xmlrunner
# parser=argparse.ArgumentParser(description="process to find out odd or even")
# parser.add_argument("--run",default=None,action="store_true",help="run this commad")
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   # help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
                   # const=sum, default=max,
                   # help='sum the integers (default: find the max)')

# args = parser.parse_args()
# if args.run:
 # print "Argument run"

# print args.accumulate(args.integers)