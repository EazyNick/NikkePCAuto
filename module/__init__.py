from .click_image import TemplateProcessor

templateprocessor = TemplateProcessor()

from .process import ProcessStep
from .dailycheck.dailycheck import run as dailycheck_run
from .login.login import run as login_run
from .freind.freind import run as freind_run
from .outpost.outpost import run as outpost_run
from .shop.shop import run as shop_run
from .mail.mail import run as mail_run

__all__ = ['templateprocessor',
            'ProcessStep',
            'dailycheck_run',
            'login_run',
            'freind_run',
            'outpost_run',
            'shop_run',
            'mail_run',]