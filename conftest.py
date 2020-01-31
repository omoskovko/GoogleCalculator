import pytest
import os
import sys
import inspect
import re

from .common.utils import get_driver
from .common.google_one_box import GoogleOneBox

def get_out_path(*dirList):
    mainFileName = inspect.stack()[0][1]
    currOutFolder = 'output.png'
    if not os.path.exists(currOutFolder):
        os.makedirs(currOutFolder)

    return os.path.abspath(os.path.join(os.path.dirname(mainFileName), currOutFolder, *dirList))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        p = re.compile('(\:|\(|\)|\.)')
        #outPngFile = get_out_path(rep.nodeid.replace(":", "_").replace("(", "_").replace(")", "_").replace(".", "_")+".png")
        outPngFile = get_out_path(p.sub(':', rep.nodeid).split(":")[-1]+".png")
        #print("Failed test is: "+outPngFile)
        
        try:
            if "resource_handler" in item.fixturenames:
                item.funcargs["resource_handler"]._driver.get_screenshot_as_file(outPngFile)
        except Exception as err:
            print(err)

'''        
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
'''        
    
def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="Firefox", help="WEB Driver name")

@pytest.fixture(scope="session")
def resource_handler(request):
    googleBox = GoogleOneBox(get_driver(request.config.option.driver), 'https://www.google.com')
    rh = googleBox.search_for("1+2=")

    # The current best practice for setup and teardown is to use yield
    # http://doc.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code
    yield rh

    try:
        rh._driver.quit()
    except Exception as err:
        print(err)

    '''
    According to http://doc.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code use of addfinalizer is "historical".
    def fin():
        try:
            rh._driver.quit()
        except Exception as err:
            print(err)

    request.addfinalizer(fin)
    return rh
    '''