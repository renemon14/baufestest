from behave import *

@given('Set pet ID')
def step_impl(self):
    self.variablesTemp['id'] = self.variablesTemp['petID']