Feature: DuckDuckGo Web Browsing
  As a web user,
  I want to find information online,
  So I can learn new things.

  Background:
    Given the DuckDuckGo home page is displayed

  Scenario: Basic DuckDuckGo Search

    When the user searches for "Python Pandas"
    Then results are shown for "Python Pandas"

  Scenario: Basic DuckDuckGo Search for Selenium

    When the user searches for "Selenium"
    Then results are shown for "Selenium"

  Scenario Outline: Basic DuckDuckGo with outline
    When the user searches for "<text>"
    Then results are shown for "<text>"

    Examples:
      | text   |
      | python |
      | java   |