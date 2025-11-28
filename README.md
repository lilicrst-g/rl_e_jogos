# Aprendizado por reforço com jogos 
Avaliação da disciplina de Inteligência Artificial II - Aplicação de Reinforce Learning(RL) em jogos e simulações.

Experimento realizado em Python utilizando o framework SimpleRL([repositório no GitHub](https://github.com/david-abel/simple_rl/tree/master)). 

Nesse trabalho rodamos algoritmos de inteligência artificial em 3 jogos:
    
1. Labirinto com armadilhas (maze.py)
2. Pedra, papel, tesoura (RockPaperScissors.py)
3. Taxi (taxi.py)

O objetivo é analisar como os alguns agentes de RL - principalmente o QLearning - se comporta em ambientes de jogos.


## Instalação

Clone do projeto

    git clone https://github.com/AlyssonOliveira/aula_rl.git

Criando um ambiente virtual no diretório do projeto

    python -m venv .venv
    source .venv/bin/activate

Instalando simple_rl e outras bibliotecas necessárias

    pip install simple_rl numpy matplotlib pygame
    pip install -r requeriments.txt

Talvez você precise usar versões abaixo da 3.8 do Python para que tudo funcione corretamente. Além disso alguns ajustes na biblioteca do simple_rl podem ser necessárias por conta de versões descontinuadas de uma coisa ou outra (se ocorrer algum erro dessa naturaza, sugiro que peça ajuda a alguma inteligência artificial e não tenha medo de "mexer" nas classes internas do framework).

O algoritmo do Pedra, papel, tesoura e do Taxi geram um arquivo pdf com gráficos que mostram a recompensa acumulada pelos agentes ao longos dos episódios e das instâncias após a execução. Para abrir esse aquivo manualmente, você vai ao diretório results e em seguida no diretório do algoritmo que foi executado e abre pelo terminal com o seguinte comando:

    xdg-open cumulative_reward.pdf



## Exemplos

### Labirinto com armadilhas

Esse jogo possui visualização gráfica por meio da biblioteca Pygame. Na função _main_, é possível escolher entre diferentes modos (_value, policy, agent, learning_ ou _interactive_), permitindo explorar diversas formas de visualização do comportamento do agente no mapa — desde observar o processo de aprendizado até controlar o agente manualmente usando as teclas de ação.

    # Choose viz type.
    viz = "agent"


<img src="https://github.com/lilicrst-g/rl_e_jogos/images.maze_image.png" width="480" align="center">


### Pedra, papel, tesoura

Neste jogo, dois agentes de Aprendizado por Reforço competem entre si ao longo de várias instâncias.
Primeiro, escolha quais dois agentes deseja comparar (entre ql_agent, fixed_agent, rmax_agent e rand_agent) e, em seguida, execute o experimento.

    # Run experiment and make plot.
    play_markov_game([ql_agent, fixed_agent], ...) 


Resultado do QLearning contra o FixedPolicyAgent. Aqui ele escolhe aleatóriamente uma jogada e permanece com ela em todas as instâncias.

<img src="https://github.com/lilicrst-g/rl_e_jogos/images.RockPaperScissors_fixed.png" width="480" align="center">

QLearning contra RandomAgent

<img src="https://github.com/lilicrst-g/rl_e_jogos/images.RockPaperScissors_rand.png" width="480" align="center">

QLearning contra RMaxAgent

<img src="https://github.com/lilicrst-g/rl_e_jogos/images.RockPaperScissors_rMax.png" width="480" align="center">


### Taxi

Este jogo tem duas formas de interação, escolha _True_ para abrir uma visualização gráfica interativa e _False_ para rodar com 3 agentes e comparar os resultados.

    viz = True

1. Visualização interativa: você controla o agente manualmente usando o teclado para guiá-lo pelo ambiente.

<img src="https://github.com/lilicrst-g/rl_e_jogos/images.taxi_viz.png" width="480" align="center">

2. Execução automática: os agentes ql_agent, rand_agent e rmax_agent são treinados/executados no ambiente para comparar qual deles obtém o melhor desempenho.

<img src="https://github.com/lilicrst-g/rl_e_jogos/images.taxi_agents.png" width="480" align="center">


## Considerações

* Em ambientes totalmente observáveis e com dinâmica simples (como Pedra-Papel-Tesoura), agentes baseados em exploração sistemática, como QLearning, tendem a convergir para padrões eficientes, especialmente quando enfrentam adversários determinísticos.
* Limitações do framework SimpleRL - algumas partes da biblioteca utilizam estruturas antigas e exigiram ajustes devido à compatibilidade com versões recentes do Python.

-grupo DataForge