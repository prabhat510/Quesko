from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

# LoginRequiredMixin is used so that only authenticated users are allowed
#  to interact with the app plus they will be automatically redirected to login page(if not authenticated)

from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf import settings


class IndexTemplateView(LoginRequiredMixin, TemplateView):

    # to define which template name to use
    def get_template_names(self):
        template_name = index-dev.html
        return template_name
