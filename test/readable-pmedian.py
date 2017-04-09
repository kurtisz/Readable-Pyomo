import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from readablepyomo.readablepyomo import *
from readablepyomo.glpk import Glpk

CandidateLocations = Set("M")
CustomerDemandNodes = Set("N")

NumberOfFacilities = Parameter("p").within(PositiveIntegers)
CustomerDemand = Parameter("d").over(CustomerDemandNodes).within(NonNegativeReals).with_default(1.0)
CustomerSatisfactionCost = Parameter("c").over(CandidateLocations, CustomerDemandNodes).within(NonNegativeReals)

SuppliedDemand = Variable("x").over(CandidateLocations, CustomerDemandNodes).within(NonNegativeReals)
FacilityAtLocation = Variable("y").over(CandidateLocations).within(Binary)

Glpk.solve(
	given(
		sets(CandidateLocations, CustomerDemandNodes),
		parameters(NumberOfFacilities, CustomerDemand, CustomerSatisfactionCost),
		variables(SuppliedDemand, FacilityAtLocation)
		)																																	\
		.minimize(sum_over(CandidateLocations)(sum_over(CustomerDemandNodes)(CustomerDemand * CustomerSatisfactionCost * SuppliedDemand)))	\
		.such_that(sum_over(CandidateLocations)(SuppliedDemand).equals(1))																	\
		.such_that(SuppliedDemand.is_less_than_or_equal_to(FacilityAtLocation))																\
		.such_that(SuppliedDemand.is_greater_than_or_equal_to(0)),
		"pmedian.dat"
	).write()