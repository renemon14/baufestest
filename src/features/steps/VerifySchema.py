from behave import *
from assertpy import assert_that


@then('Validate Schema Pet Store')
def step_impl(self):
    assert_that(type(self.responseParse['id'])).is_equal_to(int)
    assert_that(type(self.responseParse['category']['id'])).is_equal_to(int)
    assert_that(type(self.responseParse['category']['name'])).is_equal_to(str)
    assert_that(type(self.responseParse['name'])).is_equal_to(str)