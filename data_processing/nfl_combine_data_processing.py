import pandas as pd
import os

'''
Creates the combined NFL dataset by combining the odds data and play by play data.
'''
def create_combined_nfl_data(odds_data_file, play_by_play_data_file):
    # print(odds_data_file)
    # print(play_by_play_data_file)

    new_data = [] # Storing new data to be used to create the combined dataset

    # Combined columns for the dataset
    new_cols = ["Home", "Away", "OU", "OU 2H", "Total Points", "Win Margin", "Total Points 2H", "Win Margin 2H",
                "Incomplete Passes", "Touchbacks", "Interceptions", "Fumble Forced",
                "Fumble Not Forced", "Safety", "Penalty", "Tackled For Loss", "Rush Attempts", "Pass Attempts",
                "Sack", "Touchdowns", "Pass Touchdowns", "Rush Touchdowns", "Extra Point Attempts",
                "Two Point Attempts", "Field Goal Attempts", "Punt Attempts", "Fumble", "Complete Passes"]

    # Checking if the files exist.
    if(not os.path.isfile(odds_data_file)):
        print(odds_data_file + " does not exist.")
        exit(1)

    if(not os.path.isfile(play_by_play_data_file)):
        print(play_by_play_data_file + " does not exist.")
        exit(1)

    # Reads the dataset files
    df_odds = pd.read_csv(odds_data_file)
    df_pbp = pd.read_csv(play_by_play_data_file)

    # print(len(df_odds))
    # print(len(df_pbp))
    print("Reading: " + odds_data_file)
    print("Reading: " + play_by_play_data_file)

    ''' 
    Loops through each of the odds and pbp datasets and merges both datasets if 
    the data are available in both. 
    '''
    for i in range(0, len(df_odds)):
        # Setting up odds datasets
        odds_data = {
            'home': df_odds['Home'][i],
            'away': df_odds['Away'][i],
            'ou': df_odds['OU'][i],
            'ou_2h': df_odds['OU 2H'][i],
            'total_points': df_odds['Total Points'][i],
            'win_margin': df_odds['Win Margin'][i],
            'total_points_2h': df_odds['Total Points 2H'][i],
            'win_margin_2h': df_odds['Win Margin 2H'][i]
        }

        #print(odds_data['home'], odds_data['away'], odds_data['ou'], odds_data['ou_2h'], odds_data['total_points'], odds_data['win_margin'], odds_data['total_points_2h'], odds_data['win_margin_2h'])
        for j in range(0, len(df_pbp)):
            # Sets up the pbp datasets
            pbp_data = {
                'home': df_pbp['Home'][j],
                'away': df_pbp['Away'][j],
                'incomplete_passes': df_pbp['Incomplete Passes'][j],
                'touchbacks': df_pbp['Touchbacks'][j],
                'interceptions': df_pbp['Interceptions'][j],
                'fumble_forced': df_pbp['Fumble Forced'][j],
                'fumble_not_forced': df_pbp['Fumble Not Forced'][j],
                'safety': df_pbp['Safety'][j],
                'penalty': df_pbp['Penalty'][j],
                'tackled_for_loss': df_pbp['Tackled For Loss'][j],
                'rush_attempts': df_pbp['Rush Attempts'][j],
                'pass_attempts': df_pbp['Pass Attempts'][j],
                'sack': df_pbp['Sack'][j],
                'touchdowns': df_pbp['Touchdowns'][j],
                'pass_touchdowns': df_pbp['Pass Touchdowns'][j],
                'rush_touchdowns': df_pbp['Rush Touchdowns'][j],
                'extra_point_attempts': df_pbp['Extra Point Attempts'][j],
                'two_point_attempts': df_pbp['Two Point Attempts'][j],
                'field_goal_attempts': df_pbp['Field Goal Attempts'][j],
                'punt_attempts': df_pbp['Punt Attempts'][j],
                'fumble': df_pbp['Fumble'][j],
                'complete_passes': df_pbp['Complete Passes'][j]
            }

            # print(pbp_data['home'], pbp_data['away'], pbp_data['incomplete_passes'], pbp_data['touchbacks'], pbp_data['interceptions'], pbp_data['fumble_forced'],
            #       pbp_data['fumble_not_forced'], pbp_data['safety'], pbp_data['penalty'], pbp_data['tackled_for_loss'], pbp_data['rush_attempts'],
            #       pbp_data['pass_attempts'], pbp_data['sack'], pbp_data['touchdowns'], pbp_data['pass_touchdowns'], pbp_data['rush_touchdowns'], pbp_data['extra_point_attempts'],
            #       pbp_data['two_point_attempts'], pbp_data['field_goal_attempts'], pbp_data['punt_attempts'], pbp_data['fumble'], pbp_data['complete_passes'])

            # This checks if both datasets have the same home and away team. If they do, then it merges the dataset.
            # Otherwise, it will not include it in the final file.
            if(pbp_data['home'] == odds_data['home'] and pbp_data['away'] == odds_data['away']):
                # print("pbp home: " + pbp_data['home'])
                # print("odds home: " + odds_data['home'])
                # print("pbp away: " + pbp_data['away'])
                # print("odds away: " + odds_data['away'])
                new_row = [pbp_data['home'], pbp_data['away'], odds_data['ou'], odds_data['ou_2h'],
                           odds_data['total_points'], odds_data['win_margin'], odds_data['total_points_2h'],
                           odds_data['win_margin_2h'], pbp_data['incomplete_passes'], pbp_data['touchbacks'],
                           pbp_data['interceptions'], pbp_data['fumble_forced'], pbp_data['fumble_not_forced'],
                           pbp_data['safety'], pbp_data['penalty'], pbp_data['tackled_for_loss'], pbp_data['rush_attempts'],
                           pbp_data['pass_attempts'], pbp_data['sack'], pbp_data['touchdowns'], pbp_data['pass_touchdowns'],
                           pbp_data['rush_touchdowns'], pbp_data['extra_point_attempts'], pbp_data['two_point_attempts'],
                           pbp_data['field_goal_attempts'], pbp_data['punt_attempts'], pbp_data['fumble'], pbp_data['complete_passes']]

                new_data.append(new_row)

    new_processed_data = pd.DataFrame(new_data, columns=new_cols)
    # print(new_processed_data.head(1))
    # print(new_processed_data.tail(1))
    print("Processing is complete!")

    return new_processed_data


