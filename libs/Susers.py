class Susers():
    
    def __init__(self, bot):
        self.bot = bot
        
    def CalculLvl(lvl, xp):
        if (xp >= lvl *10):
            return True
        return False
    
    def Level(userID):
        NotImplemented
        return #requete SQL contenent le niveau
    
    def AddXP(numberXP,userID):
        #requete SQL
        lvl = Susers.Level(userID)
        xpTotal = NotImplemented #requete SQL pour optenire le nombre total de XP
        if Susers.CalculLvl(lvl, xpTotal):
            NotImplemented # requete SQL pour augmenter le niveau de 1
        return 
        
    def RemoveXP(numberXP, userID):
        # requete SQL
        return
    
   
    

    
