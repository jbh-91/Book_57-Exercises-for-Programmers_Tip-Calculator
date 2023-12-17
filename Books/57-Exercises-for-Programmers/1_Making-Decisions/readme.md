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


[^1]: test-driven development