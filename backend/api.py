"""Flask API for the world."""

from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.world import World

def create_app(world: World):
    """Create Flask app."""
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/api/world/state', methods=['GET'])
    def get_world_state():
        """Get current world state."""
        return jsonify({
            'step': world.step_count,
            'width': world.width,
            'height': world.height,
            'agents': world.get_agent_states(),
            'statistics': world.get_statistics()
        })
    
    @app.route('/api/world/step', methods=['POST'])
    def world_step():
        """Execute one simulation step."""
        world.step()
        return jsonify({
            'success': True,
            'step': world.step_count,
            'statistics': world.get_statistics()
        })
    
    @app.route('/api/world/stats', methods=['GET'])
    def get_stats():
        """Get world statistics."""
        return jsonify(world.get_statistics())
    
    @app.route('/api/agents/<agent_id>', methods=['GET'])
    def get_agent(agent_id):
        """Get agent information."""
        agent = world.get_agent(agent_id)
        if agent:
            return jsonify(agent.get_state())
        return jsonify({'error': 'Agent not found'}), 404
    
    @app.route('/api/agents', methods=['GET'])
    def get_all_agents():
        """Get all agents."""
        return jsonify(world.get_agent_states())
    
    @app.route('/api/agents/type/<agent_type>', methods=['GET'])
    def get_agents_by_type(agent_type):
        """Get agents by type."""
        agents = [a.get_state() for a in world.agents if a.agent_type == agent_type]
        return jsonify(agents)
    
    @app.route('/health', methods=['GET'])
    def health():
        """Health check."""
        return jsonify({'status': 'ok', 'agents': len(world.agents)})
    
    return app
