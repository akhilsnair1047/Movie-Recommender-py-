if __name__ != "__main__":
    import pickle
    import os

    def enter_autho_details(U_N, E, P, G):
        """This function takes 5 parameters and dump it into a pickle file.

           Attributes:
                    U_N(string):Username
                    E(string):Email
                    P(string):Password
                    G(int):Gender (1:Male,2:Female)"""
        d = {"Username": U_N, "Email": E,
             "Password": P, "Gender": G}
        with open(os.path.dirname(os.path.abspath(__file__))+r"\pass_database", "ab+") as f:
            pickle.dump(d, f)

    def check_authorisation(key, val):
        """This function takes 2 parameters and validate them according to the file pass_database.

           Attributes:
                    key(string):Key to be validated
                    val(string):Password to be validated
        """
        data = []
        with open(os.path.dirname(os.path.abspath(__file__))+r"\pass_database", 'rb') as fr:
            try:
                while True:
                    data.append(pickle.load(fr))
            except EOFError:
                pass

        for i in data:
            if i["Username"] == key:
                if i["Password"] == val:
                    return "yes"
                else:
                    return "wrong password"
        return "not_authorised"
