from flask import render_template, redirect, url_for, flash

from app.models import Client, ClientCategory

from .forms import ClientForm

from .utils import save_client, update_clients

from . import crm_bp




@crm_bp.route('/crm')
def crm():
    title =  'CRM'
    prev_url = url_for('public.index')
    return render_template('crm/crm.html',
                           title = title,
                           prev_url = prev_url)


@crm_bp.route('/client/<int:client_id>/get')
def view_client(client_id):
    title = 'Cliente'
    prev_url = url_for('crm.clients_view')
    client = Client.query.get_or_404(client_id)
    return render_template('crm/view_client.html',
                           title = title,
                           client = client,
                           prev_url = prev_url)


@crm_bp.route('/client/view')
def view_clients():
    title = 'Clientes'
    prev_url = url_for('crm.crm')
    clients = Client.query.all()

    return render_template('crm/view_clients.html',
                           title = title,
                           clients = clients,
                           prev_url = prev_url)



@crm_bp.route('/client/add', methods=['GET', 'POST'])
def add_client():
    title = 'Nuevo cliente'
    prev_url = url_for('crm.view_clients')
    form = ClientForm()

    if form.validate_on_submit():

        if save_client(form=form):
            flash('Cliente guardado exitosamente.', 'success')
        else:
            flash('Error al guardar el cliente', 'danger')
        return redirect(url_for('crm.view_clients'))
    
    return render_template('crm/add_client.html',
                           title = title,
                           form = form,
                           prev_url = prev_url)


@crm_bp.route('/client/<int:client_id>/update', methods=['GET', 'POST'])
def update_client(client_id):

    client = Client.query.get_or_404(client_id)
    title = 'Editar cliente'
    prev_url = url_for('crm.view_client', client_id=client_id)
    form = ClientForm(obj=client)

    if form.validate_on_submit():

        if update_clients(form=form, client=client):
            flash('Cliente guardado exitosamente.', 'success')
        else:
            flash('Error al guardar el cliente', 'danger')
        return redirect(url_for('crm.view_clients'))
    
    return render_template('crm/update_client.html',
                           title = title,
                           form = form,
                           prev_url = prev_url)


#**************Ordenes de compra************************

@crm_bp.route('/pruchase_order/view')
def view_purchase_orders():
    title = 'Ordenes de compra'
    purchase_orders = [{'id':1, 'code':'c0005', 'date':'2022-12-11', 'client': 'Nario Salas', 'vendor': 'Juan tock', 'status': 'Completada' },
                       {'id':2, 'code':'c0006', 'date':'2022-12-02', 'client': 'Mario Salas', 'vendor': 'Juan tock', 'status': 'Completada' },
                       {'id':3, 'code':'c0007', 'date':'2022-12-13', 'client': 'Wario Salas', 'vendor': 'Juan tock', 'status': 'Completada' }]
    prev_ref = url_for('crm.crm')

    return render_template('crm/view_purchase_orders.html',
                           title = title,
                           prev_ref = prev_ref,
                           purchase_orders = purchase_orders)