from django.db import IntegrityError
from django.test import TestCase

from profiles.models import Profile
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ModelTestCase(TestCase):
    """
    Test case for the UserModel and Profile model.

    Attributes:
        USERNAME (str): The username of the user.
        MAIL (str): The email of the user.
        PASSWORD (str): The password of the user.
        FIRST_NAME (str): The first name of the user.
        LAST_NAME (str): The last name of the user.
        FAVORITE_CITY (str): The favorite city of the user.
        user (User): An instance of the UserModel.
        profile (Profile): An instance of the Profile
    """

    USERNAME = "Test User"
    MAIL = "test@test.com"
    PASSWORD = "testpassword"
    FIRST_NAME = "Test"
    LAST_NAME = "User"
    FAVORITE_CITY = "Paris"

    def setUp(self) -> None:
        """
        Set up the test case with a user and profile.
        """
        self.user = UserModel.objects.create_user(
            username=self.USERNAME,
            email=self.MAIL,
            password=self.PASSWORD,
            first_name=self.FIRST_NAME,
            last_name=self.LAST_NAME,
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city=self.FAVORITE_CITY
        )

    def test_user_creation_success(self) -> None:
        """
        Test that a user is created successfully with the correct attributes.
        """
        self.assertEqual(self.user.username, self.USERNAME)
        self.assertEqual(self.user.email, self.MAIL)
        self.assertEqual(self.user.first_name, self.FIRST_NAME)
        self.assertEqual(self.user.last_name, self.LAST_NAME)

    def test_user_creation_fail(self) -> None:
        """
        Test that creating a user with empty fields raises a ValueError.
        """
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(
                username="",
                email="",
                password="",
                first_name="",
                last_name="",
            )

    def test_user_cannot_be_created_multiple_times(self) -> None:
        """
        Test that creating a user with the same username, email, and password
        raises an IntegrityError.
        """
        with self.assertRaises(IntegrityError):
            UserModel.objects.create_user(
                username=self.USERNAME,
                password=self.PASSWORD,
                email=self.MAIL,
                first_name=self.FIRST_NAME,
                last_name=self.LAST_NAME,
            )

    def test_user_delete_successful(self) -> None:
        """
        Test that a user is deleted successfully.
        """
        self.assertEqual(UserModel.objects.all().count(), 1)
        self.user.delete()
        self.assertEqual(UserModel.objects.all().count(), 0)

    def test_profile_creation_success(self) -> None:
        """
        Test that a profile is created successfully with the correct attributes.
        """
        self.assertEqual(self.profile.favorite_city, self.FAVORITE_CITY)
        self.assertEqual(self.profile.user, self.user)

    def test_profile_delete_successful(self) -> None:
        """
        Test that a profile is deleted successfully.
        """
        self.assertEqual(Profile.objects.all().count(), 1)
        self.profile.delete()
        self.assertEqual(Profile.objects.all().count(), 0)


class ProfilesViewsTestCase(TestCase):
    """
    Test case for the profile views.
    """

    USERNAME = "Test User"
    MAIL = "test@test.com"
    PASSWORD = "testpassword"
    FIRST_NAME = "Test"
    LAST_NAME = "User"
    FAVORITE_CITY = "Paris"

    def setUp(self) -> None:
        """
        Set up the test case with a user and profile.
        """
        self.user = UserModel.objects.create_user(
            username=self.USERNAME,
            email=self.MAIL,
            password=self.PASSWORD,
            first_name=self.FIRST_NAME,
            last_name=self.LAST_NAME,
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city=self.FAVORITE_CITY
        )

    def test_profiles_index_view(self) -> None:
        """
        Test that the profiles index view returns a 200 status code
        and contains the correct user information.
        """
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.profile.user.username)
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profile_detail_view(self) -> None:
        """
        Test that the profile detail view returns a 200 status code
        and contains the correct profile information.
        """
        response = self.client.get(f"/profiles/{self.profile.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.profile.favorite_city)
        self.assertContains(response, self.profile.user.username)
        self.assertContains(response, self.profile.user.email)
        self.assertContains(response, self.profile.user.first_name)
        self.assertContains(response, self.profile.user.last_name)
        self.assertTemplateUsed(response, "profile.html")

    def test_profile_detail_view_not_found(self) -> None:
        """
        Test that the profile detail view returns a 404 status code when the profile is not found.
        """
        response = self.client.get(f"/profiles/{self.profile.pk+1}/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
