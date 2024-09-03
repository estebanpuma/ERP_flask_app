from flask import render_template, redirect, url_for, flash

from app.models import Client, ClientCategory

from .forms import ClientForm

from .utils import save_client, update_clients

from . import crm_bp




@crm_bp.route('/crm')
def crm():
    title =  'CRM'

    return render_template('crm/crm.html',
                           title = title)


@crm_bp.route('/client_view/<int:client_id>')
def client_view(client_id):
    title = 'Cliente'
    client = Client.query.get_or_404(client_id)
    return render_template('crm/client_view.html',
                           title = title,
                           client = client)


@crm_bp.route('/clients_view')
def clients_view():
    title = 'Clientes'
    clients = Client.query.all()

    return render_template('crm/clients_view.html',
                           title = title,
                           clients = clients)



@crm_bp.route('/client/add', methods=['GET', 'POST'])
def add_client():
    title = 'Nuevo cliente'
    form = ClientForm()

    if form.validate_on_submit():

        if save_client(form=form):
            flash('Cliente guardado exitosamente.', 'success')
        else:
            flash('Error al guardar el cliente', 'danger')
        return redirect(url_for('crm.clients_view'))
    
    return render_template('crm/add_client.html',
                           title = title,
                           form = form)


@crm_bp.route('/client/<int:client_id>/update', methods=['GET', 'POST'])
def update_client(client_id):

    client = Client.query.get_or_404(client_id)
    title = 'Editar cliente'
    form = ClientForm(obj=client)

    if form.validate_on_submit():

        if update_clients(form=form, client=client):
            flash("todo bien nano", 'success')
        else:
            flash("no no no otravez sufriendo no", 'danger')
        return redirect(url_for('crm.clients_view'))
    
    return render_template('crm/client_update.html',
                           title = title,
                           form = form)


