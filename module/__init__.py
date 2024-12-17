from .click_image import ScreenHandler

from .login.login import run as login_run

screenhandler = ScreenHandler()

__all__ = ['screenhandler',
           'login_run',]