import os
import logging

from mongodb_odm import Document, connect

logger = logging.getLogger(__name__)


class TestModel(Document):
    full_name: str


def test_test_model():
    connect(os.environ.get("MONGO_URL", ""))

    _ = TestModel(
        full_name="Full Name"
    ).create()
