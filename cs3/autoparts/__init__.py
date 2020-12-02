import check50

@check50.check()
def exists1():
    """Part.java exists"""
    check50.exists("Part.java")

@check50.check()
def exists2():
	"""PartList.java exists"""
	check50.exists("PartList.java")

@check50.check()
def exists3():
	"""PartsRunner.java exists"""
	check50.exists("PartsRunner.java")

@check50.check()
def example1():
    """Works for Part name with 1 word"""
    check50.run("java Grader Part0").stdout("Done!\n *Dodge +Ram +2021 +Radiator +23102 *", regex=True).exit(0)

@check50.check()
def example2():
    """Works for Part name with multiple words"""
    check50.run("java Grader Part1").stdout("Done!\n *Chevy +Silverado +2019 +Air +Filter +98765 *", regex=True).exit(0)

@check50.check()
def example3():
    """compareTo seems to work"""
    check50.run("java Grader Part2").stdout("Done!\ntruetrue", regex=False).exit(0)

@check50.check()
def example4():
    """PartList works"""
    check50.run("java Grader PartList").\
            stdout("Done!\\n *Chevy +Camaro +2009 +Wiper +Blades +12321 - 1 *\\n" +
            " *Chevy +Silvarado +2019 +Air +Filter +98765 - 2 *\\n" +
            " *Dodge +Ram +2012 +Radiator +23102 - 1 *\\n" +
            " *Ford +Expedition +2016 +Water +Pump +19912 - 1 *\\n" +
            " *Ford +Focus +2017 +Fuel +Filter +19967 - 1 *\\n" +
            " *Ford +Focus +2017 +Water +Pump +19934 - 2 *\\n*", regex=True).exit(0)

