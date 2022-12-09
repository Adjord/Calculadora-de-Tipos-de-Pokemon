"""
Todas as classes e dados (ou a maioria) dos pokemon a serem utilizados pela ‘interface’ devem vir deste arquivo.
Este arquivo deve calcular a efetividade de todos os tipos tanto de defesa quanto de ataque e ter maneiras de enviar
essas informações para a ‘interface’ quando necessário.
"""

import tiposefetividade


class TiposDefesa:
    def __init__(self, nome):
        self.tipo = nome
        self.efetividade = {'planta': 1, 'fogo': 1, 'agua': 1, 'inseto': 1, 'normal': 1, 'venenoso': 1, 'eletrico': 1,
                            'terra': 1, 'lutador': 1, 'psiquico': 1, 'pedra': 1, 'voador': 1, 'fantasma': 1, 'gelo': 1,
                            'dragao': 1, 'metalico': 1, 'sombrio': 1, 'fada': 1}
        # Multiplicador de dano quando o pokemon é atingido por um ataque de cada tipo.

    def muda_efetividade(self, tipagem, nova_efetividade):
        self.efetividade[tipagem] = nova_efetividade

    # muda a efetividade do tipo em relação com outro tipo.

    def retorna_nome(self):
        return self.tipo

    # retorna o nome do tipo sendo analizado.

    def retorna_efetividades(self):
        return self.efetividade

    # retorna o dicionario de efetividades

    def retorna_efetividade_especifica(self, tipo_ef):
        return tipo_ef, self.efetividade[tipo_ef]

    # retorna uma tupla com o nome do tipo sendo analizado e a efetividade dele com relação com o tipo deste objeto

    def imprime_efetividades(self):
        print('As defesas do tipo', self.retorna_nome(), 'são:', self.efetividade)
    # imprime todas as efetividades, usado para debug, não necessário para ‘interface’.


class TiposAtaque(TiposDefesa):
    def imprime_efetividades(self):
        print('Os ataques do tipo', self.retorna_nome(), 'são:', self.efetividade)

    """
    TiposAtaque herda de tipos defesa e tem imprime_efetividades como polimorfismo, as efetividades deste objeto ainda
    tem relação com a defesa porem de forma quase que reversa, por exemplo, se o objeto é o tipo planta e está em
    relação com o tipo agua, o resultado será 2.0 ao invés de 0.5 pois grama é super efetivo contra água.
    """


