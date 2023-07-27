from django.test import TestCase, Client
from django.urls import reverse
from parameterized import parameterized

from dish.models import MenuSection, DishType, Dish


class ModelsTests(TestCase):
    def setUp(self) -> None:
        self.section = MenuSection.objects.create(name='Breakfasts')
        self.type1 = DishType.objects.create(name='Type1', section=self.section)
        self.type2 = DishType.objects.create(name='Type2', section=self.section)
        self.dish1 = Dish.objects.create(
            name='Dish1',
            description="Some words for this super test description",
            photo="https//test-dish-image/testimage1.png",
            type=self.type1,
            price=123
        )
        self.dish2 = Dish.objects.create(
            name='Dish2',
            description="Some words another for this super test description",
            photo="https//test-dish-image/testimage2.png",
            type=self.type1,
            price=123
        )
        self.dish3 = Dish.objects.create(
            name='Dish3',
            description="Some words one more for this super test description",
            photo="https//test-dish-image/testimage3.png",
            type=self.type2,
            price=123
        )

    def test_menu_section_str(self) -> None:
        self.assertEqual(str(self.section), self.section.name)

    def test_dish_type_str(self) -> None:
        self.assertEqual(str(self.type2), self.type2.name)

    def test_dish_str(self) -> None:
        self.assertEqual(
            str(self.dish1),
            f"{self.dish1.name}, type({self.dish1.type.name}) "
            f"price:{self.dish1.price}"
        )

    def test_dish_type_view(self) -> None:
        client = Client()
        url = reverse("dish:dish-list", args=[self.type1.name])
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        dish_list = response.context["dish_list"]
        self.assertEqual(list(dish_list), [self.dish1, self.dish2])

        type_list = response.context["type_list"]
        self.assertEqual(list(type_list), [self.type1, self.type2])

        section_name = response.context["section_name"]
        self.assertEqual(section_name, "Breakfasts")
