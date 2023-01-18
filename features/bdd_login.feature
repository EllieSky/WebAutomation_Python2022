feature:Basic BDD Login

  Scenario: As an admin I should be able to login
  Given I open the http://http://hrm-online.portnov.com.url
  When I enter text admin into the elements id=username
  And I enter text password into the element id=txtPassword
  And I click the id=btnLogin element
  Then the url should contain/pim/viewEmployeeList
  And I get the text from element id=welcome
  And the text should be Welcome Admin
