from django.db import models
#Models for alx_trave app

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available_to = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='listings', on_delete=models.CASCADE)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()


    def __str__(self):
        return self.title



class Review(models.Model):
    listing = models.ForeignKey(Listing, related_name='reviews', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    def __str__(self):
        return f"Review by {self.user.username} for {self.listing.title}"

class Booking(models.Model):
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], default='pending')

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.user.username}"


