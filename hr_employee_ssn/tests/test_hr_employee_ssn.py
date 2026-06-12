# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import TransactionCase


class TestHrEmployeeSsn(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))

    def test_employee_ssn_fields(self):
        employee = self.env["hr.employee"].create(
            {
                "name": "Test Employee",
                "ssnid": "123-45-6789",
                "sinid": "123 456 789",
            }
        )
        self.assertEqual(employee.ssnid, "123-45-6789")
        self.assertEqual(employee.sinid, "123 456 789")
