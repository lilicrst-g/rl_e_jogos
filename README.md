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

    git clone https://github.com/lilicrst-g/rl_e_jogos.git

Criando um ambiente virtual no diretório do projeto

    python -m venv .venv
    source .venv/bin/activate

Instalando simple_rl e outras bibliotecas necessárias

    pip install simple_rl numpy matplotlib pygame
    pip install -r requeriments.txt

Talvez seja necessário utilizar versões do Python anteriores à 3.8 para garantir o funcionamento completo do SimpleRL. Além disso, alguns ajustes internos na biblioteca podem ser necessários devido a funcionalidades descontinuadas em versões mais recentes. Caso encontre erros dessa natureza, recomenda-se consultar uma ferramenta de IA — não tenha medo de "mexer" nas classes internas do framework quando necessário.

Nos experimentos de Pedra, Papel, Tesoura e Taxi, o código gera automaticamente um arquivo PDF contendo gráficos de recompensa acumulada ao longo dos episódios e instâncias. Para abrir esse arquivo manualmente, acesse o diretório results, depois entre na pasta correspondente ao algoritmo executado e utilize o seguinte comando no terminal:

    xdg-open cumulative_reward.pdf



## Exemplos

### Labirinto com armadilhas

Esse jogo possui visualização gráfica por meio da biblioteca Pygame. Na função _main_, é possível escolher entre diferentes modos (_value, policy, agent, learning_ ou _interactive_), permitindo explorar diversas formas de visualização do comportamento do agente no mapa — desde observar o processo de aprendizado até controlar o agente manualmente usando as teclas de ação.

    # Choose viz type.
    viz = "agent"

<img src="https://github.com/lilicrst-g/rl_e_jogos/blob/main/images/maze_image.png" width="480" align="center">


### Pedra, papel, tesoura

Neste jogo, dois agentes de Aprendizado por Reforço competem entre si ao longo de várias instâncias.
Primeiro, escolha quais dois agentes deseja comparar (entre ql_agent, fixed_agent, rmax_agent e rand_agent) e, em seguida, execute o experimento.

    # Run experiment and make plot.
    play_markov_game([ql_agent, fixed_agent], ...) 


Resultado do QLearning contra o FixedPolicyAgent. Aqui ele escolhe aleatóriamente uma jogada e permanece com ela em todas as instâncias.

<img src="https://github.com/lilicrst-g/rl_e_jogos/blob/main/images/RockPaperScissors_fixed.png" width="480" align="center">

QLearning contra RandomAgent

<img src="https://github.com/lilicrst-g/rl_e_jogos/blob/main/images/RockPaperScissors_rand.png" width="480" align="center">

QLearning contra RMaxAgent

<img src="https://github.com/lilicrst-g/rl_e_jogos/blob/main/images/RockPaperScissors_rMax.png" width="480" align="center">


### Taxi

Este jogo tem duas formas de interação, escolha _True_ para abrir uma visualização gráfica interativa e _False_ para rodar com 3 agentes e comparar os resultados.

    viz = True

1. Visualização interativa: você controla o agente manualmente usando o teclado para guiá-lo pelo ambiente.

<img src="https://github.com/lilicrst-g/rl_e_jogos/blob/main/images/taxi_viz.png" width="480" align="center">

2. Execução automática: os agentes ql_agent, rand_agent e rmax_agent são treinados/executados no ambiente para comparar qual deles obtém o melhor desempenho.

<img src="https://github.com/lilicrst-g/rl_e_jogos/blob/main/images/taxi_agents.png" width="480" align="center">


## Considerações

* O SimpleRL oferece uma boa base para observar o comportamento e o processo de aprendizagem de diferentes agentes de IA em cenários de jogos. Com os ambientes e agentes já incluídos na biblioteca, é possível realizar experimentos interessantes e visualizar diversas dinâmicas de aprendizado. Porém, o framework não é muito flexível para criar ou modificar ambientes — a construção de novos jogos ou mapas exige intervenção direta no código interno, o que pode tornar a experimentação mais limitada ou trabalhosa.
* Todo retorno, seja visual com pygame e gráfico ou pelo terminal, ajuda muito no entendimento de como o algoritmo funciona e na comparação do desempenho dos agentes. Isso é sensacional.
* Em ambientes totalmente observáveis e com dinâmica simples (como Pedra-Papel-Tesoura), agentes baseados em exploração sistemática, como QLearning, tendem a convergir para padrões eficientes, especialmente quando enfrentam adversários determinísticos.
* Em ambientes imprevisíveis (como jogar pedra, papel e tesoura contra um RandomAgent), algoritmos como Q-Learning e R-Max tendem a apresentar desempenho menos consistente, já que não há padrões claros a serem explorados.
* A melhor forma de aprender é realmente colocar a mão na massa — explorar o código, testar hipóteses e não ter medo de modificar o framework quando necessário.
* Um ambiente de jogo, na prática, não difere muito de muitos ambientes do mundo real quando analisamos o desempenho das IAs. Em ambos, treinamos os agentes para maximizar recompensas — seja vencer um jogo, encontrar o melhor percurso, reduzir o tempo gasto ou superar outros agentes. Esses mesmos princípios e métricas podem ser aplicados a diversos cenários reais, onde decisões precisam ser otimizadas continuamente.
* Seria extremamente útil implementar o recurso Easy Reproduction of Results, que recompila e executa um experimento completo a partir de arquivos gerados em execuções anteriores. No entanto, essa funcionalidade ainda não está disponível para os jogos usados neste projeto.


-grupo DataForge