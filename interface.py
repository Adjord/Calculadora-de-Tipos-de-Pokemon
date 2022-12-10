"""
A ‘interface’ grafica deve ser construida neste arquivo, utilizando da biblioteca tkinter, o trabalho deste é trazer
para o usuário uma ‘interface’ limpa e com todas as informações calculadas usando os outros arquivos, agregando-as em
um só lugar.
"""

import calc_tipos as calc
import tiposefetividade as types
import tkinter as tk
import datetime


def faz_frames_tipos(list_tipos):
    # Função simples que transforma uma lista de efetividades em uma lista com o nome, a efetividade e a cor do tipo,
    # respeitando os parametros de tiposefetividade.py
    cores = types.tipos_cores
    new_types = []
    for dicionario in list_tipos:
        for i in dicionario:
            new_types.append((i, dicionario[i], cores[i]))
    return new_types


def tipo_frames(tipo_efet_frame, lista_efets):
    """Esta é a função que dá cor aos tipos, recebe-se o frame onde os tipos serão colocados e a lista de efetividades
    do tipo, esta lista é transformada pela função anterior e frames são criados para serem adicionados ao frame que
    já se foi passado, cada tipo são 3 frames: 1 que segura os frame com o nome e cor e outro que segura a
    efetividade"""
    count_row = 1
    count_column = 0
    for tipo_tupla in faz_frames_tipos(lista_efets):
        outer_frame = tk.Frame(tipo_efet_frame, highlightbackground=tipo_tupla[2], highlightthickness=1)
        outer_frame.columnconfigure(0, weight=2)
        outer_frame.grid(padx=1.5, pady=1.2, row=count_row, column=count_column, sticky='news')
        if count_column == 2:
            count_column = -1
            count_row += 1
        count_column += 1
        nome_tipo_frame = tk.Frame(outer_frame, bg=tipo_tupla[2])
        nome_tipo_frame.grid(column=0, row=0, sticky='ew')
        tk.Label(nome_tipo_frame, text=(tipo_tupla[0]).upper(), fg='white', bg=tipo_tupla[2]).grid(row=0, column=0)
        efetividade_tipo_frame = tk.Frame(outer_frame, bg='White')
        efetividade_tipo_frame.grid(row=0, column=1)
        tk.Label(efetividade_tipo_frame, text=tipo_tupla[1], bg='white').grid(row=0, column=0)


def botao_explica():
    # Mostra uma tela nova com as explicações sobre tipos quando o botao correspondente é pressionado.
    janela2 = tk.Toplevel(claclu, bg=frame_color)
    janela2.title('Explicação sobre tipos')
    janela2.geometry('600x600')
    tk.Label(janela2, text='Explicação dos tipos', bg=frame_color,
             fg='white', font=('Arial', 30)).grid(row=0, column=1, sticky='news')
    tk.Label(janela2, text='"Cada Pokémon pode pertencer a até dois tipos, sendo o primeiro deles o primário e o outro,'
                           ' o secundário. Charizard, por exemplo, é Fogo/Voador, enquanto que Pikachu é apenas '
                           'Elétrico (é um Pokémon Elétrico puro). Por outro lado, cada movimento tem só um tipo.'
                           ' Um Pokémon pode ter até quatro movimentos, mas elas não precisam ser do mesmo tipo que a '
                           'criatura. Exemplificando: Pikachu, mesmo sendo somente Elétrico, pode aprender Cauda de '
                           'Ferro, movimento do tipo Metálico. Contudo, quando o tipo da técnica e o do Pokémon que a '
                           'aprendeu coincidem, o poder da técnica aumenta em 50% (isso é chamado de STAB, Same Type '
                           'Attack Bonus = Bônus do Ataque de Mesmo Tipo)."',
             bg=frame_color, fg='white', font=('Arial', 17), wraplength=580).grid(row=1, column=1, sticky='news')
    tk.Label(janela2, text='Trecho retirado de https://pokemon.fandom.com/pt-br/wiki/Tipo#Tipos', bg=frame_color,
             fg='white', font=('Arial', 9)).grid(row=2, column=1, sticky='news')
    tk.Label(janela2, text='A calculadora mostra o multiplicador do dano base do ataque, por exemplo, se um pokemon do '
                           'tipo planta é atingido por um pokemon do tipo agua, o multiplicador é 0.5, ou seja, o pokem'
                           'on leva metade do dano', bg=frame_color, fg='white',
             font=('Arial', 17), wraplength=580).grid(row=3, column=1, sticky='news', pady=5)
    tk.Label(janela2, text='Basta escolher um ou dois tipos nos menus Tipo1 e Tipo2.', bg=frame_color, fg='white',
             font=('Arial', 15), wraplength=580).grid(row=4, column=1, sticky='news', pady=5)


