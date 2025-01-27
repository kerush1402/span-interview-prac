import pytest
from src.exceptions import InvalidInputException
from src.features.league_rankings import validate_match_results

def test_valid_match_results():
    match = "TeamA 3, TeamB 2"
    result = validate_match_results(match)
    assert result == {
        "team1_name": "TeamA",
        "team1_score": 3,
        "team2_name": "TeamB",
        "team2_score": 2
    }


def test_invalid_match_results_missing_comma():
    match = "TeamA 3 TeamB 2"
    with pytest.raises(InvalidInputException):
        validate_match_results(match)


def test_invalid_match_results_non_numeric_score():
    match = "TeamA 3, TeamB abc"
    with pytest.raises(InvalidInputException):
        validate_match_results(match)
