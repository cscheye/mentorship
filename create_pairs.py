import sys

# Define a main() function that prints a little greeting.
'''
1. read and parse args
    - input file for mentee data
    - input file for mentors
    - output file location (optional; otherwise print to stdout)
2. process mentee file
    - create array of mentee objects
3. process mentor file
    - create array of mentor objects
4. pair people together
5. output to file or stdout
'''
def main():
  mentee = Mentee("snoopy", "IC2", "onboarding")
  mentor = Mentor("snoopy2", "IC3")
  pair = Pair(mentee, mentor)

  if (pair.isValidPair()):
    print("valid")
  else:
    print("invalid pair")


class Mentee:
  target_categories = {"onboarding", "career", "technical"}

  def __init__(self, ldap, level, targetCategory):
    self.ldap = ldap
    self.level = level
    self.targetCategory = targetCategory


  def isOnboarding(self):
    return self.targetCategory == "onboarding"

  def isCareerAdvancement(self):
    return self.targetCategory == "career"

  def isTechnical(self):
    return self.targetCategory == "technical"


class Mentor:
  def __init__(self, ldap, level):
    self.ldap = ldap
    self.level = level


class Pair:
  def __init__(self, mentee, mentor):
    self.mentee = mentee
    self.mentor = mentor

  def isValidPair(self):
    return self.__isNotSamePerson() \
      and self.__hasValidLeveling() \
      and self.__mentorExpertiseInMenteeInterest()

  def __isNotSamePerson(self):
    return self.mentee.ldap != self.mentor.ldap

  def __hasValidLeveling(self):
    levels = {
      "IC1": 1,
      "IC2": 2,
      "IC3": 3,
      "IC4": 4,
      "IC5": 5,
      "IC6": 6,
      "M3": 5,
      "M4": 6,
      "M5": 7
    }
    return levels[self.mentee.level] < levels[self.mentor.level]

  def __mentorExpertiseInMenteeInterest(self):
    # case 1: onboarding
    # case 2: career advancement
    # case 3: technical
    # Should we restrict to one of these three categories?

    if self.mentee.isOnboarding():
      print("onboarding mentee")
      return self.__checkOnboardingMatch()
    elif self.mentee.isTechnical():
      print("technical mentee")
    elif self.mentee.isCareerAdvancement():
      print("career advancement")
    else:
      print("unknown mentee category")

  def __checkOnboardingMatch(self):
    pass
    # level -- mentor is either m3+ or ic2+? ic3+?
    # time -- mentor is at etsy > 1 year


if __name__ == '__main__':
  main()
