import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Let's verify the graph (grafo) and connections loaded in the MundoBD class.
# Simulating a function that will check the graph's state.

from modelo.mundo_bd import MundoBD

# Assuming a sample world name to check
world_name = "Mundo Fantástico"

# Create an instance of MundoBD and load the world
mundo_bd = MundoBD(world_name)
mundo_bd.cargar_mundo()

# Output the graph structure to verify the connections
print("Grafo cargado:", mundo_bd.grafo)
