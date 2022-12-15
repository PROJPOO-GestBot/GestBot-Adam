class Susers():

    def __init__(self, bot):
        self.bot = bot

    #calcul lvl return boolean value. Either change function name, or return type
    def calcul_lvl(self, lvl, xp):
        if xp >= lvl * 10:
            return True
        return False

    #function name must be an action. Level must be changed.
    def level(self, user_id):
        NotImplemented  # requete SQL contenent le niveau

    def add_xp(self, number_xp, user_id):
        # requete SQL
        lvl = Susers.level(user_id)
        xp_total = NotImplemented  # requete SQL pour optenire le nombre total de XP
        if Susers.calcul_lvl(lvl, xp_total):
            NotImplemented  # requete SQL pour augmenter le niveau de 1
        return

    def remove_xp(self, number_xp, user_id):
        # requete SQL
        return
