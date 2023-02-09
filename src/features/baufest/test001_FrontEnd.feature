@Test
Feature: Register user in DemoBlaze Website

  Background:
    Given site to navigate: "DEMO-BLAZE"

  Scenario: Register user
    Then register with user: "TestDemo" and pass: "TestDemo2023"

#  Scenario: Login and logout user
#    When login user
#    Then logout user

  Scenario: Add a laptop to cart
    When login user
    Then add laptop to cart
    And validate product in cart
    And logout user
