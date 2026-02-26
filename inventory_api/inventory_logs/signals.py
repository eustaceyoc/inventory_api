from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from inventory.models import InventoryItem
from .models import InventoryLog

@receiver(post_save, sender=InventoryItem)
def log_inventory_item_save(sender, instance, created, **kwargs):
    if created:
        InventoryLog.objects.create(
            inventory_item=instance,
            user=instance.user,
            change_type="create",
            previous_quantity=None,
            new_quantity=instance.quantity
        )
    else:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            previous_quantity = old_instance.quantity
        except sender.DoesNotExist:
            previous_quantity = None

        if previous_quantity != instance.quantity:
            change_type = "update_quantity"
        else:
            change_type = "update_other"

        InventoryLog.objects.create(
            inventory_item=instance,
            user=instance.user,
            change_type=change_type,
            previous_quantity=previous_quantity,
            new_quantity=instance.quantity
        )

@receiver(post_delete, sender=InventoryItem)
def log_inventory_item_delete(sender, instance, **kwargs):
    InventoryLog.objects.create(
        inventory_item=instance,
        user=instance.user,
        change_type="delete",
        previous_quantity=instance.quantity,
        new_quantity=None
    )
