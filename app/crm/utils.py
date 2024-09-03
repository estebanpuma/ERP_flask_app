from flask import flash

from app.models import Client


def save_client(form):
    # Determinar el tipo de cliente
    client_type = form.client_type.data

    # Crear instancia del cliente
    client = Client(
        client_type=client_type,
        ruc_or_ci=form.ruc_or_ci.data,
        name=form.name.data,
        address=form.address.data,
        phone=form.phone.data,
        email=form.email.data,
        client_category_id=form.category.data if form.category.data else None
    )
    
        # Guardar el cliente en la base de datos
    success, error = client.save()
    if success:
        return True
    else:
        flash(f'Error al guardar: {error}', 'danger')
        return False


def update_clients(form, client):


    
    client.client_type=form.client_type.data
    client.ruc_or_ci=form.ruc_or_ci.data
    client.name=form.name.data
    client.address=form.address.data
    client.phone=form.phone.data
    client.email=form.email.data
    client.client_category_id=form.category.data if form.category.data else None
    

    try:
        # Guardar el cliente en la base de datos
        client.save()
        flash('Cliente guardado exitosamente.', 'success')
        return True
    except Exception as e:
        # Manejar errores de base de datos
        flash(f'Error al guardar el cliente: {str(e)}', 'danger')
        return False