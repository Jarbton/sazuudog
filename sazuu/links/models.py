from django.db import models
from model_utils.models import TimeStampedModel
from django.core.files.storage import get_storage_class
from django.conf import settings

# Emoji references from
# https://www.w3schools.com/charsets/ref_emoji.asp
NO_LOGO = '129430'
INSTAGRAM = '128248'
TIKTOK = '127925'
TWITCH = '128250'
TWITTER = '128036'
DISCORD = '127918'

LOGOS = (
    ((NO_LOGO, 'No Logo'), (INSTAGRAM, 'Instagram'), (TIKTOK, 'TikTok'), 
    (TWITCH, 'Twitch'), (TWITTER, 'Twitter'), (DISCORD, 'Discord'))
)

class Link(TimeStampedModel):
    """
    A link is a URL to a social media account with other useful data.
    """
    service = models.CharField(max_length=250, help_text="Title of service e.g Facebook.")
    url = models.URLField(max_length=500, help_text="Url to account page on service.")
    username = models.CharField(default="@SazuuDog", max_length=300, help_text="Username on this service.")
    icon = models.CharField(max_length=30, default=NO_LOGO, choices=LOGOS, help_text='Emoji logo for this service.')
    display = models.BooleanField(default=False, help_text="Indicate if link should be displayed.")
    sort_order = models.IntegerField(default=0, help_text="Used to order the links")

    def __str__(self):
        return self.service


class Click(TimeStampedModel):
    """
    Click object references a link to track when a link has been clicked.
    """
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='clicks', help_text='The link that was clicked')
