import json

name = input('region:')
avgAge = float(input('avgAge:'))
avgUSD = float(input('avgDailyIncomeInUSD:'))
dailyIncomePop = float(input('avgDailyIncomePopulation:'))
period = input('periodType:')
time = int(input('timeToElapse:'))
cases = int(input('reportedCases:'))
population = int(input('population:'))
beds = int(input('totalHospitalBeds:'))
data = {
    'region': name, 'avgAge': avgAge,
    'avgDailyIncomeInUSD': avgUSD,
    'avgDailyIncomePopulation': dailyIncomePop,
    'periodType': period, 'timeToElapse': time,
    'reportedCases': cases, 'population': population,
    'totalHospitalBeds': beds
}


# CHALLENGE 1


def estimator(data):
    currentlyInfected = (data['reportedCases'] * 10) // 1
    severeImpact_currentlyInfected = (data['reportedCases'] * 50) // 1
    factor = data['timeToElapse'] // 3
    impact_infectionsByRequestedTime = currentlyInfected * 2 ** factor
    severeImpact_infectionsByRequestedTime = severeImpact_currentlyInfected * 2 ** factor

    # CHALLENGE 2

    # This is the estimated number of normal positive \n
    # cases that will require hospitalization to recover.
    impact_severeCasesByRequestTime = (
                                              impact_infectionsByRequestedTime * 0.15) // 1
    # This is the estimated number of severe impact positive \n
    # cases that will require hospitalization to recover.
    severeImpact_severeCasesByRequestTime = (
                                                    severeImpact_infectionsByRequestedTime * 0.15) // 1
    # hospitals usually are at 90% or 95% capacity.
    averageOccupation = 0.925  # percentage expressed as fraction if 100%
    hospitalCapacity = data['totalHospitalBeds'] * averageOccupation
    # On average, 65% of hospital beds are already occupied by patients
    impact_hospitalBedsByRequestedTime = ((
                                                  hospitalCapacity * 0.35) - impact_severeCasesByRequestTime) // 1
    severeImpact_hospitalBedsByRequestedTime = ((
                                                        hospitalCapacity * 0.35) - severeImpact_severeCasesByRequestTime) // 1

    # CHALLENGE 3

    # This is the estimated number of impact positive \n
    # cases that will require ICU hospitalization to recover.
    impactCasesForICUByRequestTime = (
                                             impact_infectionsByRequestedTime * 0.05) // 1
    # This is the estimated number of severe positive \n
    # cases that will require ICU hospitalization to recover.
    severeImpactCasesForICUByRequestTime = (
                                                   severeImpact_infectionsByRequestedTime * 0.05) // 1

    # This is the estimated number of impact positive cases that will require
    # ventilators.
    impact_casesForVentilatorsByRequestTime = (
                                                      impact_infectionsByRequestedTime * 0.02) // 1
    # This is the estimated number of severe positive cases that will require
    # ventilators.
    severeImpact_casesForVentilatorsByRequestTime = (
                                                            impact_infectionsByRequestedTime * 0.02) // 1

    ##money the economy is likely to lose over the said normal impact period.
    impactDollarInFlight = (impact_infectionsByRequestedTime * data[
        'avgDailyIncomePopulation'] * data[
                                'avgDailyIncomeInUSD'] * data[
                                'timeToElapse']) // 1
    # money the economy is likely to lose over the said severe period.
    severeImpactDollarInFlight = (severeImpact_infectionsByRequestedTime * data['avgDailyIncomePopulation'] * data[
                                      'avgDailyIncomeInUSD'] * data['timeToElapse']) // 1
    Impact = {

        'impact_infectionsByRequestedTime': impact_infectionsByRequestedTime,
        'impact_severeCasesByRequestTime': impact_severeCasesByRequestTime,
        'hospitalCapacity': hospitalCapacity,
        'impact_hospitalBedsByRequestedTime': impact_hospitalBedsByRequestedTime,
        'impactCasesForICUByRequestTime': impactCasesForICUByRequestTime,
        'impact_casesForVentilatorsByRequestTime': impact_casesForVentilatorsByRequestTime,
        'impactDollarInFlight': impactDollarInFlight,

    }
    SevereImpact = {
        'severeImpact_infectionsByRequestedTime': severeImpact_infectionsByRequestedTime,
        'severeImpact_hospitalBedsByRequestedTime': severeImpact_hospitalBedsByRequestedTime,
        'severeImpact_severeCasesByRequestTime': severeImpact_severeCasesByRequestTime,
        'severeImpactCasesForICUByRequestTime': severeImpactCasesForICUByRequestTime,
        'severeImpact_casesForVentilatorsByRequestTime': severeImpact_casesForVentilatorsByRequestTime,
        'severeImpactDollarInFlight': severeImpactDollarInFlight
    }  # pylint : disable=invalid-name
    estimation = {
        'data': data, 'impact': Impact, 'severeImpact': SevereImpact
    }
    return json.dumps(estimation, indent=3)


ESTIMATOR = estimator(data)
print(ESTIMATOR)