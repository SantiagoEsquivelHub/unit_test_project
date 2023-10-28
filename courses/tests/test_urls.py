from django.urls import reverse, resolve
from courses.urls import urlpatterns


class TestUrls:

    # Test para la url detail
    def test_details_url(self):
        path = reverse('courses:detail', args=[1])
        resolver = resolve(path)
        assert resolver.url_name == 'detail'
        assert resolver.kwargs == {'pk': '1'}

    # Test para la url list
    def test_list_url(self):
        path = reverse('courses:list')
        resolver = resolve(path)
        assert resolver.url_name == 'list'

    # Test para la url new
    def test_new_url(self):
        path = reverse('courses:new')
        resolver = resolve(path)
        assert resolver.url_name == 'new'

    # Test para la url edit
    def test_edit_url(self):
        path = reverse('courses:edit', args=[1])
        resolver = resolve(path)
        assert resolver.url_name == 'edit'
        assert resolver.kwargs == {'pk': '1'}

    # Test para la url delete
    def test_delete_url(self):
        path = reverse('courses:delete', args=[1])
        resolver = resolve(path)
        assert resolver.url_name == 'delete'
        assert resolver.kwargs == {'pk': '1'}
