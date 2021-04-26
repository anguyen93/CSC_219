import numpy as np
import pandas as pd
import os

# Teams that have the old acronyms.
teams = {
    'STL': 'LA',
    'SD': 'LAC'
}
"""
Creates the new processed data for the play by play data for both NFL teams
"""
def create_processed_play_by_play_data(path_to_file):
    if(not os.path.isfile(path_to_file)): # Check if the file exist.
        print("Can open file " + path_to_file + " because it does exist!")
        exit(1)

    print("Reading", path_to_file)
    df = pd.read_csv(path_to_file, low_memory=False)

    # print(df.head(5))
    # print(df.columns)
    # print(df.dtypes)

    new_cols = ["Home", "Away", "Incomplete Passes", "Touchbacks", "Interceptions", "Fumble Forced",
                "Fumble  Forced", "Safety", "Penalty", "Tackled For Loss", "Rush Attempts", "Pass Attempts",
                "Sack", "Touchdowns", "Pass Touchdowns", "Rush Touchdowns", "Extra Point Attempts", "Two Point Attempts",
                "Field Goal Attempts", "Punt Attempts", "Fumble", "Complete Passes"]
    new_data = []
    data = {}

    print("Processing data for file ", path_to_file)
    for i in range(0, len(df)):
        game_id = df["game_id"][i] # Using this to keep track where we are in the file

        # Data values we are interested to create the processed file.
        home = df["home_team"][i]
        away = df["away_team"][i]
        incomplete_passes = df["incomplete_pass"][i]
        touchbacks = df["touchback"][i]
        interceptions = df["interception"][i]
        fumble_forced = df["fumble_forced"][i]
        fumble_not_forced = df["fumble_not_forced"][i]
        safety = df["safety"][i]
        penalty = df["penalty"][i]
        tackled_for_loss = df["tackled_for_loss"][i]
        rush_attempt = df["rush_attempt"][i]
        pass_attempt = df["pass_attempt"][i]
        sack = df["sack"][i]
        touchdown = df["touchdown"][i]
        pass_toucdown = df["pass_touchdown"][i]
        rush_touchdown = df["rush_touchdown"][i]
        extra_point_attempt = df["extra_point_attempt"][i]
        two_point_attempt = df["two_point_attempt"][i]
        field_goal_attempt = df["field_goal_attempt"][i]
        punt_attempt = df["punt_attempt"][i]
        fumble = df["fumble"][i]
        complete_pass = df["complete_pass"][i]

        # If the data contains an NaN value, we can skip that.
        if(np.isnan(incomplete_passes) or np.isnan(touchbacks) or np.isnan(interceptions) or np.isnan(fumble_forced)
                or np.isnan(fumble_not_forced) or np.isnan(safety) or np.isnan(penalty) or np.isnan(tackled_for_loss)
                or np.isnan(rush_attempt) or np.isnan(pass_attempt) or np.isnan(sack) or np.isnan(touchdown)
                or np.isnan(pass_toucdown) or np.isnan(rush_touchdown) or np.isnan(extra_point_attempt) or np.isnan(two_point_attempt)
                or np.isnan(field_goal_attempt) or np.isnan(punt_attempt) or np.isnan(fumble) or np.isnan(complete_pass)):
            continue

        # print(game_id, home, away, incomplete_passes, touchbacks, interceptions, fumble_forced, fumble__forced, safety, penalty, tackled_for_loss, rush_attempt, pass_attempt, sack, touchdown, pass_toucdown, rush_touchdown, extra_point_attempt, two_point_attempt, field_goal_attempt, punt_attempt, fumble, complete_pass)
        # if(fumble_not_forced > 0):
        #     print(fumble_not_forced)

        # If the acronym is either 'STL' and 'SD', it should be 'LA' and 'LAC'.
        if(home == 'STL'):
            home = teams[home]
            # print("home:" + home)
        if(home == 'SD'):
            home = teams[home]
            # print("home: " + home)
        if(away == 'STL'):
            away = teams[away]
            # print("away: " + away)
        if(away == 'SD'):
            away = teams[away]
            # print("away: " + away)

        # Storing the play by play data in a dictionary to keep track which data belongs to which.
        if(game_id not in data):
            data[game_id] = {
                'home': home,
                'away': away,
                'incomplete_passes': incomplete_passes,
                'touchbacks': touchbacks,
                'interceptions': interceptions,
                'fumble_forced': fumble_forced,
                'fumble_not_forced': fumble_not_forced,
                'safety': safety,
                'penalty': penalty,
                'tackled_for_loss': tackled_for_loss,
                'rush_attempt': rush_attempt,
                'pass_attempt': pass_attempt,
                'sack': sack,
                'touchdown': touchdown,
                'pass_toucdown': pass_toucdown,
                'rush_touchdown': rush_touchdown,
                'extra_point_attempt': extra_point_attempt,
                'two_point_attempt': two_point_attempt,
                'field_goal_attempt': field_goal_attempt,
                'punt_attempt': punt_attempt,
                'fumble': fumble,
                'complete_pass': complete_pass
            }
        else:
            data[game_id]['incomplete_passes'] = data[game_id]['incomplete_passes'] + incomplete_passes
            data[game_id]['touchbacks'] = data[game_id]['touchbacks'] + touchbacks
            data[game_id]['interceptions'] = data[game_id]['interceptions'] + interceptions
            data[game_id]['fumble_forced'] = data[game_id]['fumble_forced'] + fumble_forced
            data[game_id]['fumble_not_forced'] = data[game_id]['fumble_not_forced'] + fumble_not_forced
            data[game_id]['safety'] = data[game_id]['safety'] + safety
            data[game_id]['penalty'] = data[game_id]['penalty'] + penalty
            data[game_id]['tackled_for_loss'] = data[game_id]['tackled_for_loss'] + tackled_for_loss
            data[game_id]['rush_attempt'] = data[game_id]['rush_attempt'] + rush_attempt
            data[game_id]['pass_attempt'] = data[game_id]['pass_attempt'] + pass_attempt
            data[game_id]['sack'] = data[game_id]['sack'] + sack
            data[game_id]['touchdown'] = data[game_id]['touchdown'] + touchdown
            data[game_id]['pass_toucdown'] = data[game_id]['pass_toucdown'] + pass_toucdown
            data[game_id]['rush_touchdown'] = data[game_id]['rush_touchdown'] + rush_touchdown
            data[game_id]['extra_point_attempt'] = data[game_id]['extra_point_attempt'] + extra_point_attempt
            data[game_id]['two_point_attempt'] = data[game_id]['two_point_attempt'] + two_point_attempt
            data[game_id]['field_goal_attempt'] = data[game_id]['field_goal_attempt'] + field_goal_attempt
            data[game_id]['punt_attempt'] = data[game_id]['punt_attempt'] + punt_attempt
            data[game_id]['fumble'] = data[game_id]['fumble'] + fumble
            data[game_id]['complete_pass'] = data[game_id]['complete_pass'] + complete_pass

    # print(data[2009091000]['home'], data[2009091000]['away'], data[2009091000]['incomplete_passes'], data[2009091000]['touchbacks'],data[2009091000]['interceptions'], data[2009091000]['fumble_forced'],
    #   data[2009091000]['fumble_not_forced'], data[2009091000]['safety'],data[2009091000]['penalty'], data[2009091000]['tackled_for_loss'], data[2009091000]['rush_attempt'], data[2009091000]['pass_attempt'],
    #   data[2009091000]['sack'], data[2009091000]['touchdown'], data[2009091000]['pass_toucdown'], data[2009091000]['rush_touchdown'], data[2009091000]['extra_point_attempt'], data[2009091000]['two_point_attempt'],
    #   data[2009091000]['field_goal_attempt'], data[2009091000]['punt_attempt'], data[2009091000]['fumble'], data[2009091000]['complete_pass'])
    # print("fumble_not_forced, ", data[2009091000]['fumble_not_forced'])
    # print("extra_point_attempt, ", data[2009091000]['extra_point_attempt'])
    # print(data)

    # Getting data from dictionary and appending them to a list to be used to create the dataframe
    # for the new processed data.
    for game_id in data:
        new_row = [data[game_id]['home'], data[game_id]['away'], data[game_id]['incomplete_passes'], data[game_id]['touchbacks'],data[game_id]['interceptions'], data[game_id]['fumble_forced'],
      data[game_id]['fumble_not_forced'], data[game_id]['safety'],data[game_id]['penalty'], data[game_id]['tackled_for_loss'], data[game_id]['rush_attempt'], data[game_id]['pass_attempt'],
      data[game_id]['sack'], data[game_id]['touchdown'], data[game_id]['pass_toucdown'], data[game_id]['rush_touchdown'], data[game_id]['extra_point_attempt'], data[game_id]['two_point_attempt'],
      data[game_id]['field_goal_attempt'], data[game_id]['punt_attempt'], data[game_id]['fumble'], data[game_id]['complete_pass']]

        new_data.append(new_row)

    new_processed_data = pd.DataFrame(new_data, columns=new_cols)
    print("Processing data is complete!")

    return new_processed_data

