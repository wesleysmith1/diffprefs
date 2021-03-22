from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import datetime

class survey(Page):
    form_model='player'
    form_fields=['gender','age','ethnicity','marital_status','employment','insurance','annual_income',
    'credit_card','smoke','alcohol','participant_education', 'parent_education', 'experimentplay', 'hourly_wage',
    'regret_one', 'regret_two', 'regret_three', 'regret_four']

page_sequence = [survey]