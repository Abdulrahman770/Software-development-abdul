import random
import string


class Gen:

    def ranGen(chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(15))