def limpa_gui():
    # Função mecessária para limpar a seleção anterior de tipos.
    # Remove os widgets subordinados que não serão mais utilizados.
    if len(tipos_frame.winfo_children()) >= 2:
        count = 0
        for widgets in tipos_frame.winfo_children():
            if count > 0:
                widgets.destroy()
            count += 1


def envia_tipos():
    """Função que garante que mostra_efetividades recebe os nomes corretos dos tipos, a gui foi limpa e a mensagem a ser
    mostrada é correta, além de pedir pelo menos um tipo válido quando este não é providenciado pelo usuário.
    Chamada quando não é a primeira vez que o usuário usa o programa (o arquivo existe e os tipos foram guardados)
    e quando o botão enviar é pressionado."""
    limpa_gui()
    if msg_boas_vindas is not None:
        boas_vindas_txt.set(msg_boas_vindas[0])
        boas_vindas_subtxt.set(msg_boas_vindas[1])
    else:
        boas_vindas_txt.set('Bem vindo!')
        boas_vindas_subtxt.set('')
    type1 = tipo1.get()
    type2 = tipo2.get()
    if type1 == 'Nenhum Tipo' or type1 == 'Tipo 1':
        type1 = None
    if type2 == 'Nenhum Tipo' or type2 == 'Tipo 2':
        type2 = None
    if type1 is None and type2 is not None:
        type1 = type2
        type2 = None
    elif type1 is None and type2 is None:
        boas_vindas_txt.set('Voce precisa escolher pelo menos um tipo valido.')
        return None
    mostra_efetividades(type1, type2)
    return None


