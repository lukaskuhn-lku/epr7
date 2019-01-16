from member import Member
from professor import Professor
from research_group import Research_Group 
from presentation import Presentation 
from wimi import WiMi 

#Testen der einzelnen Klassen
test_professor = Professor(1, "Test", 6812)
test_wimi = WiMi(2, "Test 2")
test_presentation = Presentation("Test Presentation", "12-12-12")
test_research_group = Research_Group("Test Research Group", 666) #keine Ahnung was total_presentation sein soll

#Testen der Set/Get Head Funktion 
test_research_group.set_head(test_professor)
print(test_research_group.get_head())

#Testen der Add/Get Member Funktion 
test_research_group.add_member(test_professor)
print(test_research_group.get_member())