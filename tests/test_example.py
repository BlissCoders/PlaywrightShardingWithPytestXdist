import re

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("page_num", range(1, 11))
def test_multiple_pages(page: Page, page_num):
    """Simulates a suite with multiple tests to demonstrate sharding."""
    page.goto("https://playwright.dev/")
    import re
    expect(page).to_have_title(re.compile("Playwright"))
