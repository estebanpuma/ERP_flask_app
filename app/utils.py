

def update_form_choices(field, obj):

    choices = [('', 'Seleccione una linea')]

    choices += [(c.id, c.name) for c in obj.query.all()]

    field.choices = choices
 