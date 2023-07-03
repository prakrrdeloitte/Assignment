Feature: Flipkart Travel Section

  Scenario: Validate total price for flights
    Given User is on Flipkart website
    When User navigates to Travel section
    And User selects round trip, dates, and locations
    And User clicks on search
    Then User validates the total price for flights
