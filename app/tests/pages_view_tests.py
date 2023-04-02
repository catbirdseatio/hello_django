from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed, assertContains, assertNotContains
from pages.views import HomePageView, AboutPageView


class TestHomepage:
    url = reverse("index")

    def test_homepage_status_code(self, rf):
        request = rf.get(self.url)
        response = HomePageView.as_view()(request)
        assert response.status_code == 200

    def test_homepage_template(self, client):
        response = client.get(self.url)
        assertTemplateUsed(response, "pages/index.html")

    def test_homepage_contains_correct_html(self, rf):
        request = rf.get(self.url)
        response = HomePageView.as_view()(request)
        assertContains(response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self, rf):
        request = rf.get(self.url)
        response = HomePageView.as_view()(request)
        assertNotContains(response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self, rf):
        view = resolve("/")
        assert view.func.__name__ == HomePageView.as_view().__name__

class TestAboutpage:
    url = reverse("index")

    def test_aboutpage_status_code(self, rf):
        request = rf.get(self.url)
        response = AboutPageView.as_view()(request)
        assert response.status_code == 200

    def test_aboutpage_template(self, client):
        response = client.get(self.url)
        assertTemplateUsed(response, "pages/index.html")

    def test_aboutpage_contains_correct_html(self, rf):
        request = rf.get(self.url)
        response = AboutPageView.as_view()(request)
        assertContains(response, "About Bookstore")

    def test_aboutpage_does_not_contain_incorrect_html(self, rf):
        request = rf.get(self.url)
        response = AboutPageView.as_view()(request)
        assertNotContains(response, "Hi there! I should not be on the page.")

    def test_aboutpage_url_resolves_aboutpageview(self, rf):
        view = resolve("/")
        assert view.func.__name__ == AboutPageView.as_view().__name__
