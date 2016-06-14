# -*- coding: utf-8 -*-
# Copyright <2016> <Rossa S.A.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Migrate Abaco",
    "summary": "Migrate data from Abaco system",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sistema.social",
    "author": "<Rossa S.A.>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "post_load": "post_load",
    "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
    ],
    "data": [
        "security/some_model_security.xml",
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/report_name.xml",
        "views/res_partner_view.xml",
        "wizard/wizard_model_view.xml",
    ],
    "demo": [
        "demo/res_partner_demo.xml",
    ],
    "qweb": [
        "static/src/xml/module_name.xml",
    ]
}
