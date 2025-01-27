## Span Interview Practical

This is a python project3 project. This project evaluates a list of Football matches played by teams (provided by stdin or file). A team is awarded points based on the outcome of a match. For example:
- 3 points to the team that WINS
- 1 points to both teams if DRAW
- 0 points to the team that loses

Teams are then ranked (high -> low) based on the points they have accumulated. In cases where teams have the same point, they will be sorted alphabetically.

## Testing

To run unit tests:
```
make test
```

## Running 

To run programma with mock/test data from file:
```
make run file=TestData.txt
```

To run program where user provides input to stdin:
```
make run
```

## Formatting

To run pylint:
```
make lint
```

## Requirements

This package runs with python3 and pytest.