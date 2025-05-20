import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', ["?promo=newYear"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_product_added_message()
    page.should_be_basket_total_message()
