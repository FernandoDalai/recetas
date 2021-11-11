from flask import render_template, request, redirect

from models import *
from utils import debug

recetas = []  # 0
receta1 = Receta(
    id=0,
    nombre='Tacos',
    dificultad='Difícil',
    tiempo='2hr',
    descripcion='Descripción del artículo',
    costo=400,
    calificacion=5,
)
# 1
receta2 = Receta(
    id=1,
    nombre='Pasta',
    dificultad='Normal',
    tiempo='25min',
    descripcion='Descripción del artículo',
    costo=100,
    calificacion=2,
)
recetas.append(receta1)
recetas.append(receta2)


# 2


def index():
    return render_template('index.html', recetas=recetas)


def ver_receta(id):
    # TODO: Validar id
    id = min([len(recetas) - 1, int(id)])
    return render_template('big_card.html', receta=recetas[id])


def crear_receta():
    if request.method == 'GET':
        return render_template('crear_receta.html')

    data = request.form
    # try:
    #     debug(data, dict(data))
    # except:
    #     debug(data, data.__dict__)
    #

    receta_aux = Receta(
        id=len(recetas),
        nombre=data['titulo'],
        dificultad=data['dificultad'],
        tiempo=data['tiempo'],
        descripcion='Lorem ipsum dolor amet',
        costo=data['costo'],
        calificacion=3,
    )
    recetas.append(receta_aux)
    # TODO: Añadir pasos
    # TODO: Añadir ingredientes
    return redirect(f'/ver_receta/{receta_aux.id}')
