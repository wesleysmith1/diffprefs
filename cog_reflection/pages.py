from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import datetime

class cog_reflect_one(Page):
    form_model='player'
    form_fields=['cog_reflect_one_input']

    def before_next_page(self):
        if(self.player.cog_reflect_one_input == 5):
            self.player.cog_reflect_one_correct = True
        else:
            self.player.cog_reflect_one_correct = False

class cog_reflect_two(Page):
    form_model='player'
    form_fields=['cog_reflect_two_input']

    def before_next_page(self):

        if(self.player.cog_reflect_two_input == 47):
            self.player.cog_reflect_two_correct = True
        else:
            self.player.cog_reflect_two_correct = False

page_sequence = [cog_reflect_one, cog_reflect_two,]