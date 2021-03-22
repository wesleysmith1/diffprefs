from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import datetime

# constants from other modules
from my_matrix_ret.models import Constants as MainConstants

class payment(Page):
    def vars_for_template(self):
        # if(self.player.card_color=='GREEN'):

        #     if(self.player.investment_choice): 
        #         self.player.participant.vars['investment_spending'] = Constants.investment_cost
        #     else: 
        #         self.player.participant.vars['investment_spending'] = 0

        #     self.player.participant.vars['second_task_earnings'] = self.player.problems_correct_second_task * Constants.green_card_payoff
        # elif(self.player.card_color=='RED' and self.player.investment_choice):
        #     self.player.participant.vars['second_task_earnings'] = self.player.problems_correct_second_task * Constants.investment_effectiveness
        #     self.player.participant.vars['investment_spending'] = Constants.investment_cost
        # else:
        #     self.player.participant.vars['second_task_earnings'] = self.player.problems_correct_second_task * Constants.red_card_modifier
        #     self.player.participant.vars['investment_spending'] = 0

        correct_first_task = round(self.player.participant.vars['problems_correct_first_task'])
        attempted_first_task = round(self.player.participant.vars['problems_attempted_first_task'])
        correct_second_task = round(self.player.participant.vars['problems_correct_second_task'])
        attempted_second_task = round(self.player.participant.vars['problems_attempted_second_task'])
        card_color = self.player.participant.vars['card_color']
        second_task_earnings = round(self.player.participant.vars['second_task_payoff'],2)
        first_task_payoff = self.player.participant.vars['first_task_payoff']
        participation_fee = MainConstants.participation_fee
        investment_spending = self.player.participant.vars['investment_spending']
        risk_payment = self.player.participant.vars['risk_payment']
        total_prev_earnings = first_task_payoff + participation_fee - investment_spending + second_task_earnings + risk_payment

        return {
            'num_correct_first_task': correct_first_task,
            'problems_attempted_first_task': attempted_first_task,
            'num_correct_second_task': correct_second_task,
            'problems_attempted_second_task': attempted_second_task,
            'card_color' : card_color,
            'second_task_earnings': second_task_earnings,
            'first_task_payoff' : first_task_payoff,
            'participation_fee' : participation_fee,
            'investment_spending':investment_spending,
            'total_prev_earnings': total_prev_earnings,
            'risk_payment': risk_payment,
        }

page_sequence = [payment]