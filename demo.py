import os
import django

SETTINGS = 'activflow.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = SETTINGS


def main():
    """Entry Point"""
    print ('Setting Up demo...')
    django.setup()
    # os.system('del /f db.sqlite3')
    # os.system('del /f activflow/core/migrations')
    # os.system('del /f activflow/tests/migrations')
    # os.system('./manage.py makemigrations core tests')
    # os.system('./manage.py migrate')
    # print ('Create Superuser...')
    # os.system('./manage.py createsuperuser --email=demo@activflow.com')

    from django.contrib.auth.models import Group, User

    submitter = Group.objects.create(name='Submitter')
    reviewer = Group.objects.create(name='Reviewer')

    john_doe = User.objects.create_user(
        'john.doe',
        'john@company.com',
        '12345')

    jane_smith = User.objects.create_user(
        'jane.smith',
        'jane@company.com',
        '12345')

    submitter.user_set.add(john_doe)
    reviewer.user_set.add(jane_smith)


if __name__ == '__main__':
    main()
