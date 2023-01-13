Feature: Cucumber example

  Scenario: Count letters in a name
    Given my name is Ellie
    When I calculate the length of my name
    Then There are 5 letters in total

  Scenario: This also counts letters in a name
    Given my name is Jasmine
    When I count the letters in my name
    Then There are 7 letters in total

  Scenario Outline: Count chars in a string '<word>'
    Given my string is <word>
    When I count the letters in a string
    Then There are <count> letters in total

    Examples:
    |word         |count  |
    |Psychiatrist | 12    |
    |Requirements | 12    |
    |cantaloupe   | 10    |
    |concatenation| 13    |