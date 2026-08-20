import tempfile
import unittest
from pathlib import Path

from app import server


class ServerLibraryTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.library = Path(self.tempdir.name)
        self.original_library = server.LIBRARY_ROOT
        server.LIBRARY_ROOT = self.library

    def tearDown(self):
        server.LIBRARY_ROOT = self.original_library
        self.tempdir.cleanup()

    def test_discover_folders_filters_hidden_and_repository_directories(self):
        (self.library / "travel").mkdir()
        (self.library / "family").mkdir()
        (self.library / ".hidden").mkdir()
        (self.library / server.REPO_ROOT.name).mkdir()

        self.assertEqual(server.discover_folders(), ["family", "travel"])

    def test_list_images_accepts_supported_files_only(self):
        album = self.library / "travel"
        album.mkdir()
        (album / "one.jpg").write_bytes(b"jpg")
        (album / "two.PNG").write_bytes(b"png")
        (album / "notes.txt").write_text("not an image", encoding="utf-8")

        images = server.list_images(["travel"], limit=20)

        self.assertEqual({item["name"] for item in images}, {"one.jpg", "two.PNG"})
        self.assertTrue(all(item["folder"] == "travel" for item in images))

    def test_list_images_rejects_paths_outside_library(self):
        outside = self.library.parent / "outside-guess-crop-test"
        outside.mkdir(exist_ok=True)
        try:
            (outside / "outside.jpg").write_bytes(b"jpg")
            self.assertEqual(server.list_images(["../outside-guess-crop-test"]), [])
        finally:
            (outside / "outside.jpg").unlink(missing_ok=True)
            outside.rmdir()


if __name__ == "__main__":
    unittest.main()
