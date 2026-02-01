from django.core.management.base import BaseCommand

from api.models import Book


class Command(BaseCommand):
    help = 'Load a set of dummy books into the Book model'

    def handle(self, *args, **options):
        samples = [
            ("The Hobbit", "J.R.R. Tolkien"),
            ("1984", "George Orwell"),
            ("To Kill a Mockingbird", "Harper Lee"),
            ("Pride and Prejudice", "Jane Austen"),
            ("The Catcher in the Rye", "J.D. Salinger"),
            ("Moby-Dick", "Herman Melville"),
            ("War and Peace", "Leo Tolstoy"),
            ("The Great Gatsby", "F. Scott Fitzgerald"),
            ("Brave New World", "Aldous Huxley"),
            ("The Lord of the Rings", "J.R.R. Tolkien"),
        ]

        created = 0
        for title, author in samples:
            obj, was_created = Book.objects.get_or_create(title=title, author=author)
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Loaded {created} new books.'))