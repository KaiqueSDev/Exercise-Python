from flask import Flask, render_template, request, redirect, url_for

from database import (
    criar_tabela,
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa,
    editar_tarefa,
    buscar_tarefa
)

app = Flask(__name__)

criar_tabela()


@app.route('/app', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tarefa = str(request.form['tarefa'])
        adicionar_tarefa(tarefa)

    tarefas = listar_tarefas()

    return render_template('index.html', tarefas=tarefas)


@app.route('/concluir/<int:id>')
def concluir(id: int):
    concluir_tarefa(id)

    return redirect(url_for('index'))


@app.route('/excluir/<int:id>')
def excluir(id: int):
    excluir_tarefa(id)

    return redirect(url_for('index'))


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id: int):
    tarefa = buscar_tarefa(id)

    if request.method == 'POST':
        novo_titulo = request.form['tarefa']

        editar_tarefa(id, novo_titulo)

        return redirect(url_for('index'))

    return render_template(
        'editar.html',
        tarefa=tarefa
    )


if __name__ == '__main__':
    app.run(debug=True)