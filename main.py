import sys

from src.features.league_rankings import process_league_rankings

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else ""
    
    process_league_rankings(filename)
