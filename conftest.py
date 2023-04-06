import pytest
import os
import inspect
import re

from .common.utils import get_driver
from .common.google_one_box import GoogleOneBox


def determine_scope(fixture_name, config):
    # https://docs.pytest.org/en/stable/fixture.html#dynamic-scope
    if config.option.session:
        return "session"
    return "function"


def get_out_path(*dirList):
    mainFileName = inspect.stack()[0][1]
    currOutFolder = "output.png"
    if not os.path.exists(currOutFolder):
        os.makedirs(currOutFolder)

    return os.path.abspath(
        os.path.join(os.path.dirname(mainFileName), currOutFolder, *dirList)
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call":
        xfail = hasattr(rep, "wasxfail")
        if xfail or rep.failed:
            p = re.compile(r"(\:|\(|\)|\.)")
            # outPngFile = get_out_path(rep.nodeid.replace(":", "_").replace("(", "_").replace(")", "_").replace(".", "_")+".png")
            outPngFile = get_out_path(p.sub(":", rep.nodeid).split(":")[-1] + ".png")
            # print("Failed test is: "+outPngFile)

            try:
                if "resource_handler" in item.fixturenames:
                    item.funcargs["resource_handler"]._driver.get_screenshot_as_file(
                        outPngFile
                    )
            except Exception as err:
                print(err)


"""        
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
"""


def pytest_addoption(parser):
    parser.addoption(
        "--driver", action="store", default="Chrome", help="WEB Driver name"
    )
    parser.addoption(
        "--testLoops", action="store", default=2, help="Count of suite loops"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Use headless parameter"
    )
    parser.addoption(
        "--session",
        action="store_true",
        default=False,
        help="Run fixture in session scope",
    )


def pytest_configure(config):
    class Plugin:
        @pytest.fixture(
            scope=determine_scope,
            params=[v for v in range(int(config.option.testLoops))],
        )
        def test_loops(self, request):
            return request.param

    config.pluginmanager.register(Plugin())


@pytest.fixture(scope=determine_scope)
def resource_handler(request):
    googleBox = GoogleOneBox(
        get_driver(request.config.option.headless, request.config.option.driver),
        "https://www.google.com",
    )
    rh = googleBox.search_for("1+2=")

    # The current best practice for setup and teardown is to use yield
    # http://doc.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code
    yield rh

    try:
        rh._driver.quit()
    except Exception as err:
        print(err)

    """
    According to http://doc.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code use of addfinalizer is "historical".
    def fin():
        try:
            rh._driver.quit()
        except Exception as err:
            print(err)

    request.addfinalizer(fin)
    return rh
    """


@pytest.fixture(autouse=True)
def process_func(request, resource_handler):
    """
    The class-level process_func fixture is marked with autouse=true which implies
    that all test methods in the class will use this fixture without a need to state it
    in the test function signature or with a class-level usefixtures decorator.
    http://doc.pytest.org/en/latest/fixture.html#autouse-fixtures-xunit-setup-on-steroids
    """
    if request.node.get_closest_marker("setup_func"):
        print("SetUp function {0}".format(request.function.__name__))
        print(request.keywords.node.funcargs.keys())
        resource_handler.clear_result()

    yield

    if request.node.get_closest_marker("setup_func"):
        print("TearDown function {0}".format(request.function.__name__))
        print(request.keywords.node.funcargs.keys())
        resource_handler.clear_result()
