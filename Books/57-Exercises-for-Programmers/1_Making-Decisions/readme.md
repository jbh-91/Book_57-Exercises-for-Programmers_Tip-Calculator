# Project: Tip Calculator
**Goal:** Learning TDD[^1]


## Task
Create a Tip-Calculator

### Input
* bill amount
* tip rate

### Output
* calculate the tip

### Conversions
* tip amount
* total amount

## Psuedo code
```
TipCalculator
    Initialize billAmount to 0
    Initialize tip to 0
    Initialize tipRate to 0
    Initialize total to 0

    Prompt for billAmount with "What is the bill amount?"
    Prompt for tipRate with "What is the tip rate?"

    convert billAmount to a number
    convert tipRate to a number

    tip = billAmount * (tipRate / 100)
    round tip up to nearest cent
    total = billAmount + tip

    Display "Tip: €" + tip
    Display "Total: €" + total
End

```

## Constraints
* Enter the tip as a percentage.
  * For example, a 15 % tip would be entered as 15, not 0.15.
  * The program should handle the division
* Round fractions of a cent up to the next cent


## Tests
* Basic functionality
* Tip as percantage, not decimal
* Round-up
* Only two decimal places

### Assertion-Test: Basic functionality
#### Test-Plan:
Inputs:
Expected result:
Actual result:

### Assertion-Test: Tip as percantage
#### Test-Plan:
Inputs:
Expected result:
Actual result:

### Assertion-Test: Round-up
* converted amounts need to be rounded up, since we're using currency
#### Test-Plan:
Inputs:
Expected result:
Actual result:

### Assertion-Test: Only two decimal places
#### Test-Plan: 
Inputs:
Expected result:
Actual result:

[^1]: test-driven development