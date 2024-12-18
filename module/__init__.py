from .click_image import ScreenHandler

screenhandler = ScreenHandler()

from .process import ProcessStep
from .login.login import run as login_run
from .freind.freind import run as freind_run

__all__ = ['screenhandler',
            'ProcessStep',
            'login_run',
            'freind_run',]