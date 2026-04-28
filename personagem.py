from rich import print
from rich.panel import Panel


class personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def mostrar_status(self):
        conteudo = f"[blue]Nome:[/] {self.nome}\n"
        if self.vida >= 1:
            conteudo += f"[green]Vidas:[/] {self.vida}"  
        else:
            conteudo += f"Vidas: :grey_exclamation: derrotado"
        conteudo += f"\n[yellow]Ataque:[/] {self.ataque}"
        print(Panel(conteudo, title="Status atual"))


    def atacar(self, alvo):
        if alvo.vida > 0:
            alvo.receber_dano(self.ataque)
            print(f"{self.nome} atacou {alvo.nome}")
        else: 
            print(f"{alvo.nome} derrotado")
        
    def receber_dano(self, valor):
        self.vida -= valor



mago = personagem("mago", 10, 10)
mago.mostrar_status()
guerreiro = personagem("guerreiro", 20, 5)
guerreiro.mostrar_status()
mago.atacar(guerreiro)
mago.atacar(guerreiro)
mago.atacar(guerreiro)
mago.atacar(guerreiro)
guerreiro.mostrar_status()
