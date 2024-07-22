from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from offices.models import Account, HeadOffice, DistrictOffice, BranchLocation

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a new superuser with associated owner and office structure'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('business_name', type=str)

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']
        business_name = options['business_name']

        # Create superuser
        user = User.objects.create_superuser(email=email, password=password)

        # Create account
        account = Account.objects.create(user=user, business_name=business_name)

        # Create head office
        head_office = HeadOffice.objects.create(account=account, name=f"{business_name} Head Office")

        # Create a sample district office
        district_office = DistrictOffice.objects.create(head_office=head_office, name=f"{business_name} District Office")

        # Create a sample branch location
        BranchLocation.objects.create(district_office=district_office, name=f"{business_name} Branch")

        self.stdout.write(self.style.SUCCESS(f'Successfully created new owner superuser: {email}'))