if __name__ == '__main__':
    # Preparing directories for data exploring and data processing
    current_dir = os.getcwd()
    nfl_play_by_play_data_dir = "..\\data\\play_by_play_data\\regular_season"
    nfl_play_by_play_data_path = os.path.join(current_dir, nfl_play_by_play_data_dir)
    processed_nfl_play_by_play_data_dir = "..\\processed_nfl_play_by_play_data"
    processed_nfl_play_by_play_data_path = os.path.join(current_dir, processed_nfl_play_by_play_data_dir)

    files = os.listdir(nfl_play_by_play_data_path)  # Getting the list of files in the play_by_play_data dir in the regular_season

    # Create the processed nfl odds data directory if it doesn't exist
    if (not os.path.isdir(processed_nfl_play_by_play_data_path)):
        print("Creating ", processed_nfl_play_by_play_data_path)
        os.makedirs(processed_nfl_play_by_play_data_path)
        print("Directory ", processed_nfl_play_by_play_data_path, " is now created\n")

    # file = files[0]

    for file in files:
        # Getting the season year for the new file.
        file_name1, file_name2, file_name3 = file.split("_")
        from_year = file_name3.replace(".csv", "")
        to_year = int(from_year) + 1
        to_year = str(to_year)
        season_year = from_year + "-" + to_year
        season_year_csv = season_year + "_play_by_play_data.csv"

        path_to_file = os.path.join(nfl_play_by_play_data_path, file)
        new_file = create_processed_play_by_play_data(path_to_file)

        # Saving new processed data
        new_save_file_path = os.path.join(processed_nfl_play_by_play_data_path, season_year_csv)
        print("Saving new processed data to ", new_save_file_path, "\n")
        new_file.to_csv(new_save_file_path)