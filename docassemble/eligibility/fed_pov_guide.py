from docassemble.base.util import DAObject
from docassemble.base.functions import get_config
from airtable import Airtable

def federal_poverty_guideline(base, per_person, household_size):
	return (base + (household_size - 1) * per_person)

def get_scheduled_value(table_name):
	fpg_table = Airtable('appTjL6HbRtZSScDo', table_name, api_key=get_config('airtable'))
	fpg_record = fpg_table.search('date_time', '2019-01-11T00:00:00.000Z',
      fields=['date_time', 'base', 'per_person'], max_records=10).pop()
	if 'date_time' in fpg_record['fields'] \
	and 'base' in fpg_record['fields'] \
	and 'per_person' in fpg_record['fields']:
		fpg = DAObject()
		fpg.base = fpg_record['fields']['base']
		fpg.per_person = fpg_record['fields']['per_person']
		fpg.date_time = fpg_record['fields']['date_time']
		return fpg
	return None