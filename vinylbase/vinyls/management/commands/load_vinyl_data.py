from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from pytz import UTC
from vinyls.models import Vinyl, Genre  # It is fine for this to be underlined


class Command(BaseCommand):

    # Show this when the user types help
    help = "Loads data from initial_vinyl_data.csv"

    def handle(self, *args, **options):

        # Check whether the data about vinyls and genres is not already loaded
        if Genre.objects.exists() or Vinyl.objects.exists():
            print('Vinyl data already loaded...exiting.')
            print("If you need to reload the pet data from the CSV file, first delete the db.sqlite3 file to destroy "
                  "the database. Then, run `python manage.py migrate` for a new empty database with tables")
            return

        # --------------------------------------------------------------------------------------------------------------

        # Load genres data
        available_genres = [
            'Rock',
            'Progressive Rock',
            'Pop',
            'Punk Rock',
            'Psychedelic Rock',
            'Brit Rock',
            'Dance',
            'Grunge'
        ]
        for genre_name in available_genres:

            # Initialize a Genre object
            genre = Genre(name=genre_name)
            genre.save()

        print("Genres data loaded successfully")

        # --------------------------------------------------------------------------------------------------------------

        # Load vinyls data
        for row in DictReader(open('./initial_vinyl_data.csv')):

            # Initialize a Vinyl object and assign the various properties in the CSV row to it
            vinyl = Vinyl()
            vinyl.album = row['Album']
            vinyl.artist = row['Artist']
            vinyl.label = row['Label']
            vinyl.original_year = row['Original Year']
            vinyl.no_songs = row['Number of Songs']
            vinyl.description = row['Description']
            vinyl.edition = row['Edition']
            vinyl.condition = row['Condition']
            raw_submission_date = row['Submission Date']
            submission_date = UTC.localize(datetime.strptime(raw_submission_date, '%m/%d/%Y %H:%M'))
            vinyl.submission_date = submission_date
            vinyl.save()

            # Couple the genres of the vinyl to the available genres
            raw_genres = row['Genres']
            genres = [name for name in raw_genres.split(' | ') if name]
            for genre_name in genres:
                genre = Genre.objects.get(name=genre_name)
                vinyl.genre.add(genre)
            vinyl.save()

        print("Vinyl data loaded successfully")
