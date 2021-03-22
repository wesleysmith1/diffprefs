from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.db.models import DateTimeField

import random

author = 'Chet Garlick'

doc = "Implementation of a real effort task that asks users to count to number of 1's in a 5x5 matrix of 1's and 0's. This app also contains an Eckel/Grossman risk task, a Cognitive Reflection test, and a handful of survey questions."


class Constants(BaseConstants):
    name_in_url = 'consent'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass
        
class Group(BaseGroup):
    pass #I don't think I need anything here, because it is not a multi-player game.


class Player(BasePlayer):
    consent_time = DateTimeField(null=True)
