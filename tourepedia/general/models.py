from django.db import models

class Inclusion(models.Model):
	inclusion_type = models.CharField(max_length=250, null=True)

	def __str__(self):
		return self.inclusion_type

class TourInclusion(models.Model):
	inclusion = models.ForeignKey(Inclusion)
	tour_inclusion = models.CharField(max_length=250,null=True)

class SchoolTourInclusion(models.Model):
	inclusion = models.ForeignKey(Inclusion)
	school_tour_inclusion = models.CharField(max_length=250, null=True)


class Exclusion(models.Model):
	exclusion_type = models.CharField(max_length=250, null=True)

	def __str__(self):
		return self.exclusion_type

class TourExclusion(models.Model):
	exclusion = models.ForeignKey(Exclusion)
	tour_exclusion = models.CharField(max_length=250, null=True)

class SchoolTourExclusion(models.Model):
	exclusion = models.ForeignKey(Exclusion)

	school_tour_exclusion = models.CharField(max_length=250, null=True)



class Term(models.Model):
	term_type = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.term_type



class TermNCondition(models.Model):
	term = models.ForeignKey(Term, null=True)
	heading = models.CharField(max_length=250, null=True)
	content = models.TextField(max_length=250, null=True)

	def __str__(self):
		return self.heading


class PrivacyPolicy(models.Model):
	heading = models.CharField(max_length=250, null=True)
	content = models.TextField(max_length=250, null=True)

	def __str__(self):
		return self.heading


class CancellationPolicy(models.Model):
	heading = models.CharField(max_length=250, null=True)
	content = models.TextField(max_length=250, null=True)
