from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting


class ModelTestCase(TestCase):
    """ "
    Test case for the models in the `lettings` app.
    This test case contains test methods for the creation and deletion of instances of the
    `Address` and `Letting` models.
    Attributes:
      NUMBER (int): The number of the address.
      STREET (str): The street of the address.
      CITY (str): The city of the address.
      STATE (str): The state of the address.
      ZIP_CODE (int): The zip code of the address.
      COUNTRY_ISO_CODE (int): The ISO code of the country.
      TITLE (str): The title of the letting.
      INVALID_NUMBER (str): An invalid number for testing.
      WRONG_ADDRESS (str): An invalid address for testing.
      address (Address): An instance of the `Address` model.
      letting (Letting): An instance of the `Letting` model.
    """

    NUMBER = 2
    STREET = "Place de la Comédie"
    CITY = "Bordeaux"
    STATE = "Gi"
    ZIP_CODE = 33000
    COUNTRY_ISO_CODE = 250
    TITLE = "Test Title Letting"
    INVALID_NUMBER = "rue"
    WRONG_ADDRESS = "No model instance"

    def setUp(self) -> None:
        """
        Set up the test case with an Address and a letting.
        """
        self.address = Address.objects.create(
            number=self.NUMBER,
            street=self.STREET,
            city=self.CITY,
            state=self.STATE,
            zip_code=self.ZIP_CODE,
            country_iso_code=self.COUNTRY_ISO_CODE,
        )
        self.letting = Letting.objects.create(title=self.TITLE, address=self.address)

    def test_address_creation_success(self) -> None:
        """
        Test the successful creation of an instance of the `lettings.Address` model.
        Asserts that the created instance has the expected attributes.
        """
        self.assertEqual(self.address.number, self.NUMBER)
        self.assertEqual(self.address.street, self.STREET)
        self.assertEqual(self.address.city, self.CITY)

    def test_address_creation_fail(self) -> None:
        """
        Test the failed creation of an instance of the `lettings.Address` model.
        Asserts that a ValueError is raised when an invalid number is used.

        :raises ValueError: If an invalid number is used for creating an instance
        of the `lettings.Address` model.
        """
        with self.assertRaises(ValueError):
            Address.objects.create(
                number=self.INVALID_NUMBER,
                street=self.STREET,
                city=self.CITY,
                state=self.STATE,
                zip_code=self.ZIP_CODE,
                country_iso_code=self.COUNTRY_ISO_CODE,
            )

    def test_address_delete_success(self) -> None:
        """
        Test the successful deletion of an instance of the `lettings.Address` model.
        Verify that the instance is deleted from the database.
        """
        self.assertEqual(Address.objects.all().count(), 1)
        self.address.delete()
        self.assertEqual(Address.objects.all().count(), 0)

    def test_letting_create_success(self) -> None:
        """
        Test the successful creation of an instance of the `lettings.Letting` model.
        Asserts that the created instance has the expected attributes.
        """
        self.assertEqual(self.letting.title, self.TITLE)
        self.assertEqual(self.letting.address.number, self.NUMBER)
        self.assertEqual(self.letting.address.street, self.STREET)
        self.assertEqual(self.letting.address.city, self.CITY)
        self.assertEqual(self.letting.address.state, self.STATE)

    def test_letting_create_fail(self) -> None:
        """
        Test the failed creation of an instance of the `lettings.Letting` model.
        Asserts that a ValueError is raised when an invalid address is used.

        :raises ValueError: If an invalid address is used for creating an instance
        of the `lettings.Letting` model.
        """
        with self.assertRaises(ValueError):
            Letting.objects.create(title=self.TITLE, address=self.WRONG_ADDRESS)

    def test_letting_delete_success(self) -> None:
        """
        Test the successful deletion of an instance of the `lettings.Letting` model.
        Verify that the instance is deleted from the database.
        """
        self.assertEqual(Letting.objects.all().count(), 1)
        self.letting.delete()
        self.assertEqual(Letting.objects.all().count(), 0)


class LettingsViewsTestCase(TestCase):
    """
    Test case for the views in the Lettings app.
    """

    NUMBER = 2
    STREET = "Place de la Comédie"
    CITY = "Bordeaux"
    STATE = "Gi"
    ZIP_CODE = 33000
    COUNTRY_ISO_CODE = 250
    TITLE = "Test Title Letting"

    def setUp(self) -> None:
        """
        Set up the necessary objects for each test case.
        """
        self.address = Address.objects.create(
            number=self.NUMBER,
            street=self.STREET,
            city=self.CITY,
            state=self.STATE,
            zip_code=self.ZIP_CODE,
            country_iso_code=self.COUNTRY_ISO_CODE,
        )
        self.letting = Letting.objects.create(title=self.TITLE, address=self.address)

    def test_index_view(self) -> None:
        """
        Test the index view.
        """
        response = self.client.get(reverse("lettings:lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.letting.title)
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_letting_view(self) -> None:
        """
        Test the letting view.
        """
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.letting.title)
        self.assertContains(response, self.letting.address.number)
        self.assertContains(response, self.letting.address.street)
        self.assertContains(response, self.letting.address.city)
        self.assertContains(response, self.letting.address.state)
        self.assertTemplateUsed(response, "letting.html")

    def test_letting_view_not_found(self) -> None:
        """
        Test the letting view when the letting is not found.
        """
        response = self.client.get(
            reverse("lettings:letting", args=[self.letting.pk + 1])
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
