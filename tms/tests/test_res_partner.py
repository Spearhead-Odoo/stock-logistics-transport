from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):
    def setUp(self):
        super().setUp()

        self.stage = self.env["tms.stage"].create(
            {
                "name": "Test Stage",
                "stage_type": "driver",
                "sequence": 1,
            }
        )

        self.driver = self.env["res.partner"].create(
            {
                "name": "Test Driver",
                "tms_type": "driver",
                "is_external": True,
                "driver_type": "terrestrial",
                "driver_license_number": "ABC123456",
                "driver_license_type": "B",
                "distance_traveled": 1000,
                "distance_traveled_uom": "km",
                "driving_experience_years": 5,
            }
        )

        self.location = self.env["res.partner"].create(
            {
                "name": "Test Location",
                "tms_type": "location",
                "location_type": "terrestrial",
            }
        )

    def test_driver_creation(self):
        self.driver._default_stage_id()

        self.assertTrue(self.driver, "Driver wasn't created successfully")
        self.assertEqual(
            self.driver.name, "Test Driver", "Driver name should be 'Test Driver'"
        )
        self.assertTrue(self.driver.is_external, "Driver should be marked as external")
        self.assertEqual(
            self.driver.driver_type,
            "terrestrial",
            "Driver type should be 'terrestrial'",
        )
        self.assertEqual(
            self.driver.driver_license_number,
            "ABC123456",
            "Driver license number should be 'ABC123456'",
        )
        self.assertEqual(
            self.driver.driver_license_type, "B", "Driver license type should be 'B'"
        )
        self.assertEqual(
            self.driver.distance_traveled, 1000, "Distance traveled should be 1000"
        )
        self.assertEqual(
            self.driver.driving_experience_years,
            5,
            "Driving experience years should be 5",
        )
        self.assertTrue(
            self.driver.stage_id, "Driver stage should be correctly assigned"
        )

    def test_location_creation(self):
        self.assertTrue(self.location, "Location wasn't created successfully")
        self.assertEqual(
            self.location.name,
            "Test Location",
            "Location name should be 'Test Location'",
        )
        self.assertEqual(
            self.location.location_type,
            "terrestrial",
            "Location type should be 'terrestrial'",
        )
