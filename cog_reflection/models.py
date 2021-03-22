from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

class Constants(BaseConstants):
    name_in_url = 'cog'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass
        
class Group(BaseGroup):
    pass #I don't think I need anything here, because it is not a multi-player game.


class Player(BasePlayer):
    cog_reflect_one_correct = models.BooleanField()
    cog_reflect_two_correct = models.BooleanField()

    cog_reflect_one_input = models.FloatField(
        doc="User input for the second Cognitive Reflection Test Question.",
        min=0
    )

    cog_reflect_two_input = models.FloatField(
        doc="User input for the third Cognitive Reflection Test Question.",
        min=0
    )
