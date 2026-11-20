class Enquete:
    def __init__(self, suspect):
        self.titre = suspect
        self.detective = None
        self.suspects = []
        self.lieux = []
        self.indices = []
        self.coupables = []
        self.resolue = False