def mostra_efetividades(type1, type2=None):
    """
    Utiliza o tipo passado(s) pelo usuário e os transforma em um objeto Pokemon, todos os calculos são feitos em
    calc_tipos.py e esta função cuida de como mostrá-los ao usuário
    """
    pokemon = calc.Pokemon(str(type1).lower(), str(type2).lower())
    efetividades_defesa = pokemon.retorna_efetividades_defesa()
    efetividades_stab1 = pokemon.retorna_stab1()
    efetividades_stab2 = pokemon.retorna_stab2()
    defesas_frame = tk.Frame(tipos_frame, width=650, bg=frame_color, highlightcolor='#515151', highlightthickness=1)
    defesas_frame.rowconfigure(0, weight=1)
    defesas_frame.rowconfigure(1, weight=1)
    defesas_frame.rowconfigure(2, weight=1)
    defesas_frame.columnconfigure(0, weight=2)
    defesas_frame.columnconfigure(1, weight=2)
    defesas_frame.columnconfigure(2, weight=2)
    defesas_frame.grid(row=1, sticky='news', pady=2)
    tk.Label(defesas_frame, text='Este pokemon é:', bg=frame_color, fg='white').grid(row=0, column=1)
    tk.Label(defesas_frame, text='FRACO contra:', bg=frame_color, fg='white').grid(row=1, column=0)
    tk.Label(defesas_frame, text='RESISTENTE contra:', bg=frame_color, fg='white').grid(row=1, column=1)
    tk.Label(defesas_frame, text='Dano NEUTRO de:', bg=frame_color, fg='white').grid(row=1, column=2)
    """
    Existem dois ou três frames na vertical defesas_frame é o primeiro, todos eles são divididos em 3, para as 
    super efetividades, não super efetividades e neutralidade dos tipos, as outras são stab1_frame e, quando dois tipos
    estão presentes, stab2_frame.
    Todas as informações sobre os tipos vem dos outros arquivos.
    """

    super_defesas_frame = tk.Frame(defesas_frame, width=200, padx=3.5, bg=frame_color)
    super_defesas_frame.grid(row=2, column=0)
    tipo_frames(super_defesas_frame, efetividades_defesa['Fraquezas'])

    resist_defesas_frame = tk.Frame(defesas_frame, width=200, bg=frame_color)
    resist_defesas_frame.grid(row=2, column=1, padx=3.5)
    tipo_frames(resist_defesas_frame, efetividades_defesa['Resistencias'])

    normal_defesas_frame = tk.Frame(defesas_frame, width=200, padx=3.5, bg=frame_color)
    normal_defesas_frame.grid(row=2, column=2)
    tipo_frames(normal_defesas_frame, efetividades_defesa['Neutros'])

    stabs_tipo1_frame = tk.Frame(tipos_frame, width=650, bg=frame_color, highlightthickness=1)
    stabs_tipo1_frame.rowconfigure(0, weight=1)
    stabs_tipo1_frame.rowconfigure(1, weight=1)
    stabs_tipo1_frame.rowconfigure(2, weight=1)
    stabs_tipo1_frame.columnconfigure(0, weight=2)
    stabs_tipo1_frame.columnconfigure(1, weight=2)
    stabs_tipo1_frame.columnconfigure(2, weight=2)
    stabs_tipo1_frame.grid(row=2, column=0, sticky='news', pady=2)
    tk.Label(stabs_tipo1_frame, text=f'Os ataques do tipo {type1} são:',
             bg=frame_color, fg='white').grid(column=1, row=0, pady=1)
    tk.Label(stabs_tipo1_frame, text='SUPER EFETIVOS contra:', bg=frame_color, fg='white').grid(column=0, row=1)
    tk.Label(stabs_tipo1_frame, text='FRACOS CONTRA:', bg=frame_color, fg='white').grid(column=1, row=1)
    tk.Label(stabs_tipo1_frame, text='NEUTROS CONTRA:', bg=frame_color, fg='white').grid(column=2, row=1)

    super_stab1_frame = tk.Frame(stabs_tipo1_frame, width=200, padx=3.5, bg=frame_color)
    super_stab1_frame.grid(column=0, row=2)
    tipo_frames(super_stab1_frame, efetividades_stab1['Fracos'])

    fraquezas_stab1_frame = tk.Frame(stabs_tipo1_frame, width=200, padx=3.5, bg=frame_color)
    fraquezas_stab1_frame.grid(column=1, row=2)
    tipo_frames(fraquezas_stab1_frame, efetividades_stab1['Resistentes'])

    neutro_stab1_frame = tk.Frame(stabs_tipo1_frame, width=200, padx=3.5, bg=frame_color)
    neutro_stab1_frame.grid(column=2, row=2)
    tipo_frames(neutro_stab1_frame, efetividades_stab1['Neutros'])

    if str(type1) != str(type2) and type2 is not None:
        """
        os stabs para o tipo 2 só aparecem se e somente se dois tipos diferentes e válidos foram selecionados,
        normal/nenhum, planta/planta e nenhum/fogo, por exemplo, mostram apenas stab1, enquanto lutador/inseto mostraria
        ambos stab1 e stab2
        """
        stabs_tipo2_frame = tk.Frame(tipos_frame, width=650, bg=frame_color, highlightthickness=1)
        stabs_tipo2_frame.rowconfigure(0, weight=1)
        stabs_tipo2_frame.rowconfigure(1, weight=1)
        stabs_tipo2_frame.rowconfigure(2, weight=1)
        stabs_tipo2_frame.columnconfigure(0, weight=2)
        stabs_tipo2_frame.columnconfigure(1, weight=2)
        stabs_tipo2_frame.columnconfigure(2, weight=2)
        stabs_tipo2_frame.grid(row=3, column=0, sticky='news', pady=2)
        tk.Label(stabs_tipo2_frame, text=f'Os ataques do tipo {type2} são:', bg=frame_color, fg='white').grid(
            column=1, row=0, pady=1)
        tk.Label(stabs_tipo2_frame, text='SUPER EFETIVOS contra:', bg=frame_color, fg='white').grid(column=0, row=1)
        tk.Label(stabs_tipo2_frame, text='FRACOS CONTRA:', bg=frame_color, fg='white').grid(column=1, row=1)
        tk.Label(stabs_tipo2_frame, text='NEUTROS CONTRA:', bg=frame_color, fg='white').grid(column=2, row=1)

        super_stab2_frame = tk.Frame(stabs_tipo2_frame, width=200, padx=3.5, bg=frame_color)
        super_stab2_frame.grid(column=0, row=2)
        tipo_frames(super_stab2_frame, efetividades_stab2['Fracos'])

        fraquezas_stab2_frame = tk.Frame(stabs_tipo2_frame, width=200, padx=3.5, bg=frame_color)
        fraquezas_stab2_frame.grid(column=1, row=2)
        tipo_frames(fraquezas_stab2_frame, efetividades_stab2['Resistentes'])

        neutro_stab2_frame = tk.Frame(stabs_tipo2_frame, width=200, padx=3.5, bg=frame_color)
        neutro_stab2_frame.grid(column=2, row=2)
        tipo_frames(neutro_stab2_frame, efetividades_stab2['Neutros'])


