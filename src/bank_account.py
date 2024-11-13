class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance= balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')
    
    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(f"{message}\n")
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('El monto ingresado no puede ser menor a 0')
        self.balance += amount
        self._log_transaction(f'Se deposito {amount}, el nuevo balance es {self.balance}')
        return self.getBalance()

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('El monto a retirar supera el limite')
        self.balance -= amount
        self._log_transaction(f'Se retiro {amount}, el nuevo balance es {self.balance}')
        return self.getBalance()

    def getBalance(self):
        self._log_transaction(f'El balance es {self.balance}')
        return self.balance