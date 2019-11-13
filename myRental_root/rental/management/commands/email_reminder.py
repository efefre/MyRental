import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from django.db.models import Count

from rental.models import LoanBook

class Command(BaseCommand):
    help = "Sends an e-mail reminder to users who loaned books more than N days ago"

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int)

    def handle(self, *args, **options):
        emails = []
        subject = 'Przypomnienie ;)'
        date_loan =  datetime.date.today() - datetime.timedelta(days=options['days'])
        friend_who_have_loaned_books = LoanBook.objects.filter(date__lte=date_loan)

        for friend in friend_who_have_loaned_books:
            message = f"Cześć {friend.friend_name},\n\n" \
                f"mam nadzieję, że książka: {friend.book.title} Ci się podoba. " \
                f"Jak tylko skończysz czytać, proszę zwróć ją. Chcę jeszcze do niej kiedyś zajrzeć :)"
            emails.append((subject, message, settings.DEFAULT_FROM_EMAIL, [friend.friend_email]))
        send_mass_mail(emails)
        self.stdout.write(f'Sent {len(emails)} reminders.')
