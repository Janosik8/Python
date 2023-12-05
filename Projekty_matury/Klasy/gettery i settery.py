class konto_bankowe():
    __stan = 0

    def stan_konta(self):
        return self.__stan

    @property
    def stan_konta(self):
        return 'Stan konta wynosi: ' + str(self.__stan) + ' zł'

    @stan_konta.getter
    def stan_konta(self):
        return 'Tyle masz hajsu: ' + str(self.__stan)

    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan += value



k1 = konto_bankowe()

print(k1.stan_konta)

k1.stan_konta = 50

print(k1.stan_konta)

k1.stan_konta = 150

print(k1.stan_konta)

k1.stan_konta = -200

print(k1.stan_konta)

