def federal_poverty_guideline(base, per_person, household_size):
	return (base + (household_size - 1) * per_person)