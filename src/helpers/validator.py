from typing import Dict, Any
from src.exceptions import InvalidInputException

def validate_match_results(match: str) -> Dict[str, Any]:
    """
    Validate single match results input string.

    Args:
        match (str): Match result in the format 'TeamA score, TeamB score'.

    Returns:
        dict: Match data as a dictionary.

    Raises:
        InvalidInputException: If the input format is invalid.
    """
    if match.count(",") != 1:
        raise InvalidInputException("Match data must contain exactly one comma")

    try:
        team1_data, team2_data = map(str.strip, match.split(","))
        team1_name, team1_score = team1_data.rsplit(" ", 1)
        team2_name, team2_score = team2_data.rsplit(" ", 1)
    except ValueError:
        raise InvalidInputException("Each team data must include a name and a score")

    try:
        return {
            "team1_name": team1_name,
            "team1_score": int(team1_score),
            "team2_name": team2_name,
            "team2_score": int(team2_score),
        }
    except ValueError:
        raise InvalidInputException("Scores must be valid numbers")
