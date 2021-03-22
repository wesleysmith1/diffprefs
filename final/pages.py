from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Final(Page):
    pass

page_sequence = [Final]
