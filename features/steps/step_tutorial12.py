# -*- coding: UTF-8 -*-
# language: de
"""
Based on ``behave tutorial`` (tutorial01)

Funktionalität: Using Languages other than English (tutorial12)

    Szenario: Run a simple test with German Keywords
        Angenommen we have behave installed
        Wenn we implement a test
        Dann behave will test it for us!

    Szenario: Run a simple test completely in German
        Angenommen wir haben "behave" installiert
        Wenn wir einen Test implementieren
        Dann wird "behave" ihn für uns testen!
"""

from behave import given, when, then

# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
@given('wir haben "behave" installiert')
def step(context):
    context.execute_steps(u"we have behave installed")

@when('wir einen Test implementieren')
def step(context):
    context.execute_steps(u"we implement a test")

@then(u'wird "behave" ihn für uns testen!')
def step(context):
    context.execute_steps(u'behave will test it for us!')
