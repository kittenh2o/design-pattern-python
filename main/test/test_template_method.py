from unittest import TestCase, mock

from src.template_method import (MaldiveTrip, TravelAgency, VeniceTrip,
                                 iOSCompiler)


class TestCompiler(TestCase):
    def test_ios_compiler(self):
        iOS = iOSCompiler()
        iOS.compile_and_run()


class TestTrip(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.locations = ["Maldive", "Venice"]

    def test_travel_agency(self):
        agency = TravelAgency()
        with mock.patch("builtins.input", return_value=self.locations[0]):
            agency.arrange_trip()
        self.assertIsInstance(agency.trip, MaldiveTrip)

        with mock.patch("builtins.input", return_value=self.locations[1]):
            agency.arrange_trip()
        self.assertIsInstance(agency.trip, VeniceTrip)
