"""World simulation engine."""

import yaml
import random
import numpy as np
from typing import Dict, List
from backend.agents import WorkerAgent, TraderAgent, ExplorerAgent, LearnerAgent, BaseAgent

class World:
    """Main world simulation class."""
    
    def __init__(self, config_path: str = None):
        # Load config
        if config_path:
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            # Default config
            self.config = self._default_config()
        
        # World dimensions
        self.width = self.config['world']['width']
        self.height = self.config['world']['height']
        self.time_scale = self.config['world']['time_scale']
        
        # State
        self.step_count = 0
        self.agents: List[BaseAgent] = []
        self.history = []
        
        # Initialize agents
        self._initialize_agents()
    
    def _default_config(self) -> Dict:
        """Get default configuration."""
        return {
            'world': {'width': 100, 'height': 100, 'time_scale': 1.0},
            'agents': {
                'total_count': 50,
                'types': {
                    'worker': {'count': 20},
                    'trader': {'count': 10},
                    'explorer': {'count': 10},
                    'learner': {'count': 10}
                }
            }
        }
    
    def _initialize_agents(self):
        """Initialize all agents in the world."""
        agent_config = self.config['agents']['types']
        
        # Create workers
        for _ in range(agent_config.get('worker', {}).get('count', 20)):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            self.agents.append(WorkerAgent(self, x, y))
        
        # Create traders
        for _ in range(agent_config.get('trader', {}).get('count', 10)):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            self.agents.append(TraderAgent(self, x, y))
        
        # Create explorers
        for _ in range(agent_config.get('explorer', {}).get('count', 10)):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            self.agents.append(ExplorerAgent(self, x, y))
        
        # Create learners
        for _ in range(agent_config.get('learner', {}).get('count', 10)):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            self.agents.append(LearnerAgent(self, x, y))
    
    def step(self):
        """Execute one world step."""
        self.step_count += 1
        
        # Update all agents
        for agent in self.agents[:]:
            if agent.state != "dead":
                agent.step()
            else:
                self.agents.remove(agent)
        
        # Spawn new agents if population is low
        if len(self.agents) < self.config['agents']['total_count'] * 0.5:
            self._spawn_agent()
        
        # Record statistics
        if self.step_count % 10 == 0:
            self.history.append(self.get_statistics())
    
    def _spawn_agent(self):
        """Spawn a new random agent."""
        agent_types = [WorkerAgent, TraderAgent, ExplorerAgent, LearnerAgent]
        agent_type = random.choice(agent_types)
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        self.agents.append(agent_type(self, x, y))
    
    def get_statistics(self) -> Dict:
        """Get world statistics."""
        if not self.agents:
            return {}
        
        energies = [a.energy for a in self.agents]
        happiness = [a.happiness for a in self.agents]
        
        agent_types = {}
        for agent in self.agents:
            agent_types[agent.agent_type] = agent_types.get(agent.agent_type, 0) + 1
        
        return {
            'step': self.step_count,
            'total_agents': len(self.agents),
            'agent_types': agent_types,
            'avg_energy': np.mean(energies),
            'avg_happiness': np.mean(happiness),
            'energy_std': np.std(energies),
            'happiness_std': np.std(happiness)
        }
    
    def get_agent_states(self) -> List[Dict]:
        """Get states of all agents."""
        return [agent.get_state() for agent in self.agents]
    
    def get_agent(self, agent_id: str) -> BaseAgent:
        """Get agent by ID."""
        for agent in self.agents:
            if agent.id == agent_id:
                return agent
        return None
