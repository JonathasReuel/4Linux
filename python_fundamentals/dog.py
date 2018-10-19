class Dog():
    '''
    Classe para criar um Dog...
    '''
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5

    def latir(self):
        '''Metodo para o dog latir'''
        print('{} Latindo....'.format(self.nome))

    def andar(self):
        self.energia -= 1

    def dormir(self):
        self.energia = 5

    def __str__(self):
        return 'Nome: {} Raca: {} Idade: {}'.format(self.nome,self.raca,self.idade)