class Pokemon:
    def __init__(self, tipo1, tipo2=None):
        if tipo2 == 'none':
            tipo2 = None
        self.tipo1_def = todos_os_tipos_defesa[tipo1]
        self.tipo1_atk = todos_os_tipos_ataque[tipo1]
        self.efetividade_ataque_tipo1 = self.tipo1_atk.retorna_efetividades()
        if tipo2 is not None:
            self.tipo2_def = todos_os_tipos_defesa[tipo2]
            self.tipo2_atk = todos_os_tipos_ataque[tipo2]
            self.efetividade_ataque_tipo2 = self.tipo2_atk.retorna_efetividades()
        else:
            self.tipo2_def = None
            self.tipo2_atk = None
        self.efetividade_defesa = self.calcula_efetividade_tipos_defesa()

    """ 
    É desta classe que a interface puxará a maior parte de seus resultados, está responsável por calular a efetividade
    de tipos de um pokemon que tenha um ou dois tipos, incluindo as efetividades de defesa e de ataque.
    pede-se apenas os dois tipos porem 4 objetos são adicionados a partir dessas strings, utilizando os dicionarios
    ja criados pelo programa.
    Os 2 tipos de ataque são objetos TiposAtaque.
    Os dois tipos de defesa são objetos TipoDefesa.
    """

    def calcula_efetividade_tipos_defesa(self):
        if self.tipo2_def is None or self.tipo1_def.retorna_nome() == self.tipo2_def.retorna_nome():
            return self.tipo1_def.retorna_efetividades()
        defesas_tipo_duplo = {}
        for efetividade_tipo_1 in self.tipo1_def.retorna_efetividades():
            for efetividade_tipo_2 in self.tipo2_def.retorna_efetividades():
                if efetividade_tipo_1 == efetividade_tipo_2:
                    defesas_tipo_duplo[efetividade_tipo_1] = (
                            self.tipo1_def.retorna_efetividade_especifica(efetividade_tipo_1)[1] *
                            self.tipo2_def.retorna_efetividade_especifica(efetividade_tipo_1)[1]
                    )
        return defesas_tipo_duplo

    """
    é nesta função onde as defesas do pokemon são calculadas, retorna um dicionario que multiplica a efetividade de 
    defesas dos dois tipos, então um pokemon que é metalico/venenoso teria {Terra: 4.0} pois ambos os seus tipos são
    fracos contra o tipo terra.
    """

    def retorna_efetividades_defesa(self):
        efetividades = {'Resistencias': [], 'Neutros': [], 'Fraquezas': []}
        for i in self.efetividade_defesa:
            if float(self.efetividade_defesa[i]) == 1.0:
                efetividades['Neutros'].append({i: float(self.efetividade_defesa[i])})
            elif self.efetividade_defesa[i] > 1:
                efetividades['Fraquezas'].append({i: float(self.efetividade_defesa[i])})
            else:
                efetividades['Resistencias'].append({i: float(self.efetividade_defesa[i])})
        return efetividades

    """
    retorna as defesas ja calculadas em forma de dicionario de dicionarios, usada pela interface.
    """

    def retorna_stab1(self):
        efetividades = {'Resistentes': [], 'Neutros': [], 'Fracos': []}
        for i in self.efetividade_ataque_tipo1:
            if float(self.efetividade_ataque_tipo1[i]) == 1.0:
                efetividades['Neutros'].append({i: float(self.efetividade_ataque_tipo1[i])})
            elif float(self.efetividade_ataque_tipo1[i]) > 1.0:
                efetividades['Fracos'].append({i: float(self.efetividade_ataque_tipo1[i])})
            else:
                efetividades['Resistentes'].append({i: float(self.efetividade_ataque_tipo1[i])})
        return efetividades

    """
    retorna as efetividades de ataque do tipo 1 ja calculadas em forma de dicionario de dicionarios,
     usada pela interface.
    """

    def retorna_stab2(self):
        if self.tipo2_atk is None or self.tipo1_atk.retorna_nome() == self.tipo2_atk.retorna_nome():
            return None
        efetividades = {'Resistentes': [], 'Neutros': [], 'Fracos': []}
        for i in self.efetividade_ataque_tipo2:
            if float(self.efetividade_ataque_tipo2[i]) == 1.0:
                efetividades['Neutros'].append({i: float(self.efetividade_ataque_tipo2[i])})
            elif float(self.efetividade_ataque_tipo2[i]) > 1.0:
                efetividades['Fracos'].append({i: float(self.efetividade_ataque_tipo2[i])})
            else:
                efetividades['Resistentes'].append({i: float(self.efetividade_ataque_tipo2[i])})
        return efetividades

    """
    retorna as efetividades de ataque do tipo 2 ja calculadas em forma de dicionario de dicionarios,
     usada pela interface.
    """


# ----------------------------------------------------------------------------------------------------------------------
def enche_defesa(lista_tipos_defesa):
    """
    Atualiza o dicionário em TiposDefesa.efetividade, colocando todas as efetividades de defesa encontradas em
    tiposefetividade.py
    """
    for tipo in lista_tipos_defesa:
        for efetividade in tiposefetividade.tipos_defesa:
            if lista_tipos_defesa[tipo].retorna_nome() == efetividade:
                for tipo_ataque in tiposefetividade.tipos_defesa[tipo]:
                    lista_tipos_defesa[tipo].muda_efetividade(tipo_ataque,
                                                              tiposefetividade.tipos_defesa[tipo][tipo_ataque])
    return lista_tipos_defesa


def adiciona_efetividade_ataques(lista_tipos_ataque, lista_tipos_defesa):
    """
    Utiliza das defesas que ja foram adicionadas pela funcao anterior e adiciona as
    efetividades dos ataques de cada tipo.
    """
    for tipo in lista_tipos_defesa:
        for tipo_atk in lista_tipos_defesa[tipo].retorna_efetividades():
            lista_tipos_ataque[tipo_atk].muda_efetividade(
                lista_tipos_defesa[tipo].retorna_nome(),
                lista_tipos_defesa[tipo].retorna_efetividade_especifica(tipo_atk)[1])
    return lista_tipos_ataque


todos_os_tipos_defesa = {tipo1: TiposDefesa(tipo1) for tipo1 in tiposefetividade.tipos}
todos_os_tipos_ataque = {tipo2: TiposAtaque(tipo2) for tipo2 in tiposefetividade.tipos}
"""
geradores que criam os dicionários conforme os tipos em tiposefetividade.py, a chave é uma string com o nome do tipo,
o valor é um objeto TiposDefesa e TiposAtaque respectivamente
"""
todos_os_tipos_defesa = enche_defesa(todos_os_tipos_defesa)
# adiciona as efetividades de defesa de todos os tipos
todos_os_tipos_ataque = adiciona_efetividade_ataques(todos_os_tipos_ataque, todos_os_tipos_defesa)
# usa das efetividades de defesa para adicionar as efetividades de ataque por todos os tipos.
