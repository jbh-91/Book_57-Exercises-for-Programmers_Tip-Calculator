# Project: Tip Calculator

This is a task from the book **Exercises for Programmers** – *57 Challenges to Develop Your Coding Skills* by Brian P. Hogan, a part of **[The Pragmatic Programmers](https://pragprog.com/titles/bhwb/exercises-for-programmers/)** series
> **Goal:** Learning TDD[^1]

## Task

Create a Tip-Calculator

### Input

* bill amount
* tip rate

### Conversions

* calculate the tip

### Output

* tip amount
* total amount

## Psuedo code

```text
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
* round to nearest cent
* Only two decimal places
* Tip rate and bill amount not negative
* total larger than bill amount

### Assertion-Test: Basic functionality

**Test-Plan:**

```text
Inputs:
  bill amount: 10
  tip rate: 15
Expected result:
  Tip: 1.50 €
  Total: 11.50 €
```

### Assertion-Test: Tip as percantage

**Test-Plan:**

```text
Inputs:
  tip rate: 15
Expected result:
  tip >= 0
  tip is not float
```

### Assertion-Test: Rounding

**Test-Plan:**

```text
Inputs:
  bill amount: 11.25
  tip rate: 15
Expected result:
  Tip: 1.69 € (from 1.6875)
  Total: 12.94 € (from 12.9375)
```

### Assertion-Test: Only two decimal places

**Test-Plan:**

```text
Inputs:
  bill amount: 11.25
  tip rate: 15
Expected result:
  Tip: 1.69 € (from 1.6875)
  Total: 12.94 € (from 12.9375)
  ```

### Assertion-Test: Tip rate and bill amount not negative

**Test-Plan:**

```text
Inputs:
  bill amount: -11.25
  tip rate: -10
Expected result:
  bill amount >= 0
  tip rate >= 0
```

### Assertion-Test: total larger than bill amount

**Test-Plan:**

```text
Inputs:
  bill amount: 10
  tip rate: 15
Expected result:
  Total >= bill amount
```

## Additional, optional Tasks

* only numbers can be entered for the bill amount and tip rate
  * Use Exceptions to display an appropiate message
  * Instead of using an Errormessage, keep asking until the input is correct
* Don't allow to input negative numbers
* Break the program into functions that do computations
* Add a gui
* add a slider (satisfaction with the server), using a range between 5 % and  20 %

[^1]: test-driven development
