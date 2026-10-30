# ==============================================================================
# Script auxiliar para teste automatizado com 50 entrevistados
# ==============================================================================
import random
import subprocess
import sys
import os

nomes = [
    'Ana Silva', 'Bruno Souza', 'Carlos Santos', 'Daniela Oliveira', 'Eduardo Pereira',
    'Fernanda Lima', 'Gabriel Costa', 'Helena Rodrigues', 'Igor Almeida', 'Juliana Barbosa',
    'Lucas Ribeiro', 'Mariana Carvalho', 'Nicolas Gomes', 'Olivia Martins', 'Paulo Araujo',
    'Rafaela Melo', 'Samuel Castro', 'Tatiana Cardoso', 'Vinicius Rocha', 'Yasmin Dias',
    'Andre Moreira', 'Beatriz Cunha', 'Caio Correia', 'Debora Teixeira', 'Emerson Barros',
    'Fabiana Cavalcanti', 'Gustavo Monteiro', 'Isabela Pires', 'Joao Vitor Mendes', 'Larissa Freitas',
    'Matheus Ramos', 'Natalia Duarte', 'Otavio Farias', 'Patricia Viana', 'Renan Guimaraes',
    'Sabrina Peixoto', 'Thiago Nogueira', 'Vanessa Borges', 'Willian Antunes', 'Alice Campos',
    'Bernardo Teles', 'Camila Neves', 'Diego Maciel', 'Evelyn Prado', 'Felipe Bezerra',
    'Gabriela Morais', 'Henrique Siqueira', 'Ingrid Paiva', 'Leonardo Moura', 'Manuela Franco'
]

random.seed(42)

entradas = []
for nome in nomes:
    idade = random.randint(18, 65)
    # Distribuição com pesos: 1 (Excelente), 2 (Bom), 3 (Ruim)
    opiniao = random.choices(['1', '2', '3'], weights=[0.45, 0.35, 0.20])[0]
    entradas.append(f'{nome}\n{idade}\n{opiniao}\n')

input_data = ''.join(entradas)

script_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(script_dir, 'pesquisa.py')

env = os.environ.copy()
env['PYTHONIOENCODING'] = 'utf-8'

print("Executando pesquisa.py com 50 entrevistados...\n")
proc = subprocess.run(
    [sys.executable, script_path],
    input=input_data,
    text=True,
    capture_output=True,
    encoding='utf-8',
    env=env
)

print(proc.stdout)

