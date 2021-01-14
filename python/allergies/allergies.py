class Allergies:
    score = 1
    al_db = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8,
             'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128}

    def __init__(self, score):
        self.score = score % 256  # When input score is Over than 255

    def allergic_to(self, item):
        return item in self.lst   # IS item in list of allergen?

    @property
    def lst(self):
        res = []
        for k, v in list(self.al_db.items())[::-1]:  # [128, 64, 32, 16, 8, 4, 2, 1]
            if self.score - v >= 0:                  # EX. when self.score = 248
                res.append(k)                        # 128 -> matched, self.score (248 - 128) = 120
                self.score -= v                      # 64 -> matched              (120 - 64) = 56
                                                     # 32 -> matched              (56 - 32) = 24
        return res                                   # 16 -> matched              (24 - 16) = 8
                                                     # 8 -> matched               (8 - 8) = 0 then, no more calcuation
                                                     # returned list = ["strawberries", "tomatoes", "chocolate", "pollen", "cats"]