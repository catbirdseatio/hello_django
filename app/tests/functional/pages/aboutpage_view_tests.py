import pytest
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed, assertContains, assertNotContains
from pages.views import HomePageView, AboutPageView


# This fixture is to be used only in this module
@pytest.fixture(scope="class")
def url():
    return reverse("about")


class TestAboutpage:
    def test_aboutpage_status_code(self, rf, url):
        request = rf.get(url)
        response = AboutPageView.as_view()(request)
        assert response.status_code == 200

    def test_aboutpage_template(self, client, url):
        response = client.get(url)
        assertTemplateUsed(response, "pages/about.html")

    def test_aboutpage_contains_correct_html(self, rf, url):
        request = rf.get(url)
        response = AboutPageView.as_view()(request)
        assertContains(response, "About Boilerplate")

    def test_aboutpage_does_not_contain_incorrect_html(self, rf, url):
        request = rf.get(url)
        response = AboutPageView.as_view()(request)
        assertNotContains(response, "Hi there! I should not be on the page.")

    def test_aboutpage_url_resolves_aboutpageview(self, rf):
        view = resolve("/")
        assert view.func.__name__ == AboutPageView.as_view().__name__
