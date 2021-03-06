from wtforms import Form, StringField, BooleanField, IntegerField, SelectField, validators
from hardwarecheckout.forms.inventory_update_form import InventoryUpdateForm
from hardwarecheckout.models.inventory_entry import ItemType

def validate_quantity(form, field):
    return field.data != None or form.item_type == ItemType.FREE

class InventoryForm(InventoryUpdateForm):
   quantity = IntegerField('quantity', [validators.Optional(), validators.NumberRange(min=0), validate_quantity])
