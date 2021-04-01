import os
import sys
import pandas as pd

class Games():

    def __init__(self, game_id, game_source, game_title, game_url, game_genre,
       game_size, game_size_unit, game_release_date, insert_date,game_page ):
       self.game_id = game_id
       self.game_source = game_source
       self.game_title = game_title
       self.game_url = game_url
       self.game_genre = game_genre
       self.game_size = game_size
       self.game_size_unit = game_size_unit
       self.game_release_date = game_release_date
       self.insert_date = insert_date
       self.game_page = game_page
    
    def add_games_to_csv(self):
        pass

if __name__=="__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print("Service : ", current_dir)
    sys.path.append(os.path.abspath(current_dir + "..\..\files"))
    # files = os.listdir(cwd)  # Get all the files in that directory
    read_csv = pd.read_csv("list_ovagames.csv")
    df = pd.DataFrame(read_csv)
    print(df.columns)

    # print(cwd)


