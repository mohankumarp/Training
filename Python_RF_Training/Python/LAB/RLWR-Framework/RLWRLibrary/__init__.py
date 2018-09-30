'''This is a library for RobotFramework that uses Selenium 2.0 WebDriver in the back-end.
For the front it it provides a number of specific keywords to work with NGA's EWS application
It shall be awesome.'''


from csv import DictReader
import os
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from Selenium2Library import Selenium2Library
#page elements
from EWSLibrary.pageobjects.ews_buttons import EWSButtons
from EWSLibrary.pageobjects.ews_inputs import EWSInputs
from EWSLibrary.pageobjects.ews_radiocheck import EWSRadioCheck
from EWSLibrary.pageobjects.ews_tables import EWSTables
from EWSLibrary.pageobjects.ews_trees import EWSTrees
from EWSLibrary.pageobjects.ews_calendar import EWSCalendar
from EWSLibrary.pageobjects.ews_message_box import EWSMessageBox
from EWSLibrary.pageobjects.ews_text import EWSText
from EWSLibrary.pageobjects.ews_links import EWSLinks


#waits
from EWSLibrary.pageobjects.waits import Waits
#flows
from EWSLibrary.flows.flows import Flows
from EWSLibrary.flows.flows_pcr import Flows_PCR
#core - settings
from EWSLibrary.core.object_repository import ObjectRepository
from EWSLibrary.settings import Settings



_EWSLIBRARY_PATH=os.path.dirname(os.path.abspath(__file__))
if os.sys.platform == "darwin": #support mac :)
    CHROMEDRIVER_PATH = os.path.join(_EWSLIBRARY_PATH, "lib", "chromedriver")
else: #assume windows
    CHROMEDRIVER_PATH = os.path.join(_EWSLIBRARY_PATH, "lib", "chromedriver.exe")


