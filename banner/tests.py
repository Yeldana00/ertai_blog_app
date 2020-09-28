from django.test import TestCase

from banner.models import Banner, BANNER_TYPE_CODE


class BannerTestCase(TestCase):

    def test_success_create_banner(self):
        created_banner = Banner.objects.create(
            name="Course",
            type=BANNER_TYPE_CODE,
            code="banner code",
            position=1
        )

        self.assertEquals(created_banner.name, "Course")
        self.assertEquals(created_banner.type, BANNER_TYPE_CODE)
        self.assertEquals(created_banner.code, "banner code")
        self.assertEquals(created_banner.position, 1)
        self.assertFalse(created_banner.is_published)
