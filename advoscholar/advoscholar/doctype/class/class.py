# Copyright (c) 2024, Jupytec and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Class(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from advoscholar.advoscholar.doctype.class_fees.class_fees import ClassFees
		from advoscholar.advoscholar.doctype.class_subject.class_subject import ClassSubject
		from frappe.types import DF

		class_fees: DF.Table[ClassFees]
		multiple_teachers: DF.Check
		subjects: DF.Table[ClassSubject]
		teacher: DF.Link
	# end: auto-generated types

	pass
