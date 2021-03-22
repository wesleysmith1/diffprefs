from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass
        
class Group(BaseGroup):
    pass #I don't think I need anything here, because it is not a multi-player game.

regret_choices = [
    [1, 'Strongly agree'],
    [2, 'Agree'],
    [3, 'Neither agree nor disagree'],
    [4, 'Disagree'],
    [5, 'Strongly disagree'],
]

class Player(BasePlayer):
    gender = models.StringField(
        choices=['Male','Female','Other','Prefer Not To Answer'],
        doc="Self-reported gender of the participant."
    )

    age = models.PositiveIntegerField(
        doc = "Self-reported age of participant.",
        min=0,
        max=100
    )

    ethnicity = models.StringField(
        doc = "Self-reported ethinicity of the participant.",
        choices = ['White','Hispanic or Latino', 'African American', 'Native American or American Indian', 'Asian', 'Pacific Islander', 'Other', 'Prefer Not To Answer']
    )

    marital_status = models.StringField(
        doc = "Self-rerported civil status of participant.",
        choices=['Single, Never Married', 'Married/Domestic Partnership', 'Widowed', 'Divorced']
    )

    employment = models.StringField(
        doc = "Employment status of participant.",
        choices = ['Yes','No']
    )

    insurance = models.StringField(
        doc = "Insured status of participant.",
        choices = ['Yes','No']
    )

    annual_income = models.StringField(
        doc = "Self-reported household annual income of participant.",
        choices = [ '$0-$5,000','$5,001-$10,000','$10,001-$15,000','$15,001-$20,000','$20,001-$25,000','$25,001-$30,000',
        '$30,001-$35,000','$35,001-$40,000','$40,001-$45,000','$45,001-$50,000','$50,001-$55,000',
        '$55,001-$60,000','$60,001-$65,000','$65,001-$70,000','$70,001-$75,000','$75,001-$80,000','$80,001-$85,000',
        '$85,001-$90,000','$90,001-$95,000','$95,001-$100,000','$100,001-$105,000','$105,001-$110,000',
        '$110,001-$115,000','$115,001-$120,000','$120,001-$125,000','Greater Than $125,000',
        ]
    )

    credit_card = models.StringField(
        doc = "Does the participant have a credit card?",
        choices = ['Yes','No']
    )

    participant_education = models.StringField(
        doc =  "Highest level of education you have completed.",
        choices = ['1st grade','2nd grade','3rd grade', '4th grade','5th grade','6th grade','7th grade',
        '8th grade', '9th grade', '10th grade', '11th grade', 'Graduated High School', '1 year of college',
        '2 years of college','3 years of college', 'Graduated from college', 'Some graduate school', 'Completed graduate school']

    )

    parent_education = models.StringField(
        doc =  "Highest level of education one of the parents of the participant completed.",
        choices = ['1st grade','2nd grade','3rd grade', '4th grade','5th grade','6th grade','7th grade',
        '8th grade', '9th grade', '10th grade', '11th grade', 'Graduated High School', '1 year of college',
        '2 years of college','3 years of college', 'Graduated from college', 'Some graduate school', 'Completed graduate school']

    )

    smoke = models.StringField(
        doc = "Does the participant smoke?",
        choices = ['Yes','No']
    )

    alcohol = models.StringField(
        doc = "Does the participant drink alcohol?",
        choices = ['Yes','No']
    )

    experimentplay = models.StringField(
        doc = "Has the participant played an economic experiment",
        choices = ['Yes','No']
    )

    hourly_wage = models.FloatField(
        doc =  "Hourly wage.",
        min=0
    )

    regret_one = models.IntegerField(
        choices=regret_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I made the right choices during the experiment."
    )

    regret_two = models.IntegerField(
        choices=regret_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I regret the choices I made during the experiment."
    )

    regret_three = models.IntegerField(
        choices=regret_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I would make the same choices in the experiment if I had to do it over again."
    )

    regret_four = models.IntegerField(
        choices=regret_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="My decisions during the experiment were wise."
    )
