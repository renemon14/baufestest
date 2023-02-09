from behave import *

@then('Get pet ID')
def step_impl(self):
    self.variablesTemp['petID'] = self.responseParse['id']