def manipula_arquivo(state_bool):
    """
    Função encarregada da manipulação do arquivo, quando o programa é iniciado checa se o arquivo existe, se não,
    assume-se ser a primeira vez que o usuário utiliza-se da aplicação, quando o programa é fechado, o arquivo
    anterior é substituído por um novo.
    """
    if state_bool:
        try:
            with open('ultima_sessao.txt', mode='r') as arquivo:
                linhas = arquivo.read().splitlines()
                arquivo.close()
                del arquivo
                return linhas if len(linhas) == 7 else None
        except IOError:
            return None
    else:
        with open('ultima_sessao.txt', mode='w') as arquivo:
            data = datetime.datetime.now()
            temptuple = (data.month, data.year, data.hour, data.minute)
            arquivo.write(str(data.day))
            for tempo in temptuple:
                arquivo.write(f'\n{str(tempo)}')
            arquivo.write(f'\n{str(tipo1.get())}')
            arquivo.write(f'\n{str(tipo2.get())}')
            arquivo.close()
            return None


def mensagem_boas_vindas(lista_ult):
    """
    Muda a mensagem de Boas-vindas conforme o arquivo, se este não existir é recomendado que o usuário clique
    no botão de ajuda. Quando o arquivo existe, checa-se se a hora e minuto armazenados tem dois digitos e então
    atualiza o valor do texto para mostrá-los
    """
    if lista_ult is None:
        boas_vindas_subtxt.set('Esta parece ser sua primeira vez aqui, clique no botao ao lado para saber mais!')
        return None
    if len(lista_ult[3]) <= 1:
        lista_ult[3] = '0' + lista_ult[3]
    if len(lista_ult[4]) <= 1:
        lista_ult[4] = '0' + lista_ult[4]
    boas_txt = 'Bem vindo de volta!'
    boas_subtxt = f'ultimo login em {lista_ult[0]}/{lista_ult[1]}/{lista_ult[2]} às {lista_ult[3]}:{lista_ult[4]}'
    boas_vindas_txt.set(boas_txt)
    boas_vindas_subtxt.set(boas_subtxt)
    tipo1.set(lista_ult[5])
    tipo2.set(lista_ult[6])
    return boas_txt, boas_subtxt


frame_color = '#414141'

root = tk.Tk()
root.title('Calculadora de efetividade de tipos de pokemon.')
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
root.geometry('950x670')
root.configure(bg=frame_color)
root.resizable(False, False)

claclu = tk.Frame(root)
claclu.pack()
claclu.configure(bg=frame_color)
# Mesmo root sendo a base de toda a ‘interface’, claclu é sua única subordinada direta, todos os widgets estão em claclu
# e seus filhos.

