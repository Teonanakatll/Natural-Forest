from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from . models import ImageItem, TextItem, GenericGalleryItem

@receiver(post_save, sender=ImageItem)
def create_generic_gallery_item_for_image(sender, instance, created, **kwargs):
    content_type = ContentType.objects.get_for_model(ImageItem)

    GenericGalleryItem.objects.update_or_create(
        content_type=content_type,
        object_id=instance.id,
        defaults={'gallery': instance.gallery}
    )

@receiver(post_save, sender=TextItem)
def create_generic_gallery_item_for_text(sender, instance, created, **kwargs):
    content_type = ContentType.objects.get_for_model(TextItem)

    GenericGalleryItem.objects.update_or_create(
        content_type=content_type,
        object_id=instance.id,
        defaults={'gallery': instance.gallery}
    )