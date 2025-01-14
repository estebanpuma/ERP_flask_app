from flask import current_app

from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime

import pytz

from app import db


quito_tz = pytz.timezone('America/Guayaquil')


def utc_now():
    return datetime.now(pytz.utc).astimezone(quito_tz)


class ValidationError(Exception):
    pass

class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=utc_now)
    updated_at = db.Column(db.DateTime, default=utc_now, onupdate=utc_now)

    def validate(self):
        """
        Método base para validación. Cada modelo debe implementar su propia lógica de validación.
        """
        return True

    def save(self):
        try:
            if not self.validate():
                raise ValidationError("Validation failed")
            db.session.add(self)
            db.session.commit()
            current_app.logger.info(f'Registro guardado: {self}')
            return True, None
        except ValidationError as e:
            current_app.logger.warning(f'ValidationError: {e}')
            return False, str(e)
        except SQLAlchemyError as e:
            db.session.rollback()
            current_app.logger.warning(f'SQLAlchemyError: {e}')
            return False, str(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            current_app.logger.info(f'Registro eliminado: {self}')
            return True, None
        except SQLAlchemyError as e:
            db.session.rollback()
            current_app.logger.warning(f'SQLAlchemyError: {e}')
            return False, str(e)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()