boas_vindas_frame = tk.Frame(claclu)
boas_vindas_frame.columnconfigure(0, weight=1)
boas_vindas_frame.columnconfigure(1, weight=1)
boas_vindas_frame.configure(bg=frame_color)
boas_vindas_frame.pack(pady=3)

boas_vindas_txt = tk.StringVar(boas_vindas_frame, 'Bem vindo!')
boas_vindas_subtxt = tk.StringVar(boas_vindas_frame)

tk.Label(boas_vindas_frame, textvariable=boas_vindas_txt, font=('Arial', 20), bg=frame_color,
         fg='white').grid(column=0, row=0, padx=15, pady=2)
tk.Label(boas_vindas_frame, textvariable=boas_vindas_subtxt, font=('Arial', 15), bg=frame_color, fg='white').grid(
    column=0, row=1)

tk.Button(boas_vindas_frame, text='?', font=('Arial', 20), bg='#5b5b5b', fg='white',
          command=botao_explica).grid(row=0, column=1, padx=3)

"""
O painel de boas vindas é inicializado e 2 labels e um botão são adicionados, os labels são texto e subtexto e serão
atualizados pelas funções, o botão mostra ajuda e explicação.
"""

tipos_frame = tk.Frame(claclu)
tipos_frame.rowconfigure(0, weight=1)
tipos_frame.rowconfigure(1, weight=1)
tipos_frame.rowconfigure(2, weight=1)
tipos_frame.rowconfigure(3, weight=1)
tipos_frame.configure(bg='#414141')
tipos_frame.pack(pady=3)
# Tipos frames é onde 99% da informação é mostrada, será dividida em 4 partes:
"""
1 - onde o usuario escolhe e envia os tipos a serem analizados
2 - as defesas do tipo analizado(s)
3 - as efetividades de ataque do primeiro tipo
4 - as efetividades de ataque do segundo tipo, se este foi enviado.
"""


escolha_tipo_frame = tk.Frame(tipos_frame)
escolha_tipo_frame.columnconfigure(0, weight=1)
escolha_tipo_frame.columnconfigure(1, weight=1)
escolha_tipo_frame.configure(bg='#414141')
escolha_tipo_frame.grid(row=0, column=0, pady=3)

tipo1 = tk.StringVar(escolha_tipo_frame, 'Tipo 1')
tipo2 = tk.StringVar(escolha_tipo_frame, 'Tipo 2')
opcoes_tipos = [tipo.capitalize() for tipo in types.tipos]
opcoes_tipos.insert(0, 'Nenhum Tipo')

escolhe_tipo1_optmenu = tk.OptionMenu(escolha_tipo_frame, tipo1, *opcoes_tipos)
escolhe_tipo1_optmenu.configure(bg='#5b5b5b', fg='white')
escolhe_tipo1_optmenu['menu'].config(bg='light blue')
escolhe_tipo1_optmenu.grid(column=0, row=0, padx=5)

escolhe_tipo2_optmenu = tk.OptionMenu(escolha_tipo_frame, tipo2, *opcoes_tipos)
escolhe_tipo2_optmenu.configure(bg='#5b5b5b', fg='white')
escolhe_tipo2_optmenu['menu'].config(bg='light blue')
escolhe_tipo2_optmenu.grid(column=1, row=0, padx=5)
tk.Button(escolha_tipo_frame, text='Enviar', command=envia_tipos,
          bg='#5b5b5b', fg='white').grid(row=1, column=0, pady=5, columnspan=2)

"""
Onde os dois menus de tipos são criados, todos os 18 tipos aparecem aqui e uma opção extra para quando não se deseja 
tipo nenhum, o botão de enviar também é criado aqui.
"""

ultima_sessao = manipula_arquivo(True)
msg_boas_vindas = mensagem_boas_vindas(ultima_sessao)
if msg_boas_vindas is not None:
    envia_tipos()
root.mainloop()
manipula_arquivo(False)

"""
checa-se o arquivo e inicia-se o loop infinito da interface.
"""
