# 🛡️ Projeto de Batalha RPG - Versão LITE

## 📖 Introdução

Esta é a versão **LITE** do jogo original **JogoDoPoder1.0**. Nesta versão, foram removidas as habilidades e trilhas sonoras para focar em seu principal objetivo: **geração de dados estatísticos**.

O jogo simula diversas partidas automáticas, e ao final de cada execução, um relatório detalhado é gerado em formato `.xlsx`. É possível configurar o número de partidas simultâneas alterando a variável `quantidadeDeJogos`, permitindo assim obter uma grande quantidade de dados para análise.

---

## 🔁 Fluxo do Jogo

1. **Entrada na Dungeon**  
   Ao iniciar o jogo, será perguntado se o jogador deseja entrar na dungeon.  
   - Se responder **SIM**, será solicitado um valor de aposta.

2. **Sistema de Aposta & Banca**  
   O jogo possui um sistema de **banca** para controlar ganhos e perdas. As informações mais claras sobre o desempenho financeiro ficam visíveis no relatório gerado após as partidas.

3. **Combate**  
   - O jogador inicia no **nível 1** com um **poder aleatório** entre `1000` e `4000`.
   - Os **monstros** são selecionados aleatoriamente a partir do arquivo:  
     ```
     app/config/gameData.yaml
     ```
   - Cada monstro possui um poder fixo, definido neste arquivo.
   - A vitória em combate é determinada comparando os poderes. O personagem que tiver **mais poder** causará:
     ```
     dano = poder / 30
     ```
   - Caso o jogador sofra dano, será aplicado um **dano refletido** ao monstro:
     ```
     dano_refletido = poder / 40
     ```

---

## 🏆 Como Vencer

- A cada monstro derrotado, o jogador **sobe +1 nível**.
- Ao atingir o **nível 100**, o jogador vence a dungeon.
- Como recompensa, ele recebe o **dobro do valor apostado**.

---

## 💎 Diferenciais do Jogo

O diferencial está no **gerenciamento da banca** e no **comportamento da IA da plataforma** com base nas variáveis abaixo:

- `vantagemMaster`: Quando **ativada (True)** e a banca estiver **abaixo de `valorMinimo`**, o jogo automaticamente **dificulta as batalhas**, escolhendo monstros mais fortes com mais frequência.
- Isso gera uma **tendência de lucro automático para a plataforma**, mantendo um saldo base positivo ao longo do tempo.

---

## 📊 Geração de Relatórios

- Ao final das execuções, é gerado um arquivo `Relatorio.xlsx` no diretório: ```\app\dataRelatorio.xlsx```

## Estrutura de pastas do projeto
```
├── app/                    # Código-fonte principal da aplicação
│   ├── __pycache__/        # Cache de bytecode gerado pelo Python
│   ├── .mypy_cache/        # Cache do mypy para checagem de tipos
│   ├── batalha/            # Lógica relacionada ao sistema de batalha
│   │   ├── __init__.py
│   │   └── batalha.py
│   ├── config/             # Configurações e dados do jogo
│   │   ├── __init__.py
│   │   ├── gameData.yaml           # Dados principais do jogo (configurações)
│   │   ├── gameData-copy.yaml      # Cópia de backup das configurações
│   │   └── settings.py             # Código para lidar com as configurações
│   ├── data/               # Dados adicionais utilizados pela aplicação
│   │   └── Relatorio.xlsx          # Planilha de relatórios
│   ├── functions/          # Pasta para funções utilitárias (Utilizado apenas para sistema de cores)
│   ├── jogador/            # Lógica e estrutura do jogador
│   │   ├── __init__.py
│   │   └── jogador.py
│   ├── monstro/            # Lógica dos monstros
│   │   ├── __init__.py
│   │   └── monstro.py
│   ├── main.py             # Ponto de entrada da aplicação
├── public/                 # Pasta reservada para arquivos públicos (estáticos?)
├── .gitignore              # Arquivos e pastas ignorados pelo Git
├── README.md               # Descrição do projeto (este arquivo)
└── requirements.txt        # Dependências do projeto
```

## Como executar o projeto
1. Clone o repositório com o comando git clone ```https://github.com/KristoferBorges/JogoDoPoder_v1.0.git```;
2. Ative o ambiente virtual ```.venv\Scripts\activate```;
3. Instale as dependências ```pip install -r requirements.txt```
4. Execute o programa ```python app/main.py```;
