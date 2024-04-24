from aima3.logic import FolKB, fol_fc_ask, expr
kb = FolKB()
name = 'Bassmala'

kb.tell(expr('name'))

kb = FolKB()

# Adding rules and assertions
kb.tell(expr('EnglishExcellent(x) & Reading(x) & Writing(x) & Art(x) & Working_alone(x) & Nothing(x) & No(x) ==> Orient(x, Literature)'))
kb.tell(expr('HistoryGood(x) & Reading(x) & Writing(x) & Art(x) & Working_alone(x) & Nothing(x) & No(x) ==> Orient(x, Literature)'))

kb.tell(expr('HistoryGood(x) & Debate(x) & Public_speaking(x) & Critical_Thinking(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Law)'))
kb.tell(expr('EthicsGood(x) & Debate(x) & Public_speaking(x) & Critical_Thinking(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Law)'))

kb.tell(expr('EconomicsExcellent(x) & Entrepreneurship(x) & Marketing(x) & Team_work(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('EconomicsExcellent(x) & Entrepreneurship(x) & Marketing(x) & Critical_Thinking(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('EconomicsExcellent(x) & Entrepreneurship(x) & Marketing(x) & Mentorship(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('AccountingExcellent(x) & Entrepreneurship(x) & Marketing(x) & Team_work(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('AccountingExcellent(x) & Entrepreneurship(x) & Marketing(x) & Critical_Thinking(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('AccountingExcellent(x) & Entrepreneurship(x) & Marketing(x) & Mentorship(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('MathGood(x) & Entrepreneurship(x) & Marketing(x) & Team_work(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('MathGood(x) & Entrepreneurship(x) & Marketing(x) & Critical_Thinking(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))
kb.tell(expr('MathGood(x) & Entrepreneurship(x) & Marketing(x) & Mentorship(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, Business)'))

kb.tell(expr('PhysicsExcellent(x) & Mentoring(x) & Expertize(x) & Critical_Thinking(x) & Organizing(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Teaching)'))
kb.tell(expr('MathsExcellent(x) & Mentoring(x) & Expertize(x) & Critical_Thinking(x) & Organizing(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Teaching)'))
kb.tell(expr('ScienceExcellent(x) & Mentoring(x) & Expertize(x) & Critical_Thinking(x) & Organizing(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Teaching)'))

kb.tell(expr('ChemistryExcellent(x) & Science(x) & Teamwork(x) & Communication(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Medicine)'))
kb.tell(expr('ChemistryExcellent(x) & Science(x) & Teamwork(x) & Attention_to_Detail(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Medicine)'))
kb.tell(expr('ChemistryExcellent(x) & Science(x) & Attention_to_Detail(x) & Communication(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Medicine)'))

kb.tell(expr('ChemistryExcellent(x) & Research(x) & Teamwork(x) & Communication(x) & Working_with_ppl(x) & Flexibility(x) & Yes(x) ==> Orient(x, Pharmacy)'))

kb.tell(expr('ChemistryGood(x) & Science(x) & Teamwork(x) & Communication(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Psychology)'))
kb.tell(expr('ChemistryGood(x) & Science(x) & Teamwork(x) & Analytical_Thinking(x) & Working_with_ppl(x) & Society_serving(x) & Yes(x) ==> Orient(x, Psychology)'))

kb.tell(expr('PhysicsGood(x) & Electronics(x) & Critical_Thinking(x) & Problem_solving(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, CS)'))
kb.tell(expr('MathExcellent(x) & PhysicsGood(x) & Electronics(x) & Critical_Thinking(x) & Problem_solving(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, CS)'))
kb.tell(expr('MathGood(x) & PhysicsGood(x) & Electronics(x) & Critical_Thinking(x) & Problem_solving(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, CS)'))
kb.tell(expr('PhysicsGood(x) & Programming(x) & Critical_Thinking(x) & Problem_solving(x) & Working_alone(x) & Flexibility(x) & Yes(x) ==> Orient(x, CS)'))

kb.tell(expr('Problem_solving(Rahma)'))
kb.tell(expr('PhysicsGood(Rahma)'))
kb.tell(expr('Programming(Rahma)'))
kb.tell(expr('Critical_Thinking(Rahma)'))
kb.tell(expr('Problem_solving(Rahma)'))
kb.tell(expr('Working_alone(Rahma)'))
kb.tell(expr('Flexibility(Rahma)'))
kb.tell(expr('Yes(Rahma)'))


# Query
result = fol_fc_ask(kb, expr('Orient(Rahma , x)'))
print(list(result))