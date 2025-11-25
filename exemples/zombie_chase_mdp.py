# zombie_chase_mdp.py
from simple_rl.mdp.MDPClass import MDP
from simple_rl.mdp.StateClass import State

import random

class ZombieChaseState(State):
    def __init__(self, player_x, player_y, zombie_x, zombie_y):
        self.data = (player_x, player_y, zombie_x, zombie_y)
        super().__init__(data=self.data)

    @property
    def player(self):
        return self.data[0], self.data[1]

    @property
    def zombie(self):
        return self.data[2], self.data[3]

    def __repr__(self):
        px, py, zx, zy = self.data
        return f"P({px},{py}) Z({zx},{zy})"

class ZombieChaseMDP(MDP):
    def __init__(self, width=5, height=5, goal=(5,5), init_player=(1,1), init_zombie=(3,3),
                 step_cost=-0.01, capture_penalty=-1.0, goal_reward=1.0, gamma=0.99):
        
        actions = ["up", "down", "left", "right", "stay"]
        self.width = width
        self.height = height
        self.goal = goal
        self.init_player = init_player
        self.init_zombie = init_zombie
        self.step_cost = step_cost
        self.capture_penalty = capture_penalty
        self.goal_reward = goal_reward

        # --- CORREÇÃO CRÍTICA AQUI ---
        # Passar as funções requeridas para o construtor do MDP:
        super().__init__(
            actions=actions, 
            transition_func=self._transition_func,  # Chamada do método de transição
            reward_func=self._reward_func,          # Chamada do método de recompensa
            init_state=self.get_init_state(),       # Estado inicial
            gamma=gamma
        )
        # O cur_state é gerenciado internamente pela classe MDP
        
    # --- Métodos de Setup (permanecem os mesmos) ---
    def get_init_state(self):
        px, py = self.init_player
        zx, zy = self.init_zombie
        return ZombieChaseState(px, py, zx, zy)

    def reset(self):
        return self.get_init_state() # Retorna um novo estado inicial


    # --- 1. Função de Transição: Retorna o próximo estado e a recompensa (não altera o estado interno) ---
    # Nota: A IA chamou de 'execute_agent_action', mas o framework espera a função de transição
    def _transition_func(self, state, action):
        px, py = state.player
        zx, zy = state.zombie

        # 1. Atualiza jogador (Lógica de movimento do jogador)
        if action == "up":    py = min(self.height, py + 1)
        if action == "down":  py = max(1, py - 1)
        if action == "left":  px = max(1, px - 1)
        if action == "right": px = min(self.width, px + 1)

        # 2. Movimento do zumbi (Lógica de movimento do Zumbi)
        dx = 1 if px > zx else -1 if px < zx else 0
        dy = 1 if py > zy else -1 if py < zy else 0
        
        # O zumbi move apenas na dimensão com maior diferença absoluta (para um movimento mais "direto")
        # Mas para o exemplo, vamos mover nas duas direções se possível:
        
        # Nota: O movimento do zumbi na resposta da IA estava um pouco simplificado, 
        # mas vamos manter a lógica: ele se move 1 unidade em x e 1 em y na direção do novo px,py
        
        zx_new = max(1, min(self.width, zx + dx))
        zy_new = max(1, min(self.height, zy + dy))

        next_state = ZombieChaseState(px, py, zx_new, zy_new)

        return next_state

    # --- 2. Função de Recompensa: Retorna a recompensa do estado (não altera o estado interno) ---
    def _reward_func(self, state, action, next_state):
        px, py = next_state.player
        zx, zy = next_state.zombie
        
        reward = self.step_cost
        
        # Captura
        if (px, py) == (zx, zy):
            return self.capture_penalty
        
        # Goal
        if (px, py) == self.goal:
            return self.goal_reward
        
        # Passo normal
        return reward
        
    # --- Goal check (usado em planejadores) ---
    def is_goal_state(self, state):
        return state.player == self.goal