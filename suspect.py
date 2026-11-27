from modeles.personnage import Personnage
class Suspect(Personnage):
    def __init(self, nom, description, age, profession,alibi
               , alibi_est_vrai, secret, role, presentation
               , nervosite) :
        super().__init__(nom, description, age, profession)
        self.__alibi = alibi
        self.__alibi_est_vrai = alibi_est_vrai
        self.__secret = secret
        self.__role = role
        self.__presentation = presentation  #une petite presentation sur le suspect
        self.setNervosite(nervosite)        # l'element cle 
        self.__questions = []   
        self.reactions = {}     #code d'indice -> replique
        self.__indices_confrontes = set()  #code deja montres
        self.__indices_lies = []    #objets indice

    