class EWSLibrary( Selenium2Library, EWSButtons, EWSInputs, EWSRadioCheck, Waits,
                EWSTables, EWSText, EWSLinks, EWSTrees, EWSCalendar, EWSMessageBox, Flows, Flows_PCR):
    '''This is the main class for a library for RobotFramework that uses Selenium 2.0 WebDriver
    in the back-end.  It exposes the EWSLibrary to robot framework
    '''

    def __init__(self,
                 timeout=0.0,
                 client=None,
                 run_on_failure='Capture Page Screenshot',
                 highlight=None,
                 log_console=None,
                 lang='en',
                 use_proxy=None, 
                 test_data_dir=None,
                 login_data_dir=None,
                 or_dir=None):
        '''for the initi function timeout will be used to set both javascript timeout and
        the implicit_wait functunality.  Client is used to perform different functions for 
        different ews clients, say AZ vs Securex. run_on_failure is the robot framework keyword that 
        is run when a keyword fails, by default it is set to capturing a page screenshot, 
        test_data_dir holds path to TestData directory, login_data_dir holds path to login directory, 
        or_dir holds path to objectrepository directory'''
        super( EWSLibrary, self).__init__()

        #allow overwritting of EWSLibrary from command line
        timeout = self._cmdline_val("timeout", timeout)
        client = self._cmdline_val("client", client)
        highlight = self._cmdline_val("highlight", highlight)
        log_console = self._cmdline_val("log_console", log_console)
        lang = self._cmdline_val("lang",lang)
        use_proxy = self._cmdline_val("proxy", use_proxy)
        test_data_dir = self._cmdline_val("test_data_dir", test_data_dir)
        login_data_dir = self._cmdline_val("login_data_dir", login_data_dir)
        or_dir = self._cmdline_val("or_dir", or_dir)

        #setup an OR
        self.OR = ObjectRepository().default_OR

        #override global settings only if they were sepcifically passed in this
        #makes it easy to set global settings from run_tests.py
        new_settings = {}
        if client != None: new_settings["client"] = client
        if highlight != None: new_settings["highlight"] = highlight
        if log_console != None: new_settings["log_console"] = log_console
        if lang !='en': new_settings['lang'] = lang
        if use_proxy is not None: new_settings['use_proxy'] = use_proxy
        if test_data_dir is not None: new_settings['test_data_dir'] = test_data_dir
        if login_data_dir is not None: new_settings['login_data_dir'] = login_data_dir
        if or_dir is not None: new_settings['or_dir'] = or_dir

        self.settings = Settings(new_settings)

        self.OR = self.settings.merge_ORs(self.OR)

        logger.console("EWSLibrary created with timeout=%s , client=%s , "
            "highlight=%s , log_console=%s , run_on_failure=%s , lang=%s , test_data_dir=%s, "
            "login_data_dir=%s, or_dir=%s" % (timeout,
                client, highlight, log_console, run_on_failure, lang,
                 test_data_dir, login_data_dir, or_dir))

        Selenium2Library.__init__(self,timeout=timeout, implicit_wait=timeout,
                    run_on_failure=run_on_failure)

    def _cmdline_val(self,cmdline_name,default):
        '''returns the value from the command line if it exists otherwise
        returns the default value
        '''
        try:
            val = BuiltIn().get_variable_value("${%s}" % cmdline_name)
            return val if val else default
        except AttributeError:  #raised during unit testing
            return default


    def open_browser(self, url, browser="firefox", alias=None):
        #default to ff if we are not on windows
        if ((["ie", "internet explorer"].count(browser.lower()) > 0 )
                and (self.get_os_name() != "win32")):
            browser = "firefox"   #there is not ie on mac or linux so set ie to firefox
        
        return Selenium2Library.open_browser(self, url, browser, alias)


    @property
    def browser(self):
        return self._current_browser()
    
    def _make_ff(self , remote , desired_capabilites , profile_dir):
        '''override the firefox creation function in Selenium2Library
        so we can put firebug in the mix.:) '''
        #constants to point to ff profile dir
        ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
        FIREFOX_PROFILE_DIR = os.path.join(ROOT_DIR, 'lib', 'firefoxprofile')
        FIREBUG_EXTENSION = os.path.join(ROOT_DIR, 'lib', 'firebug-1.11.2-fx.xpi')
        FIREPATH_EXTENSION = os.path.join(ROOT_DIR,'lib', 'firepath-0.9.7-fx.xpi')
        GREASEMONKEY_EXTENSION = os.path.join(ROOT_DIR,'lib', 'greasemonkey-1.8-fx.xpi')
        from selenium import webdriver
        #do to huge logs on CI server, for now just turn of native events if we
        #are not on windows...they don't work anyways on mac and the CI server
        #is linux
        #if self.get_os_name() != "win32":
        webdriver.Firefox.NATIVE_EVENTS_ALLOWED = False
        #webdriver.Firefox.__init__ = __ff_init__

        if not profile_dir: profile_dir = FIREFOX_PROFILE_DIR
        profile = webdriver.FirefoxProfile(profile_dir)
        if remote:
            browser = self._create_remote_web_driver(webdriver.DesiredCapabilities.FIREFOX  ,
                        remote , desired_capabilites , profile)
        else:
            #setup some debuging stuff
            #TODO: probably need some sort of flag so we don't try to do this on the CI server
            profile.add_extension(FIREBUG_EXTENSION)
            profile.add_extension(FIREPATH_EXTENSION)
            #profile.add_extension(GREASEMONKEY_EXTENSION)
            #setting this disables the annoying firebug first run page
            profile.set_preference("extensions.firebug.currentVersion", "1.11.2")
            profile.set_preference("extensions.greasemonkey.version", "1.8")
            # Proxy setup here. and since the code was structured like this
            # we need to add other _make_* functions for the other browsers
            proxy = None
            if (self.settings.use_proxy is not None):
                proxy = self._get_proxy_ff(self.settings.use_proxy.upper(), webdriver)
            
            browser = webdriver.Firefox(firefox_profile=profile, proxy=proxy)
        return browser

    def _get_proxy_ff(self, proxy_env, webdriver):
        #proxy_env = self.settings.use_proxy.upper()
        logger.info("proxy setting: %s" % proxy_env, also_console=True)
        # Currently assume one proxy_env per DC environment, otherwise: DCA-EQC, DCA-SEQ, etc.
        if not self.settings.proxies.get(proxy_env, None):
            logger.warn('<span class="fail">Proxy "%s" does not exist!</b>' % proxy_env, html=True)
            raise ValueError("proxy doesn't exist")
        else:
            from selenium.webdriver.common.proxy import Proxy, ProxyType
            myProxy = self.settings.proxies[proxy_env]
            logger.info("proxy for '%s' is '%s'" % (proxy_env, myProxy))
            
            proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'autodetect': False,
                'httpProxy': myProxy,
                'ftpProxy': myProxy,
                'sslProxy': myProxy,
                'noProxy': ''
                # TODO: add the internal hosts if some eWS communications use
                # internal hosts even if the eWS server is external
                })
            
            # we don't need this bit of code, for now. but leaving it in...
            """
            driver = webdriver.Firefox(proxy=proxy)
            # for remote
            caps = webdriver.DesiredCapabilities.FIREFOX
            proxy.add_to_capabilities(caps)
            driver = webdriver.Remote(desired_capabilities=caps)
            """
            return proxy

    def get_os_name(self):
        '''use this function to get the os_name from robot framework.'''
        #FYI, from http://docs.python.org/library/sys.html#sys.platform
        #Linux (2.x and 3.x)    'linux2'
        #Windows    'win32'
        #Windows/Cygwin    'cygwin'
        #Mac OS X    'darwin'

        if os.sys.platform.startswith('linux'):
            return 'linux'      #preparing for python 3.3 :P
        return os.sys.platform

    def _info_to_console(self,msg,html=False,also_console=True):
        '''use self._info instead of logger.info so info goes also to the
        console
        '''
        logger.write(msg, 'INFO', html)
        if also_console:
            logger.console(msg)
        #self._old_logger(msg,html,also_console)

    def make_euhbool(self, *args):
        '''Converts strings, ints, etc. to boolean values, since all RF scripts pass
        parameters to selenium as strings.
        Usage, multiple and single vars:
        (positive_test, required) = self.make_euhbool(positive_test, required)
        positive_test = self.make_euhbool(positive_test)
        '''
        if len(args)==1:
            return BuiltIn().convert_to_boolean(args[0])
        return tuple(BuiltIn().convert_to_boolean(arg) for arg in args)

    def decode_utf8(self, strvalue):
        '''Decode any string using utf8. 
        This is required when we use a text which is not in English language'''
        return strvalue.decode('utf8')


    def _get_password(self, user_name, client_sys):
        """Read through the 'logins.txt' directly under the proj repo and check
        each username against the listed one, returning the password according
        to the client_sys provided in the password argument from RF.
        If client_sys is None or '' then return the one under 'Password'
        """
        if not client_sys: client_sys = 'Password'
        self.login_file = self.settings.get_login_file()
        logger.info('login file: %s' % self.login_file, also_console=True)
        lf = DictReader(open(self.login_file, 'rb'), delimiter='\t')
        for row in lf:
            if row['Username'] == user_name:
                logger.info(row)
                password = row.get(client_sys, None)
                break
        else:
            raise ValueError("username not found: '%s'" % user_name)
        
        if password is None:
            raise ValueError("password not found for username '%s' on system '%s'"
                             % (user_name, client_sys))
        return password
    
    def _get_test_data(self, id, path, data_file_name, product=None):
        """Return test data  for given 'id' and 'product'. if 'product' is None then data returned based on 'id'.
        """
        self.test_data_file = self.settings.get_test_data_file(data_file_name, path)
        logger.info('Test Data file: %s' % self.test_data_file , also_console=True)
        lf = DictReader(open(self.test_data_file, 'rb'), delimiter='\t')
        isIDFound, isProductFound = False, False
        for row in lf:
            if row['ID'].lower() == id.lower():
                isIDFound = True
                if product == None:
                    test_data = self._get_data(row)
                    return test_data
                if product != None and row['PRODUCT'].lower() == product.lower():
                    test_data = self._get_data(row)
                    isProductFound = True
                    return test_data
        if not isIDFound:
            raise ValueError("ID not found: '%s'" % id)
        if product != None and not isProductFound:
            raise ValueError("PRODUCT not found: '%s'" % product)
    
    def _get_data(self, row):
        '''Convert test data which has string ${none} to RF ${None}
        '''
        for key in row:
            if row[key].lower() == '${none}':
                row[key] = None
        logger.info(row)
        test_data = row
        return test_data

    def maximize_browser(self):
        self.browser.maximize_window()


