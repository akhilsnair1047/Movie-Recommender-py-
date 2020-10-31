if __name__ != "__main__":
    # # Importing Modules
    # ## We have used two module to process our data
    # ## 1. pandas: To clean the data and pick out the usable content
    # ## 2. re: This is the module for Regular Expressions, a combination or set of special symbols and character used to
    # ##        find/check the desired pattern
    import pandas as pd
    import re

    # # Creating a dataframe
    # ## Created a dataframe with the csv file named tmdb_5000_movies.csv
    df = pd.read_csv("tmdb_5000_movies.csv")

    # # A view of the dataframe
    # ## See the dataframe is messed a lot
    # df.head()

    # ## lets clean the data
    # # Checking the avalable columns
    # df.columns

    # ## Droping/selecting the desired columns
    df = df[['genres', 'original_language', 'homepage',  'popularity', 'release_date', 'runtime',
             'spoken_languages', 'tagline', 'title', 'vote_average',
             'vote_count']]

    # ## A single row of genres column of the dataframe
    # ## See it is a string, so we need to extract the dictionary out of it to use the "name" key so that we can create a list of genres
    # df["genres"][0]

    def extracted(l, key):
        """
        Takes a string as a input and extracts a list(of dictionaries) out of it.Then it operates on the list to get the values of 
        desired key and appends it to the list.

        Attributes:
                l(string)=String in which to be searched
                key=Key to be searched
        """
        a = eval(re.search(r"\[(.*?)\]", l).group(0))
        li = []
        for i in a:
            li.append(i[key])
        return li

    # ## apply() will operate row by row on the genres column and apply the extracted function on it with the key="name".
    df["genres"] = df["genres"].apply(extracted, key="name")

    # ## After applying the extracted function, this is what we have got, a list of genres.
    # df["genres"][0]

    # ## Now lets check for the language column
    # ## See, again it is in a string form, but this time we are going to extract the language code ("iso_639_1") only
    # df["spoken_languages"][0]

    # ## Now we are applying the extracted functon again but this time we need to extract language code so we pass the key="iso_639_1".
    df["spoken_languages"] = df["spoken_languages"].apply(
        extracted, key="iso_639_1")

    # ## After applying the extracted function, this is what we got, a list of available language codes for a movie.
    # df["spoken_languages"][0]

    # ## It seems that the runtime is in minutes. Lets change it into hours
    # df["runtime"][0]

    df["runtime"] = df["runtime"].apply(lambda x: x/60)

    # ## Now it is appropriate
    # df["runtime"][0]

    # ## Now lets check the final dataframe
    # df.head()

    # # Movie by genre
    # # =========================================================================

    def return_orig_df():
        """This function returns the original dataframe"""
        return df

    def find_movie_by_genre(g, data_frame):
        """This function return the processed dataframe by genre column

           Attribute:
                    g(string): Genre type
                    dataframe(pd.Dataframe): Dataframe to be worked upon"""
        if g == "All":
            return data_frame.sort_values(by="popularity", ascending=False)
        else:
            s = []
            for i in data_frame["genres"]:
                s.append(g in i)
            return data_frame[s].sort_values(by="popularity", ascending=False)

    # find_movie_by_genre("Fantasy")

    # # =========================================================================
    # # Movie by language
    # # =========================================================================

    def find_movie_by_language(l, data_frame):
        """This function return the processed dataframe by language column

           Attribute:
                    l(string): Language code
                    dataframe(pd.Dataframe): Dataframe to be worked upon"""
        if l == "All":
            return data_frame.sort_values(by="popularity", ascending=False)
        else:
            s = []
            for i in data_frame["spoken_languages"]:
                s.append(l in i)
            return data_frame[s].sort_values(by="popularity", ascending=False)

    # find_movie_by_language("ja")

    # # =========================================================================
    # # Movie by rating
    # # =========================================================================

    def find_movie_by_rating(r, data_frame):
        """This function return the processed dataframe by rating column

           Attribute:
                    r(float): Minimum Rating
                    dataframe(pd.Dataframe): Dataframe to be worked upon"""
        if r == "All":
            return data_frame.sort_values(by="vote_average", ascending=False)
        else:
            return data_frame[data_frame["vote_average"] >= r]

    # find_movie_by_rating("All")

    # # =========================================================================
    # # Movie by runtime
    # # =========================================================================

    def find_movie_by_runtime(rt, data_frame):
        """This function return the processed dataframe by runtime column

           Attribute:
                    rt(string): Minimum Runtime
                    dataframe(pd.Dataframe): Dataframe to be worked upon"""
        if rt == "All":
            return df.sort_values(by="popularity", ascending=False)
        else:
            if rt == "1.5hr+":
                return data_frame[(data_frame["runtime"] > 1.5) & (data_frame["runtime"] < 2.0)].sort_values(by="popularity", ascending=False)
            elif rt == "2hr+":
                return data_frame[data_frame["runtime"] >= 2.0].sort_values(by="popularity", ascending=False)

    # movie_by_runtime("2.0+")

    # # =========================================================================
