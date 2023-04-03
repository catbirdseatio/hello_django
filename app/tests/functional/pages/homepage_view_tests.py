import pytest
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed, assertContains, assertNotContains
from pages.views import HomePageView, AboutPageView


# This fixture is to be used only in this module
@pytest.fixture(scope="class")
def url():
    return reverse("index")


class TestHomepage:
    def test_homepage_status_code(self, rf, url):
        request = rf.get(url)
        response = HomePageView.as_view()(request)
        assert response.status_code == 200

    def test_homepage_template(self, client, url):
        response = client.get(url)
        assertTemplateUsed(response, "pages/index.html")

    def test_homepage_contains_correct_html(self, rf, url):
        request = rf.get(url)
        response = HomePageView.as_view()(request)
        assertContains(response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self, rf, url):
        request = rf.get(url)
        response = HomePageView.as_view()(request)
        assertNotContains(response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self, rf):
        view = resolve("/")
        assert view.func.__name__ == HomePageView.as_view().__name__
