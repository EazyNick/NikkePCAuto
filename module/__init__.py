from .click_image import ScreenHandler

screenhandler = ScreenHandler()

from .process import ProcessStep
from .dailycheck.dailycheck import run as dailycheck_run
from .login.login import run as login_run
from .freind.freind import run as freind_run
from .outpost.outpost import run as outpost_run

__all__ = ['screenhandler',
            'ProcessStep',
            'dailycheck_run',
            'login_run',
            'freind_run',
            'outpost_run',]