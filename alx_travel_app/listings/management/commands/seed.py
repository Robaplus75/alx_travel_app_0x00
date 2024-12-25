from django.core.management.base import BaseCommand
from datetime import date
import random
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review



class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        users = [User.objects.create_user(username=f'user{i}', password='password123') for i in range(1, 6)]
        for i in range(1, 11):
            listing = Listing.objects.create(
                title=f"Listing {i}",
                description=f"This is a description for listing {i}.",
                price_per_night=random.randint(50, 500),
                available_from=date.today(),
                available_to=date.today(),
                owner=random.choice(users)
            )
            self.stdout.write(self.style.SUCCESS(f"Completed listing: {listing.title}"))
            for _ in range(random.randint(0, 5)):
                booking = Booking.objects.create(
                    listing=listing,
                    user=random.choice(users),
                    start_date=date.today(),
                    end_date=date.today(),
                    status=random.choice(['confirmed', 'pending', 'canceled'])
                )
                self.stdout.write(self.style.SUCCESS(f"Created booking for: {booking.listing.title} by {booking.user.username}"))
            for _ in range(random.randint(0, 3)):
                review = Review.objects.create(
                    listing=listing,
                    user=random.choice(users),
                    rating=random.randint(1, 5),
                    comment=f"This is a review for {listing.title}.",
                )
                self.stdout.write(self.style.SUCCESS(f"Created review for: {review.listing.title} by {review.user.username}"))
