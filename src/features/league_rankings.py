from collections import defaultdict
from typing import Dict, Any, List
from src.constants import POINTS
from src.exceptions import InvalidInputException
from src.helpers.validator import validate_match_results


def format_league_table(points_table: List[Dict[str, Any]]) -> str:
    """
    Format the ranked teams into the desired output format.

    Args:
        points_table (list): Sorted list of tuples (team, points).

    Returns:
        str: Formatted ranking string.
    """
    output = [
        f"{rank}. {team}, {points} pt{'s' if points != 1 else ''}"
        for rank, (team, points) in enumerate(points_table, start=1)
    ]
    return "\n".join(output)


def determine_team_rankings(matches: List[Dict[str, Any]]) -> List[Any]:
    """
    Process matches results and calculate the points for each team.

    Args:
        matches (list): List of match results as dictionaries.

    Returns:
        list: Sorted list of tuples (team, points) based on points.
    """
    points_table = defaultdict(int)

    for match in matches:
        team1_name, team1_score = match["team1_name"], match["team1_score"]
        team2_name, team2_score = match["team2_name"], match["team2_score"]

        if team1_score > team2_score:
            points_table[team1_name] += POINTS["WIN"]
            points_table[team2_name] += POINTS["LOSE"]
        elif team1_score < team2_score:
            points_table[team2_name] += POINTS["WIN"]
            points_table[team1_name] += POINTS["LOSE"]
        else:
            points_table[team1_name] += POINTS["DRAW"]
            points_table[team2_name] += POINTS["DRAW"]

    # Return sorted table (descending points, ascending team name)
    return sorted(points_table.items(), key=lambda team: (-team[1], team[0]))


def process_league_rankings(file=None):
    matches_results = []

    if file:
        try:
            with open(file, 'r') as f:
                for line in f:
                    match_results = line.strip()
                    if match_results:
                        try:
                            matches_results.append(validate_match_results(match_results))
                        except InvalidInputException as e:
                            print(f"Invalid match format in file: {e}. Skipping line.")
        except FileNotFoundError:
            print(f"Error: The file '{file}' was not found.")
            return
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return
    else:
        print("Enter match results (or 'done' to exit): ")
        while True:
            match_results = input("> ").strip()

            if match_results.lower() == 'done':
                break

            try:
                matches_results.append(validate_match_results(match_results))
            except InvalidInputException as e:
                print(f"Invalid match format: {e}. Please try again with a valid format. Example: Liverpool 3, Manchester United 0")


    if len(matches_results) == 0:
        print("No matches played.")
        return
    
    print("\nCalculating rankings...\n")
    sorted_table = determine_team_rankings(matches_results)
    print(format_league_table(sorted_table))
