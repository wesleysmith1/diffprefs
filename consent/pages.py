from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import datetime

class consent(Page):
    pass

    def before_next_page(self):
        self.player.consent_time = datetime.datetime.now()

page_sequence = [consent]