from tqdm import tqdm
import time

def barra_progresso():
    for _ in tqdm(range(100), desc='Saindo do Sistema'):
        time.sleep(0.05)

