# -*- encoding: utf-8 -*-
##############################################################################
#
#    open2bizz
#    Copyright (C) 2017 open2bizz (open2bizz.nl).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Dream Aesthetics House-housestyle",
    "summary": "Overrides CSS styling of the default Odoo Enterprise theme.",
    "version": "0.1",
    "category": "Website",
    "website": "https://www.open2bizz.nl",
    "author": "Open2bizz",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        'web',
    ],
	"data": [
        'views/assets.xml',
    ],
}
