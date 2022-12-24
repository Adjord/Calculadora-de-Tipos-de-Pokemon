"""
Pequeno banco de dados para a calculadora de efetividade de tipos de pokemon.
"""
tipos = ['planta', 'fogo', 'agua', 'inseto', 'normal', 'venenoso', 'eletrico', 'terra', 'lutador', 'psiquico', 'pedra',
         'voador', 'fantasma', 'gelo', 'dragao', 'metalico', 'sombrio', 'fada']
# o nome de cada tipo.

tipos_defesa = {
    'planta': {"fogo": 2.0, "agua": 0.5, "planta": 0.5, "gelo": 2.0, "venenoso": 2.0, "terra": 0.5, "voador": 2.0,
               "eletrico": 0.5, "inseto": 2.0},
    'fogo': {"fogo": 0.5, "agua": 2.0, "planta": 0.5, "gelo": 0.5, "terra": 2.0, "inseto": 0.5, "pedra": 2.0,
             "metalico": 0.5,
             "fada": 0.5},
    'agua': {"fogo": 0.5, "agua": 0.5, "eletrico": 2.0, "planta": 2.0, "gelo": 0.5, "metalico": 0.5},
    'inseto': {"fogo": 2.0, "planta": 0.5, "lutador": 0.5, "terra": 0.5, "voador": 2.0, "pedra": 2.0},
    'normal': {"lutador": 2.0, "fantasma": 0.0},
    'venenoso': {"planta": 0.5, "lutador": 0.5, "venenoso": 0.5, "terra": 2.0, "psiquico": 2.0, "fada": 0.5,
                 "inseto": 0.5},
    'eletrico': {"eletrico": 0.5, "terra": 2.0, "voador": 0.5, "metalico": 0.5},
    'terra': {"agua": 2.0, "eletrico": 0.0, "planta": 2.0, "gelo": 2.0, "venenoso": 0.5, "pedra": 0.5},
    'lutador': {"voador": 2.0, "psiquico": 2.0, "inseto": 0.5, "pedra": 0.5, "sombrio": 0.5, "fada": 2.0},
    'psiquico': {"lutador": 0.5, "psiquico": 0.5, "inseto": 2.0, "fantasma": 2.0, "sombrio": 2.0},
    'pedra': {"normal": 0.5, "fogo": 0.5, "agua": 2.0, "planta": 2.0, "lutador": 2.0, "venenoso": 0.5, "terra": 2.0,
              "voador": 0.5, "metalico": 2.0},
    'voador': {"eletrico": 2.0, "planta": 0.5, "gelo": 2.0, "lutador": 0.5, "terra": 0.0, "inseto": 0.5, "pedra": 2.0},
    'fantasma': {"normal": 0.0, "lutador": 0.0, "venenoso": 0.5, "inseto": 0.5, "fantasma": 2.0, "sombrio": 2.0},
    'gelo': {"fogo": 2.0, "gelo": 0.5, "lutador": 2.0, "pedra": 2.0, "metalico": 2.0},
    'dragao': {"fogo": 0.5, "agua": 0.5, "eletrico": 0.5, "planta": 0.5, "gelo": 2.0, "dragao": 2.0, "fada": 2.0},
    'metalico': {"normal": 0.5, "fogo": 2.0, "planta": 0.5, "gelo": 0.5, "lutador": 2.0, "venenoso": 0.0, "terra": 2.0,
                 "voador": 0.5, "psiquico": 0.5, "inseto": 0.5, "pedra": 0.5, "dragao": 0.5, "metalico": 0.5,
                 "fada": 0.5},
    'sombrio': {"lutador": 2.0, "psiquico": 0.0, "inseto": 2.0, "fantasma": 0.5, "sombrio": 0.5, "fada": 2.0},
    'fada': {"lutador": 0.5, "venenoso": 2.0, "inseto": 0.5, "dragao": 0.0, "sombrio": 0.5, "metalico": 2.0}
}

''' efetividade de tipos relacionada a defesa, multiplicador, um ataque nao muito efetivo é mutiplicado por 0.5,
 ou seja, o pokemon que recebe o ataque recebe metade do dano.'''

tipos_cores = {
    'planta': '#4caf50',
    'fogo': '#e86513',
    'agua': '#2196f3',
    'inseto': '#98b82d',
    'normal': '#bfb87f',
    'venenoso': '#ab47bc',
    'eletrico': '#ffcc08',
    'terra': '#e0b352',
    'lutador': '#d32f2f',
    'psiquico': '#ec407a',
    'pedra': '#bda537',
    'voador': '#9d87e0',
    'fantasma': '#7556a5',
    'gelo': '#80deea',
    'dragao': '#673ab7',
    'metalico': '#b4b4cc',
    'sombrio': '#5d4037',
    'fada': '#eb7eb4'
}
# Cores correspondentes a cada tipo. utilizadas na interface grafica.
