from flask import Flask
from src.main.routes.calculators import calc_route_bp

# Cria uma instância do Flask chamada app que recebe o nome do módulo atual (__name__) como argumento para que o Flask saiba onde procurar os arquivos estáticos, templates, etc.
app = Flask(__name__)

app.register_blueprint(calc_route_bp, url_prefix='/calculators')
