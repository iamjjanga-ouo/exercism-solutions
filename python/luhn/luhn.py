class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        # Check first validation : not digital number or length
        if self.card_num.isdigit() is False or len(self.card_num) < 2:
            return False

        '''
        valid_sum = 0
        for i, x in enumerate(reversed(self.card_num)):
            x = int(x)
            if i % 2 != 0:
                x *= 2
                x = int(x/10) + x%10
            valid_sum += x
        '''

        ## List Comprehension
        valid_sum = sum(([int((int(x)*2)/10) + (int(x)*2)%10 if i % 2 != 0 else int(x)
                          for i, x in enumerate(reversed(self.card_num))]))

        return bool(valid_sum % 10 == 0)