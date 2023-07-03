Feature: Weather Shopper

  Scenario: Purchase sunscreen or moisturizer based on temperature
    Given User is on Weather Shopper website
    When User gets the temperature
    And User chooses to buy sunscreen or moisturizer based on the temperature
    And User reads instructions and adds the product accordingly
    And User verifies the cart
    And User makes a payment
    Then User completes the purchase
