import pandas as pd
import numpy as np
import os

# List of teams with the acroynms associated with the teams
teams = {
    'GreenBay': 'GB',
    'Chicago': 'CHI',
    'Atlanta': 'ATL',
    'Minnesota': 'MIN',
    'Washington': 'WAS',
    'Philadelphia': 'PHI',
    'Buffalo': 'BUF',
    'NYJets': 'NYJ',
    'Baltimore': 'BAL',
    'Miami': 'MIA',
    'SanFrancisco': 'SF',
    'TampaBay': 'TB',
    'KansasCity': 'KC',
    'Jacksonville': 'JAC',
    'Tennessee': 'TEN',
    'Cleveland': 'CLE',
    'LARams': 'LA',
    'Carolina': 'CAR',
    'Detroit': 'DET',
    'Arizona': 'ARI',
    'Cincinnati': 'CIN',
    'Seattle': 'SEA',
    'Indianapolis': 'IND',
    'LAChargers': 'LAC',
    'NYGiants': 'NYG',
    'Dallas': 'DAL',
    'Pittsburgh': 'PIT',
    'NewEngland': 'NE',
    'Houston': 'HOU',
    'NewOrleans': 'NO',
    'Denver': 'DEN',
    'Oakland': 'OAK',
    'St.Louis': 'LA', # Used to be in St. Louis
    'SanDiego': 'LAC', # Used to be in San Diego
    'HoustonTexans': 'HOU' # Different format on some excel files
}

"""
Creates a new process NFL odds data so that it can be used for training and testing the model.
The data needs to be cleaned and the new processed data should include:
home team, away team, the over/under spread (OU), OU the 2nd half of the game (2H), points by both teams, Win Margin, 2H points, and 2H Win Margin
"""
def create_processed_odds_data(path_to_file):
    if(not os.path.isfile(path_to_file)): # Check if the file exist.
        print("Cannot open file " + path_to_file + " because it does not exist!")
        exit(1)

    print("Reading", path_to_file)

    df = pd.read_excel(path_to_file)
    new_cols = ['Home', 'Away', 'OU', 'OU 2H', 'Total Points', 'Win Margin', 'Total Points 2H', 'Win Margin 2H']
    new_data = []
    # print(df.dtypes)
    # print(df.columns)

    print("Processing data for file ", path_to_file)
    for i in range(0, len(df), 2):
        row1 = df.iloc[[i]] # Getting 1st row values. The away team odds data.
        row2 = df.iloc[[i+1]] # Getting 2nd row values. The home team odds data.

        away = row1["Team"][i]
        home = row2["Team"][i+1]

        if(away in teams):
            away = teams[away]
        if(home in teams):
            home = teams[home]

        # print("Away: " + away + " Home: " + home)

        # Getting the OU spread values
        ou_spread = np.sort([row1["Open"][i], row2["Open"][i+1]])
        ou = ou_spread[1]

        # Check if the OU values is indeed a value and not a string. If it is a string, we can skip this data.
        if(isinstance(ou, np.str)):
            continue

        # print(ou)

        # Getting the OU 2H spread values
        ou_spread_2h = np.sort([row1["2H"][i], row2["2H"][i+1]])
        ou_2h = ou_spread_2h[1]

        # Check if the OU 2H values is indeed a value and not a string. If it is a string, we can skip this data.
        if (isinstance(ou_2h, np.str)):
            continue

        # print(ou_2h)

        # Calculating the total points for both teams, the win margin, 2H total points, and 2H win margin.
        total_points = row1["Final"][i] + row2["Final"][i+1]
        win_margin = row1["Final"][i] - row2["Final"][i+1]
        total_points_2h = row1["3rd"][i] + row2["3rd"][i+1] + row1["4th"][i] + row2["4th"][i+1]
        win_margin_2h = row1["3rd"][i] - row2["3rd"][i+1] + row1["4th"][i] + row2["4th"][i+1]

        new_row = [home, away, ou, ou_2h, total_points, win_margin, total_points_2h, win_margin_2h]
        new_data.append(new_row)

    new_processed_data = pd.DataFrame(new_data, columns=new_cols)
    # print(new_processed_data.head())

    print("Processing data is complete!")

    return new_processed_data


if __name__ == '__main__':
    # Preparing directories for data exploring and data processing
    current_dir = os.getcwd()
    nfl_odds_data_path_dir = "..\\data\\nfl_odds_data"
    nfl_odds_data_path = os.path.join(current_dir, nfl_odds_data_path_dir)
    processed_nfl_odds_data_dir = "..\\processed_nfl_odds_data"
    processed_nfl_odds_data_path = os.path.join(current_dir, processed_nfl_odds_data_dir)

    files = os.listdir(nfl_odds_data_path) # Getting the list of files in the nfl_odds_data dir

    # Create the processed nfl odds data directory if it doesn't exist
    if(not os.path.isdir(processed_nfl_odds_data_path)):
        print("Creating ", processed_nfl_odds_data_path)
        os.makedirs(processed_nfl_odds_data_path)
        print("Directory ", processed_nfl_odds_data_path, " is now created\n")

    print("Reading files for data processing")

    # file = files[0]

    for file in files:
        file_name1, file_name2, file_name3 = file.split(" ")
        from_year, to_year = file_name3.split("-")
        to_year = to_year.replace(".xlsx", "")

        # Getting the 1st two digits to get the year for to_year.
        from_year_tmp = int(from_year) / 100
        from_year1, from_year2 = str(from_year_tmp).split(".")
        to_year = from_year1 + to_year
        season_year = from_year + "-" + to_year
        season_year_csv = season_year + "_odds_data.csv"

        path_to_file = os.path.join(nfl_odds_data_path, file)
        new_file = create_processed_odds_data(path_to_file)

        # Saving new processed data
        new_save_file_path = os.path.join(processed_nfl_odds_data_path, season_year_csv)
        print("Saving new processed data to ", new_save_file_path, "\n")
        new_file.to_csv(new_save_file_path)