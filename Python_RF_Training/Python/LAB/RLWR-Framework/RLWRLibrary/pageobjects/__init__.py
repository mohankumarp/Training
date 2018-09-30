'''pageobjects module is where all the ews functionality is stored.  It includes such files as
ews_button, ews_element_finder, dummy_classes, object_repository and more'''

from robot.api import logger
from selenium.common.exceptions import StaleElementReferenceException
from decorator import decorator


@decorator
def handle_stale_element(method, *args, **kwargs):
    '''This is a decorator which means it is a function used
    to wrap other functions.  It will wrap a function and if that
    function throws a StaleElementReferenceException, which usually
    happens becaue an AJAX call has changed an element we are trying
    to operate on, it will retry the function one more time, the idea
    is the function would just try to find the element again and then
    performe an operation on the element.
    To use this decorator on a function declare the function like:
    @handle_stale_element
    def myfunction():
    a good example is euh_set_text_value
    '''
    try:
        return method(*args, **kwargs)
    except StaleElementReferenceException:
        logger.warn("Found a stale element in %s trying again.  Consider using"
                " an explicit wait such as wait until page contains element to"
                " avoid the stale element and speed up script playback time." % (method.__name__))
        return method(*args, **kwargs)
     
