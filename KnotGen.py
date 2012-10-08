import random
import unittest


class KnotGen(object):
    def __init__(self):
        self.codex = '0123456789ABCFGHJKMNPQRTVWXZ'
        self.knots = [0, 75, 78, 79, 84, 83]  # KNOTS ASCII w/ buffer
        random.seed(self)

    def gen_token(self, position):
        if 1 > position < 5:
            raise ValueError
        key = 'knots'
        while not self.check_token(key, position):
            key = "".join([random.choice(self.codex) for x in xrange(5)])
        return key

    def gen_key(self):
        tokens = [self.gen_token(x) for x in xrange(1, 6)]
        return "{}-{}-{}-{}-{}".format(*tokens)

    def check_token(self, token, position):
        try:
            token = [x for x in token if token.count(x) == 1]
            if not len(token) == 5:
                raise ValueError
            value = sum([self.codex.index(x) for x in token]) * 2
            if not value + position == self.knots[position]:
                raise ValueError
        except ValueError:
            return False
        return True

    def check_key(self, key):
        try:
            if len(key) < 29:
                raise ValueError
            tokens = [x for x in key.split('-') if len(x) == 5]
            if not len(tokens) == 5:
                raise ValueError

            tokenIndex = 0
            for token in tokens:
                tokenIndex += 1
                if not self.check_token(token, tokenIndex):
                    raise ValueError

        except ValueError:
            return False

        return True


class KnotGen_Test(unittest.TestCase):
    def setUp(self):
        self.knot = KnotGen()

    def test_bad_key(self):
        self.assertFalse(
            self.knot.check_key("This is very wrong"))
        self.assertFalse(
            self.knot.check_key('This-is-getting-kinda-closer'))
        self.assertFalse(
            self.knot.check_key('NOPES-NOPES-NOPES-NOPES-NOPES'))
        self.assertFalse(
            self.knot.check_key('KN00Z-KN1TZ-KN2TZ-KN3TZ-KN4TZ'))
        self.assertFalse(
            self.knot.check_key('P7181-V2516-4380T-4F0BC-J39B0'))

    def test_gen_random_key(self):
        key = self.knot.gen_key()
        self.assertTrue(
            self.knot.check_key(key))


if __name__ == '__main__':
        knotMe = KnotGen()
        key = knotMe.gen_key()
        print "Knot me good with {}".format(key)
