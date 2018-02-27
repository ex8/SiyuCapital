from django.contrib import admin
from newsletter.models import Recipient, NewsLetter
from django.core.mail import EmailMessage, send_mail


class NewsletterAdmin(admin.ModelAdmin):
    model = NewsLetter
    list_display = ('title', 'created', 'published', 'sort', 'author')
    search_fields = ('title', 'content')
    list_filter = ('published',)
    raw_id_fields = ('author',)
    actions = ['send_newsletter_email']

    def send_newsletter_email(self, request, queryset):
        for o in queryset:
            if o.published is True:
                peeps = Recipient.objects.filter(subscribed=True)
                for p in peeps:
                    send_mail(subject=o.title, html_message=o.content,
                                     recipient_list=[p.email],
                                     from_email='newsletter@siyucapital.com', message='')
                    # mail = EmailMessage(to=[p.email], subject=o.title, body=o.content,
                    # from_email='newsletter@siyucapital.com')
                    # mail.send()
        self.message_user(request=request, message='Newsletter mass mail sent successful.')
    send_newsletter_email.short_description = 'Send newsletter to all SUBSCRIBED recipients'
admin.site.register(model_or_iterable=NewsLetter, admin_class=NewsletterAdmin)


class RecipientAdmin(admin.ModelAdmin):
    model = Recipient
    list_display = ('first', 'last', 'email', 'subscribed', 'created')
    search_fields = ('first', 'last', 'email')
    list_filter = ('subscribed',)
admin.site.register(model_or_iterable=Recipient, admin_class=RecipientAdmin)
