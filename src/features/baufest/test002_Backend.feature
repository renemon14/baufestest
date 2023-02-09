Feature: Pet store

  Scenario: Add pet
    Given Set Environment EndPoint: "PET_STORE"
    And Set HEADER key: "Content-Type" - value: "application/json"
    And Set api endpoint as: "/pet"
    And load jsonpath: "./features/steps/jsons/addPet.json"
    When Set Method "POST"
    Then Get Response Body, set Name: AddPet
    And Response http code should be "200"
    And Get pet ID
    And Validate Schema Pet Store

  Scenario: Search pet
    Given Set Environment EndPoint: "PET_STORE"
    And Set HEADER key: "Content-Type" - value: "application/json"
    And Set api endpoint as: "/pet/"
    And Set pet ID
    When Set Method "GET"
    Then Get Response Body, set Name: GetPet
    And Response http code should be "200"
    And Validate Schema Pet Store

  Scenario: Modify pet
    Given Set Environment EndPoint: "PET_STORE"
    And Set HEADER key: "Content-Type" - value: "application/json"
    And Set api endpoint as: "/pet"
    And load modify pet json
    When Set Method "PUT"
    Then Get Response Body, set Name: ModifyPet
    And Response http code should be "200"
    And Validate Schema Pet Store