if __name__ == '__main__':
    # Preparing directories for data exploring and data processing
    current_dir = os.getcwd()
    nfl_combined_data_dir = os.path.join(current_dir, "..\\nfl_combined_data")

    processed_nfl_odds_data_dir = os.path.join(current_dir, "..\\processed_nfl_odds_data")
    # print(processed_nfl_odds_data_dir)
    processed_nfl_play_by_play_data_dir = os.path.join(current_dir, "..\\processed_nfl_play_by_play_data")
    # print(processed_nfl_play_by_play_data_dir)

    if(not os.path.isdir(nfl_combined_data_dir)):
        print("Creating " + nfl_combined_data_dir + " directory")
        os.makedirs(nfl_combined_data_dir)
        print("The directory is created.")

    if (not os.path.isdir(processed_nfl_odds_data_dir)):
        print(processed_nfl_odds_data_dir + " does not exist!")

    if (not os.path.isdir(processed_nfl_play_by_play_data_dir)):
        print(processed_nfl_play_by_play_data_dir + " does not exist!")

    processed_odds_data_files = os.listdir(processed_nfl_odds_data_dir)
    processed_play_by_play_data_files = os.listdir(processed_nfl_play_by_play_data_dir)
    file_count = len(processed_odds_data_files)

    # print(processed_odds_data_files[0])
    # print(processed_play_by_play_data_files[0])

    print("Reading files for data processing")

    for i in range(0, file_count):
        processed_odds_data_file_path = os.path.join(processed_nfl_odds_data_dir, processed_odds_data_files[i])
        processed_play_by_play_data_file_path = os.path.join(processed_nfl_play_by_play_data_dir, processed_play_by_play_data_files[i])
        new_file = create_combined_nfl_data(processed_odds_data_file_path, processed_play_by_play_data_file_path)
        # print(new_file.head(1))
        # print(new_file.tail(1))

        # Getting the year of the file so that it can be used to name the new file.
        year,name1,name2 = processed_odds_data_files[i].split("_")
        new_file_name = year + " nfl.xlsx"

        # Saves the new file to the location.
        new_file_path = os.path.join(nfl_combined_data_dir, new_file_name)
        print("Saving new processed data to ", new_file_path, "\n")
        new_file.to_excel(new_file_path)
