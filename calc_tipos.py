"""
Todas as classes e dados (ou a maioria) dos pokemon a serem utilizados pela ‘interface’ devem vir deste arquivo.
Este arquivo deve calcular a efetividade de todos os tipos tanto de defesa quanto de ataque e ter maneiras de enviar
essas informações para a ‘interface’ quando requisitado.
"""

import tiposefetividade


class Tipo:
    def __init__(self, nome):
        self.nome = nome
        self.defesa = {typing: 1.0 for typing in tiposefetividade.tipos}
        self.stab = {typing: 1.0 for typing in tiposefetividade.tipos}
        # Multiplicador de cada tipo, começa como 1, que significa efetividade neutra.

    def muda_defesa(self, tipagem, nova_efetividade):
        self.defesa[tipagem] = nova_efetividade

    def muda_ataque(self, tipagem, nova_efetividade):
        self.stab[tipagem] = nova_efetividade

    # muda a efetividade do tipo em relação com outro tipo.

    def retorna_nome(self):
        return self.nome

    # retorna o nome do tipo sendo analizado.

    def retorna_defesas(self):
        return self.defesa

    # retorna o dicionario de efetividade de defesas

    def retorna_defesa_especifica(self, tipo_ef):
        return tipo_ef, self.defesa[tipo_ef]

    # retorna uma tupla com o nome do tipo sendo analizado e a efetividade dele com relação com o tipo deste objeto

    def retorna_stabs(self):
        return self.stab

    # retorna o dicionario de efetividades de ataque


class Pokemon:
    def __init__(self, tipo1, tipo2=None):
        if tipo2 == 'none':
            tipo2 = None
        self.tipo1 = todos_os_tipos[tipo1]
        self.efetividade_ataque_tipo1 = self.tipo1.retorna_stabs()
        if tipo2 is not None:
            self.tipo2 = todos_os_tipos[tipo2]
            self.efetividade_ataque_tipo2 = self.tipo2.retorna_stabs()
        else:
            self.tipo2 = None
        self.efetividade_defesa = self.calcula_efetividade_tipos_defesa()

    """ 
    É desta classe que a interface puxará a maior parte de seus resultados, está responsável por calular a efetividade
    de tipos de um pokemon que tenha um ou dois tipos, incluindo as efetividades de defesa e de ataque.
    pede-se os dois tipos, utilizando os dicionarios ja criados pelo programa.
    """

    def calcula_efetividade_tipos_defesa(self):
        if self.tipo2 is None or self.tipo1.retorna_nome() == self.tipo2.retorna_nome():
            return self.tipo1.retorna_defesas()
        defesas_tipo_duplo = {}
        for efetividade_tipo_1 in self.tipo1.retorna_defesas():
            for efetividade_tipo_2 in self.tipo2.retorna_defesas():
                if efetividade_tipo_1 == efetividade_tipo_2:
                    defesas_tipo_duplo[efetividade_tipo_1] = (
                            self.tipo1.retorna_defesa_especifica(efetividade_tipo_1)[1] *
                            self.tipo2.retorna_defesa_especifica(efetividade_tipo_1)[1]
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
        if self.tipo2 is None or self.tipo1.retorna_nome() == self.tipo2.retorna_nome():
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
def adiciona_efetividades(dict_tipos):
    """
    Atualiza o dicionário de tipos, utilizando as informações em tiposefetividades.py. Adiciona as efetividades de
    defesa e de ataque para todos os tipos.
    """
    for tipo in dict_tipos:
        for efetividade in tiposefetividade.tipos_defesa:
            if dict_tipos[tipo].retorna_nome() == efetividade:
                for tipo_ataque in tiposefetividade.tipos_defesa[tipo]:
                    dict_tipos[tipo].muda_defesa(tipo_ataque,
                                                 tiposefetividade.tipos_defesa[tipo][tipo_ataque])
                    dict_tipos[tipo_ataque].muda_ataque(dict_tipos[tipo].retorna_nome(),
                                                        tiposefetividade.tipos_defesa[tipo][tipo_ataque])
    return dict_tipos


todos_os_tipos = {tipo: Tipo(tipo) for tipo in tiposefetividade.tipos}
"""
gerador que cria o dicionário conforme os tipos em tiposefetividade.py, a chave é uma string com o nome do tipo,
o valor é um objeto Tipos.
"""
todos_os_tipos = adiciona_efetividades(todos_os_tipos)
# adiciona as efetividades de todos os tipos
