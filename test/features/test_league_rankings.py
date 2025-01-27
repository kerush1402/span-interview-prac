from unittest.mock import patch, mock_open
from src.features.league_rankings import determine_team_rankings, format_league_table, process_league_rankings
from src.constants import POINTS


def test_determine_team_rankings():
    matches = [
        {"team1_name": "TeamA", "team1_score": 3, "team2_name": "TeamB", "team2_score": 2},
        {"team1_name": "TeamC", "team1_score": 1, "team2_name": "TeamA", "team2_score": 1},
        {"team1_name": "TeamB", "team1_score": 2, "team2_name": "TeamC", "team2_score": 3},
    ]
    sorted_table = determine_team_rankings(matches)
    expected = [
        ("TeamA", POINTS["DRAW"] + POINTS["WIN"]),
        ("TeamC", POINTS["WIN"] + POINTS["DRAW"]),
        ("TeamB", POINTS["LOSE"] + POINTS["LOSE"])
    ]
    assert sorted_table == expected

def test_format_league_table():
    points_table = [("TeamA", 6), ("TeamB", 3), ("TeamC", 3), ("TeamD", 1)]
    formatted_table = format_league_table(points_table)
    expected_output = "1. TeamA, 6 pts\n2. TeamB, 3 pts\n3. TeamC, 3 pts\n4. TeamD, 1 pt"
    assert formatted_table == expected_output


@patch("builtins.open", mock_open(read_data="TeamA 3, TeamB 2\nTeamC 1, TeamA 1"))
def test_process_league_rankings_from_file():
    with patch("builtins.print") as mock_print:
        process_league_rankings("dummy_file.txt")
        mock_print.assert_any_call("\nCalculating rankings...\n")
        mock_print.assert_any_call("1. TeamA, 4 pts\n2. TeamC, 1 pt\n3. TeamB, 0 pts")


@patch("builtins.input", side_effect=["TeamA 3, TeamB 2", "TeamC 1, TeamA 1", "done"])
@patch("builtins.print")
def test_process_league_rankings_from_input(mock_print, mock_input):
    process_league_rankings()
    mock_print.assert_any_call("\nCalculating rankings...\n")
    mock_print.assert_any_call("1. TeamA, 4 pts\n2. TeamC, 1 pt\n3. TeamB, 0 pts")

@patch('builtins.input', side_effect=['done'])
@patch('builtins.print')
def test_no_matches_played(mock_print, mock_input):
    process_league_rankings()
    mock_print.assert_any_call("No matches played.")
